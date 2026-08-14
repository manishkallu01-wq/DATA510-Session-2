#!/usr/bin/env python3
from __future__ import annotations
import argparse, io, platform, urllib.request, warnings
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from sklearn.base import clone
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
try:
    import sklearn
    import xgboost
    from xgboost import XGBRegressor
except ImportError as exc:
    raise SystemExit("Required packages: pandas numpy matplotlib scikit-learn xgboost openpyxl. Install them and rerun.") from exc

warnings.filterwarnings("ignore", category=FutureWarning)
RANDOM_STATE=42
VALIDATION_START=pd.Timestamp("1989-01-01")
TEST_START=pd.Timestamp("1999-01-01")
TARGETS={"3M":("FutureUnemployment_3M",3),"6M":("FutureUnemployment_6M",6),"12M":("FutureUnemployment_12M",12)}
UNEMPLOYMENT_BASELINE_CANDIDATES=["UnemploymentRate","UnemploymentLag1","UnemploymentLag3","UnemploymentLag6","UnemploymentLag12","UnemploymentChange1M","UnemploymentChange3M","UnemploymentMomentum","LaborMarketShock"]
MODEL_COLORS={"Linear Regression":"#2563EB","Ridge Regression":"#7C3AED","Random Forest":"#0D9488","Extra Trees":"#F97316","Gradient Boosting":"#DB2777","XGBoost":"#0891B2"}
HORIZON_COLORS={"3M":"#2563EB","6M":"#0D9488","12M":"#7C3AED"}
RECESSIONS=[("2001 recession","2001-03-01","2001-11-30","#FFF4D6"),("Great Recession","2007-12-01","2009-06-30","#FCE8EC"),("COVID-19 recession","2020-02-01","2020-04-30","#EEEAFE")]
plt.rcParams.update({"figure.dpi":180,"savefig.dpi":900,"figure.facecolor":"white","axes.facecolor":"white","axes.grid":False,"font.family":"DejaVu Sans","font.size":10,"axes.titlesize":15,"axes.titleweight":"semibold","axes.labelsize":11,"legend.frameon":False})

def parse_args():
    p=argparse.ArgumentParser(description="Run the reproducible six-model U.S. unemployment forecasting analysis directly from the GitHub XLSX dataset.")
    p.add_argument("--no-plots",action="store_true",help="Run calculations and print tables without opening figures.")
    return p.parse_args()

GITHUB_XLSX_URL="https://raw.githubusercontent.com/manishkallu01-wq/DATA510-Session-2/main/data/processed/capstone_plus_final.xlsx"
EXPECTED_ROWS=837
EXPECTED_COLUMNS=40

def load_from_github():
    print("Reading analysis dataset directly from GitHub:\n"+GITHUB_XLSX_URL)
    try:
        request=urllib.request.Request(GITHUB_XLSX_URL,headers={"User-Agent":"Mozilla/5.0","Accept":"application/octet-stream","Cache-Control":"no-cache"})
        with urllib.request.urlopen(request,timeout=90) as response:
            content=response.read()
    except Exception as exc:
        raise RuntimeError(f"Unable to read the project dataset from GitHub. Confirm internet access and that the repository path is public. Original error: {exc}") from exc
    if len(content)<10000:
        raise RuntimeError(f"GitHub returned an unexpectedly small response ({len(content)} bytes). The XLSX path may be unavailable.")
    try:
        data=pd.read_excel(io.BytesIO(content),engine="openpyxl")
    except Exception as exc:
        raise RuntimeError(f"GitHub responded, but the XLSX workbook could not be read: {exc}") from exc
    if data.shape!=(EXPECTED_ROWS,EXPECTED_COLUMNS):
        raise RuntimeError(f"GitHub workbook shape is {data.shape[0]} rows × {data.shape[1]} columns; expected the submitted final dataset shape {EXPECTED_ROWS} × {EXPECTED_COLUMNS}.")
    print(f"GitHub workbook loaded in memory only: {len(data):,} rows × {data.shape[1]} columns")
    return data

def build_models():
    return {"Linear Regression":Pipeline([("scale",StandardScaler()),("model",LinearRegression())]),"Ridge Regression":Pipeline([("scale",StandardScaler()),("model",Ridge(alpha=10.0))]),"Random Forest":RandomForestRegressor(n_estimators=200,max_depth=10,min_samples_leaf=2,max_features="sqrt",random_state=RANDOM_STATE,n_jobs=1),"Extra Trees":ExtraTreesRegressor(n_estimators=200,max_depth=12,min_samples_leaf=2,max_features=1.0,random_state=RANDOM_STATE,n_jobs=1),"Gradient Boosting":GradientBoostingRegressor(n_estimators=200,learning_rate=0.04,max_depth=3,min_samples_leaf=3,subsample=0.90,random_state=RANDOM_STATE,loss="squared_error"),"XGBoost":XGBRegressor(n_estimators=250,learning_rate=0.04,max_depth=3,min_child_weight=3,subsample=0.90,colsample_bytree=0.90,reg_alpha=0.05,reg_lambda=1.0,objective="reg:squarederror",eval_metric="rmse",random_state=RANDOM_STATE,n_jobs=1,verbosity=0)}

def metrics(y,p):
    y=np.asarray(y,dtype=float); p=np.asarray(p,dtype=float)
    return {"MAE":mean_absolute_error(y,p),"RMSE":float(np.sqrt(mean_squared_error(y,p))),"R2":r2_score(y,p)}

def prepare_data(raw):
    df=raw.copy()
    required={"Date","UnemploymentRate",*[x[0] for x in TARGETS.values()]}
    missing=sorted(required-set(df.columns))
    if missing: raise ValueError("Required columns missing: "+", ".join(missing))
    df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
    if df["Date"].isna().any(): raise ValueError("Invalid Date values found.")
    df=df.sort_values("Date").drop_duplicates("Date",keep="last").reset_index(drop=True)
    numeric=[c for c in df.columns if c!="Date"]
    df[numeric]=df[numeric].apply(pd.to_numeric,errors="coerce").replace([np.inf,-np.inf],np.nan)
    predictors=[c for c in numeric if not c.startswith("Future")]
    if not predictors: raise ValueError("No predictor columns found.")
    miss=df[predictors].isna().sum(); miss=miss[miss>0]
    if not miss.empty: raise ValueError("Predictor missingness found; final analysis expects complete predictors: "+", ".join(f"{k}={int(v)}" for k,v in miss.items()))
    if df[predictors].isin([np.inf,-np.inf]).any().any(): raise ValueError("Infinite predictor values found.")
    baseline=[c for c in UNEMPLOYMENT_BASELINE_CANDIDATES if c in predictors]
    if not baseline: raise ValueError("No unemployment-only baseline features found.")
    return df,predictors,baseline

def make_splits(df,months):
    dates=df["Date"]
    train_cutoff=VALIDATION_START-pd.DateOffset(months=months)
    validation_cutoff=TEST_START-pd.DateOffset(months=months)
    idx={"train":np.flatnonzero(dates<train_cutoff),"validation":np.flatnonzero((dates>=VALIDATION_START)&(dates<validation_cutoff)),"pretest":np.flatnonzero(dates<validation_cutoff),"test":np.flatnonzero(dates>=TEST_START)}
    if any(len(idx[k])==0 for k in idx): raise ValueError(f"Empty chronological split for {months}-month horizon.")
    return idx

def print_table(title,frame,digits=3):
    f=frame.copy()
    for c in f.select_dtypes(include=[np.number]).columns: f[c]=f[c].map(lambda x:"NA" if pd.isna(x) else f"{x:.{digits}f}")
    print("\n"+title); print("="*len(title)); print(f.to_string(index=False))

def clean_axes(ax,left=True,bottom=True):
    ax.grid(False); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False); ax.spines["left"].set_visible(left); ax.spines["bottom"].set_visible(bottom)
    if left: ax.spines["left"].set_color("#CBD5E1")
    if bottom: ax.spines["bottom"].set_color("#CBD5E1")
    ax.tick_params(length=0,pad=6)

def add_recessions(ax):
    for _,s,e,c in RECESSIONS: ax.axvspan(pd.Timestamp(s),pd.Timestamp(e),color=c,alpha=.65,linewidth=0,zorder=0)

def add_recession_labels(ax):
    y0,y1=ax.get_ylim(); y=y1-(y1-y0)*.055
    for name,s,e,_ in RECESSIONS:
        mid=pd.Timestamp(s)+(pd.Timestamp(e)-pd.Timestamp(s))/2
        ax.text(mid,y,name,ha="center",va="top",fontsize=7.5,color="#475569",fontweight="semibold")

def plot_model_rmse(results):
    order=list(build_models()); pivot=results.pivot(index="Model",columns="Horizon",values="Test RMSE").reindex(order).reindex(columns=["3M","6M","12M"])
    fig,ax=plt.subplots(figsize=(11.5,6.2)); y=np.arange(len(order)); h=.22
    for offset,horizon in [(-h,"3M"),(0,"6M"),(h,"12M")]:
        values=pivot[horizon].to_numpy(float); bars=ax.barh(y+offset,values,height=.17,color=HORIZON_COLORS[horizon],label=horizon,edgecolor="none")
        for b,v in zip(bars,values): ax.text(v+.018,b.get_y()+b.get_height()/2,f"{v:.2f}",va="center",fontsize=8,color="#334155")
    ax.set_yticks(y); ax.set_yticklabels(order); ax.invert_yaxis(); ax.set_xlabel("Test RMSE (unemployment percentage points; lower is better)"); ax.set_title("Six-Model Test RMSE Comparison Across Forecast Horizons",loc="left",pad=14); ax.legend(title="Horizon",ncol=3,loc="upper right"); clean_axes(ax,left=False); fig.tight_layout()

def plot_selected_forecasts(predictions,selected):
    for horizon,winner in selected.items():
        p=predictions[(predictions.Horizon==horizon)&(predictions.Model==winner)].sort_values("TargetDate")
        fig,ax=plt.subplots(figsize=(12.5,5.8)); add_recessions(ax); ax.plot(p.TargetDate,p.Actual,color="#111827",lw=2.35,label="Actual",zorder=5); ax.plot(p.TargetDate,p.Predicted,color=MODEL_COLORS[winner],lw=2.05,label=f"Predicted — {winner}",zorder=5)
        ax.set_title(f"{horizon} Selected Unemployment Forecast — {winner}",loc="left",pad=14); ax.set_xlabel("Target date"); ax.set_ylabel("Unemployment rate (%)"); ax.xaxis.set_major_locator(mdates.YearLocator(4)); ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y")); ax.legend(loc="upper right"); clean_axes(ax); add_recession_labels(ax); fig.tight_layout()

def plot_all_model_forecasts(predictions):
    for horizon in TARGETS:
        p0=predictions[predictions.Horizon==horizon]; actual=p0.sort_values("TargetDate").drop_duplicates("TargetDate")
        fig,ax=plt.subplots(figsize=(12.8,6.2)); add_recessions(ax); ax.plot(actual.TargetDate,actual.Actual,color="#111827",lw=2.5,label="Actual",zorder=6)
        for name in build_models():
            p=p0[p0.Model==name].sort_values("TargetDate"); ax.plot(p.TargetDate,p.Predicted,color=MODEL_COLORS[name],lw=1.35,alpha=.9,label=name,zorder=4)
        ax.set_title(f"{horizon} Forecast Comparison — All Six Models",loc="left",pad=14); ax.set_xlabel("Target date"); ax.set_ylabel("Unemployment rate (%)"); ax.xaxis.set_major_locator(mdates.YearLocator(4)); ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y")); ax.legend(ncol=2,loc="upper right"); clean_axes(ax); add_recession_labels(ax); fig.tight_layout()

def plot_feature_importance(importances,selected):
    for horizon,winner in selected.items():
        top=importances[horizon].head(12).sort_values("Importance",ascending=True)
        fig,ax=plt.subplots(figsize=(9.5,6.1)); bars=ax.barh(top.Feature,top.Importance,color=MODEL_COLORS[winner],alpha=.9,edgecolor="none")
        for b,v in zip(bars,top.Importance): ax.text(v+max(top.Importance.max()*.015,.0001),b.get_y()+b.get_height()/2,f"{v:.3f}",va="center",fontsize=8,color="#334155")
        ax.set_xlabel("Permutation importance (increase in MAE when permuted)"); ax.set_title(f"{horizon} Top Predictive Features — {winner}",loc="left",pad=14); clean_axes(ax,left=False); fig.tight_layout()

def plot_residuals(predictions,selected):
    for horizon,winner in selected.items():
        p=predictions[(predictions.Horizon==horizon)&(predictions.Model==winner)].sort_values("TargetDate").copy(); p["Residual"]=p.Actual-p.Predicted
        fig,ax=plt.subplots(figsize=(11.5,4.8)); ax.scatter(p.Predicted,p.Residual,s=22,alpha=.55,color=MODEL_COLORS[winner],edgecolors="none"); ax.axhline(0,color="#111827",lw=1.2); ax.set_xlabel("Predicted unemployment rate (%)"); ax.set_ylabel("Residual: actual − predicted"); ax.set_title(f"{horizon} Residual Diagnostics — {winner}",loc="left",pad=14); clean_axes(ax); fig.tight_layout()

def run_analysis(show_plots=True):
    raw=load_from_github(); source=GITHUB_XLSX_URL; df,predictors,baseline_features=prepare_data(raw)
    print("\nREPRODUCIBILITY ENVIRONMENT"); print("="*27); print(f"Python {platform.python_version()} | pandas {pd.__version__} | numpy {np.__version__} | scikit-learn {sklearn.__version__} | xgboost {xgboost.__version__}")
    print(f"Data source: {source}"); print(f"Rows: {len(df):,} | Columns: {df.shape[1]} | Predictors: {len(predictors)} | Date range: {df.Date.min().date()} to {df.Date.max().date()}")
    target_missing={t:int(df[t].isna().sum()) for t,_ in TARGETS.values()}; print("Target missingness (expected at series end): "+", ".join(f"{k}={v}" for k,v in target_missing.items())); print(f"Duplicate dates: {int(df.Date.duplicated().sum())} | Predictor missing values: {int(df[predictors].isna().sum().sum())}")
    result_rows=[]; prediction_frames=[]; selected={}; fitted_models={}; importance_by_horizon={}; baseline_rows=[]; split_rows=[]
    for horizon,(target,months) in TARGETS.items():
        hd=df.dropna(subset=[target]).reset_index(drop=True); idx=make_splits(hd,months); X=hd[predictors]; y=hd[target]; templates=build_models(); validation_scores={}; fitted_models[horizon]={}
        split_rows.append({"Horizon":horizon,"Initial train rows":len(idx["train"]),"Validation rows":len(idx["validation"]),"Final pre-test fit rows":len(idx["pretest"]),"Test rows":len(idx["test"]),"Test origin start":hd.Date.iloc[idx["test"]].min().date(),"Test origin end":hd.Date.iloc[idx["test"]].max().date()})
        for name,template in templates.items():
            m=clone(template); m.fit(X.iloc[idx["train"]],y.iloc[idx["train"]]); validation_scores[name]=metrics(y.iloc[idx["validation"]],m.predict(X.iloc[idx["validation"]]))
        winner=min(validation_scores,key=lambda n:(validation_scores[n]["RMSE"],validation_scores[n]["MAE"])); selected[horizon]=winner
        for name,template in templates.items():
            m=clone(template); m.fit(X.iloc[idx["pretest"]],y.iloc[idx["pretest"]]); pred=m.predict(X.iloc[idx["test"]]); fitted_models[horizon][name]=m; test=metrics(y.iloc[idx["test"]],pred); val=validation_scores[name]
            result_rows.append({"Horizon":horizon,"Model":name,"Val MAE":val["MAE"],"Val RMSE":val["RMSE"],"Val R2":val["R2"],"Test MAE":test["MAE"],"Test RMSE":test["RMSE"],"Test R2":test["R2"],"Selected":"Yes" if name==winner else "No"})
            origins=hd.Date.iloc[idx["test"]].reset_index(drop=True); prediction_frames.append(pd.DataFrame({"Horizon":horizon,"Model":name,"ForecastOriginDate":origins,"TargetDate":origins+pd.DateOffset(months=months),"Actual":y.iloc[idx["test"]].to_numpy(),"Predicted":pred}))
        selected_model=fitted_models[horizon][winner]; perm=permutation_importance(selected_model,X.iloc[idx["test"]],y.iloc[idx["test"]],scoring="neg_mean_absolute_error",n_repeats=5,random_state=RANDOM_STATE,n_jobs=1)
        importance_by_horizon[horizon]=pd.DataFrame({"Feature":predictors,"Importance":perm.importances_mean,"Std":perm.importances_std}).sort_values("Importance",ascending=False).reset_index(drop=True)
        selected_test=metrics(y.iloc[idx["test"]],selected_model.predict(X.iloc[idx["test"]])); persistence=metrics(y.iloc[idx["test"]],X.iloc[idx["test"]]["UnemploymentRate"].to_numpy()); baseline_model=Pipeline([("scale",StandardScaler()),("model",LinearRegression())]); baseline_model.fit(hd[baseline_features].iloc[idx["pretest"]],y.iloc[idx["pretest"]]); unemp_only=metrics(y.iloc[idx["test"]],baseline_model.predict(hd[baseline_features].iloc[idx["test"]]))
        for approach,m in [("Persistence",persistence),("Unemployment-Only Linear",unemp_only),(f"Selected Full Model: {winner}",selected_test)]: baseline_rows.append({"Horizon":horizon,"Approach":approach,**m})
    results=pd.DataFrame(result_rows); predictions=pd.concat(prediction_frames,ignore_index=True); baselines=pd.DataFrame(baseline_rows); splits=pd.DataFrame(split_rows)
    print_table("CHRONOLOGICAL SPLIT AUDIT",splits)
    for h in TARGETS: print_table(f"{h} — SIX-MODEL VALIDATION AND TEST RESULTS",results[results.Horizon==h][["Model","Val MAE","Val RMSE","Val R2","Test MAE","Test RMSE","Test R2","Selected"]].sort_values(["Val RMSE","Val MAE"]))
    selected_summary=results[results.Selected=="Yes"][["Horizon","Model","Val RMSE","Test MAE","Test RMSE","Test R2"]].copy()
    base_pivot=baselines.pivot(index="Horizon",columns="Approach",values="RMSE")
    for i,row in selected_summary.iterrows():
        h=row.Horizon; selected_rmse=row["Test RMSE"]; selected_summary.loc[i,"RMSE improvement vs persistence (%)"]=(base_pivot.loc[h,"Persistence"]-selected_rmse)/base_pivot.loc[h,"Persistence"]*100; selected_summary.loc[i,"RMSE improvement vs unemployment-only (%)"]=(base_pivot.loc[h,"Unemployment-Only Linear"]-selected_rmse)/base_pivot.loc[h,"Unemployment-Only Linear"]*100
    print_table("SELECTED MODEL SUMMARY",selected_summary)
    print_table("BASELINE COMPARISON",baselines)
    for h in TARGETS: print_table(f"{h} — TOP 12 PERMUTATION IMPORTANCE",importance_by_horizon[h].head(12))
    if show_plots:
        plot_model_rmse(results); plot_selected_forecasts(predictions,selected); plot_all_model_forecasts(predictions); plot_feature_importance(importance_by_horizon,selected); plot_residuals(predictions,selected); plt.show()
    return {"data":df,"predictors":predictors,"models":fitted_models,"results":results,"selected_models":selected,"predictions":predictions,"baselines":baselines,"feature_importance":importance_by_horizon,"splits":splits}

if __name__=="__main__":
    args=parse_args(); ANALYSIS=run_analysis(not args.no_plots)
