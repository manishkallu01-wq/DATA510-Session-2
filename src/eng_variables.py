#!/usr/bin/env python3
"""Engineer the final 40-column workbook from capstone_super_dataset.csv."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

FINAL = ["Date","UnemploymentRate","ConsumerPriceIndex","FederalFundsRate",
"GrossDomesticProduct","ConsumerSentiment","RecessionIndicator","InflationRateYoY",
"GDPGrowthYoY","RealInterestRate","UnemploymentChange1M","UnemploymentChange3M",
"ConsumerSentimentMomentum3M","UnemploymentLag1","UnemploymentLag3","UnemploymentLag6",
"UnemploymentLag12","InflationLag3","FederalFundsLag3","GDPGrowthLag3",
"ConsumerSentimentLag3","InflationLag6","FederalFundsLag6","GDPGrowthLag6",
"ConsumerSentimentLag6","EconomicStressIndex","LaborMarketShock",
"InflationAcceleration","GDPGrowthMomentum","UnemploymentMomentum",
"MonetaryTighteningIndex","PolicyPressureScore","ConsumerConfidenceDeterioration",
"InflationUnemploymentRatio","GrowthToInflationRatio","RecessionRiskScore",
"FutureUnemployment_3M","FutureUnemployment_6M","FutureUnemployment_12M",
"FutureLaborMarketShock_6M"]

def arguments():
    root=Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,
        default=root/"data"/"processed"/"capstone_super_dataset.csv")
    p.add_argument("--output",type=Path,
        default=root/"data"/"processed"/"capstone_plus_final.xlsx")
    return p.parse_args()

def engineer(df):
    needed={"Date","UNRATE","CPIAUCSL","FEDFUNDS","GDP","UMCSENT","USREC"}
    if missing:=sorted(needed-set(df.columns)):
        raise ValueError("Missing super-dataset columns: "+", ".join(missing))
    df=df.copy().rename(columns={"UNRATE":"UnemploymentRate",
        "CPIAUCSL":"ConsumerPriceIndex","FEDFUNDS":"FederalFundsRate",
        "GDP":"GrossDomesticProduct","UMCSENT":"ConsumerSentiment",
        "USREC":"RecessionIndicator"})
    df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
    df=df.sort_values("Date").drop_duplicates("Date",keep="last").reset_index(drop=True)
    df["InflationRateYoY"]=df.ConsumerPriceIndex.pct_change(12,fill_method=None)*100
    df["GDPGrowthYoY"]=df.GrossDomesticProduct.pct_change(12,fill_method=None)*100
    df["RealInterestRate"]=df.FederalFundsRate-df.InflationRateYoY
    df["UnemploymentChange1M"]=df.UnemploymentRate.diff()
    df["UnemploymentChange3M"]=df.UnemploymentRate.diff(3)
    df["ConsumerSentimentMomentum3M"]=df.ConsumerSentiment.diff(3)
    for lag in (1,3,6,12): df[f"UnemploymentLag{lag}"]=df.UnemploymentRate.shift(lag)
    for lag in (3,6):
        df[f"InflationLag{lag}"]=df.InflationRateYoY.shift(lag)
        df[f"FederalFundsLag{lag}"]=df.FederalFundsRate.shift(lag)
        df[f"GDPGrowthLag{lag}"]=df.GDPGrowthYoY.shift(lag)
        df[f"ConsumerSentimentLag{lag}"]=df.ConsumerSentiment.shift(lag)
    cols=["UnemploymentRate","InflationRateYoY","FederalFundsRate"]
    usable=df[cols].dropna()
    df["EconomicStressIndex"]=np.nan
    df.loc[usable.index,"EconomicStressIndex"]=StandardScaler().fit_transform(usable).mean(1)
    df["LaborMarketShock"]=(df.UnemploymentChange3M>=0.5).astype(int)
    df["InflationAcceleration"]=df.InflationRateYoY.diff()
    df["GDPGrowthMomentum"]=df.GDPGrowthYoY-df.GDPGrowthLag3
    df["UnemploymentMomentum"]=df.UnemploymentChange3M
    df["MonetaryTighteningIndex"]=df.FederalFundsRate-df.FederalFundsLag6
    df["PolicyPressureScore"]=df.FederalFundsRate*df.InflationRateYoY
    df["ConsumerConfidenceDeterioration"]=df.ConsumerSentimentLag6-df.ConsumerSentiment
    df["InflationUnemploymentRatio"]=df.InflationRateYoY/df.UnemploymentRate.replace(0,np.nan)
    df["GrowthToInflationRatio"]=df.GDPGrowthYoY/df.InflationRateYoY.replace(0,np.nan)
    df["RecessionRiskScore"]=(df.EconomicStressIndex.fillna(0)
        +df.RecessionIndicator.fillna(0)+df.LaborMarketShock)
    for n in (3,6,12): df[f"FutureUnemployment_{n}M"]=df.UnemploymentRate.shift(-n)
    df["FutureLaborMarketShock_6M"]=df.LaborMarketShock.shift(-6)
    df=df[(df.Date>="1956-04-01")&(df.Date<="2025-12-01")].copy()
    predictors=[c for c in FINAL if c!="Date" and not c.startswith("Future")]
    df=df.dropna(subset=predictors).reset_index(drop=True)[FINAL]
    numeric=[c for c in FINAL if c!="Date"]
    df[numeric]=df[numeric].round(2)
    return df

def main():
    args=arguments()
    if not args.input.is_file():
        raise FileNotFoundError(f"{args.input} not found; run src/rebuild.py first")
    df=engineer(pd.read_csv(args.input))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    df.to_excel(args.output,index=False,engine="openpyxl")
    print(f"Saved: {args.output}")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Range: {df.Date.min().date()} to {df.Date.max().date()}")

if __name__=="__main__":
    main()
