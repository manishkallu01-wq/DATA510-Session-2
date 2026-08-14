#!/usr/bin/env python3
from __future__ import annotations
import argparse, io, platform, urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from scipy import stats
try:
    import scipy
except ImportError as exc:
    raise SystemExit("Required packages: pandas numpy matplotlib scipy openpyxl. Install them and rerun.") from exc

OUTCOME="UnemploymentRate"
LEADS=[0,3,6,12]
INDICATORS=["InflationRateYoY","FederalFundsRate","GDPGrowthYoY","ConsumerSentiment","RecessionIndicator"]
DISPLAY={"InflationRateYoY":"Inflation rate (YoY)","FederalFundsRate":"Federal funds rate","GDPGrowthYoY":"GDP growth (YoY)","ConsumerSentiment":"Consumer sentiment","RecessionIndicator":"Recession indicator"}
ALIASES={"Date":["Date","DATE","date","ObservationDate","observation_date"],"UnemploymentRate":["UnemploymentRate","UNRATE","Unemployment Rate","unemployment_rate"],"InflationRateYoY":["InflationRateYoY","InflationYoY","Inflation Rate YoY","CPIInflationYoY","inflation_rate_yoy"],"FederalFundsRate":["FederalFundsRate","FEDFUNDS","Federal Funds Rate","federal_funds_rate"],"GDPGrowthYoY":["GDPGrowthYoY","GDP Growth YoY","RealGDPGrowthYoY","gdp_growth_yoy"],"ConsumerSentiment":["ConsumerSentiment","UMCSENT","Consumer Sentiment","consumer_sentiment"],"RecessionIndicator":["RecessionIndicator","USREC","Recession Indicator","recession_indicator"],"ConsumerPriceIndex":["ConsumerPriceIndex","CPIAUCSL","Consumer Price Index"],"GrossDomesticProduct":["GrossDomesticProduct","GDP","GDPC1","Gross Domestic Product"]}
PERIODS=[("1956–1979","1956-01-01","1979-12-31"),("1980–1999","1980-01-01","1999-12-31"),("2000–2009","2000-01-01","2009-12-31"),("2010–2019","2010-01-01","2019-12-31"),("2020–2025","2020-01-01","2025-12-31")]
COLORS={"InflationRateYoY":"#E11D48","FederalFundsRate":"#F97316","GDPGrowthYoY":"#2563EB","ConsumerSentiment":"#7C3AED","RecessionIndicator":"#0F9D8A"}
plt.rcParams.update({"figure.dpi":180,"savefig.dpi":900,"figure.facecolor":"white","axes.facecolor":"white","axes.grid":False,"font.family":"DejaVu Sans","font.size":10,"axes.titlesize":15,"axes.titleweight":"semibold","axes.labelsize":11,"legend.frameon":False})

def parse_args():
    p=argparse.ArgumentParser(description="Run the reproducible unemployment correlation analysis directly from the GitHub XLSX dataset.")
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

def resolve(columns,canonical):
    lookup={str(c).strip().lower():str(c) for c in columns}
    for alias in ALIASES.get(canonical,[canonical]):
        if alias.strip().lower() in lookup: return lookup[alias.strip().lower()]
    return None

def prepare_data(raw):
    df=raw.copy(); rename={}
    for canonical in ALIASES:
        src=resolve(df.columns,canonical)
        if src is not None: rename[src]=canonical
    df=df.rename(columns=rename)
    if "Date" not in df.columns or OUTCOME not in df.columns: raise ValueError("Date and UnemploymentRate are required.")
    df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
    if df["Date"].isna().any(): raise ValueError("Invalid Date values found.")
    df=df.sort_values("Date").drop_duplicates("Date",keep="last").reset_index(drop=True)
    if "InflationRateYoY" not in df.columns:
        if "ConsumerPriceIndex" not in df.columns: raise ValueError("InflationRateYoY or ConsumerPriceIndex is required.")
        df["InflationRateYoY"]=pd.to_numeric(df["ConsumerPriceIndex"],errors="coerce").pct_change(12,fill_method=None)*100
    if "GDPGrowthYoY" not in df.columns:
        if "GrossDomesticProduct" not in df.columns: raise ValueError("GDPGrowthYoY or GrossDomesticProduct is required.")
        df["GDPGrowthYoY"]=pd.to_numeric(df["GrossDomesticProduct"],errors="coerce").pct_change(12,fill_method=None)*100
    missing=[c for c in INDICATORS if c not in df.columns]
    if missing: raise ValueError("Required indicators missing: "+", ".join(missing))
    cols=[OUTCOME,*INDICATORS]; df[cols]=df[cols].apply(pd.to_numeric,errors="coerce").replace([np.inf,-np.inf],np.nan)
    if df[OUTCOME].isna().any(): raise ValueError("UnemploymentRate contains missing values.")
    for c in INDICATORS:
        if df[c].notna().sum()<24: raise ValueError(f"Insufficient usable observations for {c}.")
    return df

def paired(x,y):
    return pd.concat([x,y],axis=1).replace([np.inf,-np.inf],np.nan).dropna()

def pearson(x,y):
    p=paired(x,y)
    if len(p)<3 or p.iloc[:,0].nunique()<2 or p.iloc[:,1].nunique()<2: return np.nan,np.nan,len(p)
    r=stats.pearsonr(p.iloc[:,0],p.iloc[:,1]); return float(r.statistic),float(r.pvalue),len(p)

def spearman(x,y):
    p=paired(x,y)
    if len(p)<3 or p.iloc[:,0].nunique()<2 or p.iloc[:,1].nunique()<2: return np.nan,np.nan,len(p)
    r=stats.spearmanr(p.iloc[:,0],p.iloc[:,1]); return float(r.statistic),float(r.pvalue),len(p)

def build_lead_lag(df):
    rows=[]
    for ind in INDICATORS:
        for lead in LEADS:
            future=df[OUTCOME].shift(-lead); pr,pp,n=pearson(df[ind],future); sr,sp,_=spearman(df[ind],future)
            rows.append({"Indicator":DISPLAY[ind],"Lead":lead,"Pearson r":pr,"Pearson p":pp,"Spearman rho":sr,"Spearman p":sp,"N":n})
    return pd.DataFrame(rows)

def build_summary(ll):
    rows=[]
    for ind in INDICATORS:
        label=DISPLAY[ind]; s=ll[ll.Indicator==label].sort_values("Lead"); valid=s.dropna(subset=["Pearson r"]); best=valid.loc[valid["Pearson r"].abs().idxmax()]
        row={"Indicator":label,"Mean |Pearson r|":valid["Pearson r"].abs().mean(),"Strongest lead":int(best.Lead),"Strongest Pearson r":best["Pearson r"],"Strongest p":best["Pearson p"]}
        for lead in LEADS: row[f"r {lead}M"]=s.loc[s.Lead==lead,"Pearson r"].iloc[0]
        rows.append(row)
    return pd.DataFrame(rows).sort_values("Mean |Pearson r|",ascending=False).reset_index(drop=True)

def build_period_stability(df):
    rows=[]
    for period,start,end in PERIODS:
        d=df[df.Date.between(pd.Timestamp(start),pd.Timestamp(end))].copy()
        for ind in INDICATORS:
            r,p,n=pearson(d[ind],d[OUTCOME].shift(-6)); rows.append({"Period":period,"Indicator":DISPLAY[ind],"Pearson r at 6M":r,"p-value":p,"N":n})
    return pd.DataFrame(rows)

def build_recession_analysis(df):
    d=df[[OUTCOME,"RecessionIndicator"]].dropna().copy(); d["RecessionIndicator"]=(d.RecessionIndicator>0).astype(int); recession=d.loc[d.RecessionIndicator==1,OUTCOME]; expansion=d.loc[d.RecessionIndicator==0,OUTCOME]
    if recession.empty or expansion.empty: raise ValueError("RecessionIndicator must contain both 0 and 1 values.")
    pb=stats.pointbiserialr(d.RecessionIndicator,d[OUTCOME]); welch=stats.ttest_ind(recession,expansion,equal_var=False,nan_policy="omit")
    return pd.DataFrame({"Metric":["Mean unemployment during recessions","Mean unemployment during expansions","Difference: recession minus expansion","Point-biserial correlation","Point-biserial p-value","Welch t-test p-value","Recession observations","Expansion observations"],"Value":[recession.mean(),expansion.mean(),recession.mean()-expansion.mean(),pb.statistic,pb.pvalue,welch.pvalue,len(recession),len(expansion)]})

def print_table(title,frame,digits=3):
    f=frame.copy()
    for c in f.select_dtypes(include=[np.number]).columns: f[c]=f[c].map(lambda x:"NA" if pd.isna(x) else f"{x:.{digits}f}")
    print("\n"+title); print("="*len(title)); print(f.to_string(index=False))

def clean_axes(ax,left=True,bottom=True):
    ax.grid(False); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False); ax.spines["left"].set_visible(left); ax.spines["bottom"].set_visible(bottom)
    if left: ax.spines["left"].set_color("#CBD5E1")
    if bottom: ax.spines["bottom"].set_color("#CBD5E1")
    ax.tick_params(length=0,pad=6)

def heatmap(matrix,xlabels,ylabels,title):
    cmap=LinearSegmentedColormap.from_list("corr",["#6D28D9","#F8FAFC","#0F9D8A"]); norm=TwoSlopeNorm(vmin=-1,vcenter=0,vmax=1)
    fig,ax=plt.subplots(figsize=(9.6,6.1)); im=ax.imshow(matrix,cmap=cmap,norm=norm,aspect="auto"); ax.set_xticks(np.arange(len(xlabels))); ax.set_xticklabels(xlabels); ax.set_yticks(np.arange(len(ylabels))); ax.set_yticklabels(ylabels)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            v=matrix[i,j]; ax.text(j,i,"NA" if pd.isna(v) else f"{v:.2f}",ha="center",va="center",color="white" if pd.notna(v) and abs(v)>=.48 else "#13213C",fontweight="semibold",fontsize=9)
    ax.set_title(title,loc="left",pad=14); ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]; cb=fig.colorbar(im,ax=ax,fraction=.046,pad=.04); cb.set_label("Correlation coefficient"); cb.outline.set_visible(False); fig.tight_layout(); return fig,ax

def plot_same_month(df):
    labels=["Unemployment","Inflation","Fed funds","GDP growth","Sentiment","Recession"]; corr=df[[OUTCOME,*INDICATORS]].corr(method="pearson"); heatmap(corr.to_numpy(),labels,labels,"Same-Month Pearson Correlation Matrix")

def plot_lead_lag(ll):
    order=[DISPLAY[i] for i in INDICATORS]; p=ll.pivot(index="Indicator",columns="Lead",values="Pearson r").reindex(order).reindex(columns=LEADS); heatmap(p.to_numpy(),["Same month","3 months","6 months","12 months"],order,"Lead-Lag Correlations with Current and Future Unemployment")

def plot_profiles(ll):
    fig,ax=plt.subplots(figsize=(10.8,5.9))
    for ind in INDICATORS:
        s=ll[ll.Indicator==DISPLAY[ind]].sort_values("Lead"); ax.plot(s.Lead,s["Pearson r"],marker="o",markersize=5,lw=2.1,color=COLORS[ind],label=DISPLAY[ind])
    ax.axhline(0,color="#CBD5E1",lw=1); ax.set_xticks(LEADS); ax.set_ylim(-1,1); ax.set_xlabel("Months indicator leads unemployment"); ax.set_ylabel("Pearson correlation"); ax.set_title("Indicator Relationships Across Forecast Horizons",loc="left",pad=14); ax.legend(ncol=2,loc="upper right"); clean_axes(ax); fig.tight_layout()

def plot_ranking(summary):
    rank=summary.sort_values("Mean |Pearson r|",ascending=True); fig,ax=plt.subplots(figsize=(9.8,5.7)); colors=["#0F9D8A" if x>=0 else "#7C3AED" for x in rank["Strongest Pearson r"]]; bars=ax.barh(rank.Indicator,rank["Mean |Pearson r|"],color=colors,edgecolor="none",alpha=.92); maximum=rank["Mean |Pearson r|"].max()
    for b,(_,r) in zip(bars,rank.iterrows()): ax.text(b.get_width()+maximum*.018,b.get_y()+b.get_height()/2,f"{r['Mean |Pearson r|']:.3f} | best {int(r['Strongest lead'])}M, r={r['Strongest Pearson r']:.3f}",va="center",fontsize=8,color="#334155")
    ax.set_xlim(0,maximum*1.58); ax.set_xlabel("Mean absolute Pearson correlation across 0M, 3M, 6M, and 12M"); ax.set_title("Overall Historical Relationship Strength",loc="left",pad=14); clean_axes(ax,left=False); fig.tight_layout()

def plot_stability(stability):
    order=[DISPLAY[i] for i in INDICATORS]; p=stability.pivot(index="Indicator",columns="Period",values="Pearson r at 6M").reindex(order).reindex(columns=[x[0] for x in PERIODS]); heatmap(p.to_numpy(),p.columns.tolist(),order,"Six-Month Lead Correlations Across Historical Periods")

def plot_top_scatter(df,summary):
    for _,row in summary.head(3).iterrows():
        label=row.Indicator; ind=next(k for k,v in DISPLAY.items() if v==label); lead=int(row["Strongest lead"]); pair=pd.DataFrame({"Indicator":df[ind],"FutureUnemployment":df[OUTCOME].shift(-lead)}).dropna()
        if len(pair)<3: continue
        fit=stats.linregress(pair.Indicator,pair.FutureUnemployment); x=np.linspace(pair.Indicator.min(),pair.Indicator.max(),200); fig,ax=plt.subplots(figsize=(7.8,5.6)); ax.scatter(pair.Indicator,pair.FutureUnemployment,s=19,alpha=.34,color=COLORS[ind],edgecolors="none"); ax.plot(x,fit.intercept+fit.slope*x,color="#111827",lw=2.1); ax.set_xlabel(label); ax.set_ylabel("Unemployment rate (%)" if lead==0 else f"Unemployment rate {lead} months later (%)"); ax.set_title(f"{label} vs Unemployment — Strongest Lead ({lead}M)",loc="left",pad=14); ax.text(.98,.96,f"Pearson r = {fit.rvalue:.3f}\np-value = {fit.pvalue:.3g}\nN = {len(pair)}",transform=ax.transAxes,ha="right",va="top",fontsize=9,bbox={"boxstyle":"round,pad=.4","facecolor":"white","edgecolor":COLORS[ind],"alpha":.96}); clean_axes(ax); fig.tight_layout()

def plot_recession_means(df):
    d=df[[OUTCOME,"RecessionIndicator"]].dropna().copy(); d["Regime"]=np.where(d.RecessionIndicator>0,"Recession","Expansion"); means=d.groupby("Regime")[OUTCOME].mean().reindex(["Expansion","Recession"]); fig,ax=plt.subplots(figsize=(6.8,5.2)); bars=ax.bar(means.index,means.values,color=["#64748B","#E11D48"],width=.58,edgecolor="none")
    for b,v in zip(bars,means.values): ax.text(b.get_x()+b.get_width()/2,v+.06,f"{v:.2f}%",ha="center",va="bottom",fontweight="semibold")
    ax.set_ylabel("Mean unemployment rate (%)"); ax.set_title("Average Unemployment During Expansions and Recessions",loc="left",pad=14); clean_axes(ax,left=True); fig.tight_layout()

def run_analysis(show_plots=True):
    raw=load_from_github(); source=GITHUB_XLSX_URL; df=prepare_data(raw); ll=build_lead_lag(df); summary=build_summary(ll); stability=build_period_stability(df); recession=build_recession_analysis(df)
    same_month_pearson=df[[OUTCOME,*INDICATORS]].corr(method="pearson"); same_month_spearman=df[[OUTCOME,*INDICATORS]].corr(method="spearman")
    print("\nREPRODUCIBILITY ENVIRONMENT"); print("="*27); print(f"Python {platform.python_version()} | pandas {pd.__version__} | numpy {np.__version__} | scipy {scipy.__version__}"); print(f"Data source: {source}"); print(f"Rows: {len(df):,} | Date range: {df.Date.min().date()} to {df.Date.max().date()}")
    print_table("LEAD-LAG PEARSON AND SPEARMAN RESULTS",ll)
    print_table("INDICATOR STRENGTH SUMMARY",summary)
    print_table("SIX-MONTH LEAD STABILITY BY HISTORICAL PERIOD",stability)
    print_table("RECESSION VS EXPANSION ANALYSIS",recession)
    pearson_print=same_month_pearson.copy(); pearson_print.index=["Unemployment","Inflation","Fed funds","GDP growth","Sentiment","Recession"]; pearson_print.columns=pearson_print.index; print_table("SAME-MONTH PEARSON CORRELATION MATRIX",pearson_print.reset_index(names="Variable"))
    spearman_print=same_month_spearman.copy(); spearman_print.index=["Unemployment","Inflation","Fed funds","GDP growth","Sentiment","Recession"]; spearman_print.columns=spearman_print.index; print_table("SAME-MONTH SPEARMAN CORRELATION MATRIX",spearman_print.reset_index(names="Variable"))
    strongest=summary.iloc[0]; print(f"\nStrongest overall historical relationship: {strongest.Indicator}; mean |r|={strongest['Mean |Pearson r|']:.3f}; strongest lead={int(strongest['Strongest lead'])}M; Pearson r={strongest['Strongest Pearson r']:.3f}.")
    if show_plots:
        plot_same_month(df); plot_lead_lag(ll); plot_profiles(ll); plot_ranking(summary); plot_stability(stability); plot_top_scatter(df,summary); plot_recession_means(df); plt.show()
    return {"data":df,"lead_lag":ll,"summary":summary,"period_stability":stability,"recession_analysis":recession,"same_month_pearson":same_month_pearson,"same_month_spearman":same_month_spearman}

if __name__=="__main__":
    args=parse_args(); ANALYSIS=run_analysis(not args.no_plots)
