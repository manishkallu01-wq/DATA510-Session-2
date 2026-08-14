#!/usr/bin/env python3
"""Validate the final analysis-ready workbook."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

ROWS,COLUMNS=837,40
START,END=pd.Timestamp("1956-04-01"),pd.Timestamp("2025-12-01")
TARGET_MISSING={"FutureUnemployment_3M":3,"FutureUnemployment_6M":6,
    "FutureUnemployment_12M":12,"FutureLaborMarketShock_6M":6}

def arguments():
    root=Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,
        default=root/"data"/"processed"/"capstone_plus_final.xlsx")
    return p.parse_args()

def validate(path):
    if not path.is_file(): raise FileNotFoundError(f"Final dataset not found: {path}")
    df=pd.read_excel(path,engine="openpyxl"); errors=[]
    if df.shape!=(ROWS,COLUMNS): errors.append(f"shape {df.shape}, expected {(ROWS,COLUMNS)}")
    if "Date" not in df: errors.append("Date column is missing")
    else:
        dates=pd.to_datetime(df.Date,errors="coerce")
        if dates.isna().any(): errors.append("invalid dates")
        if dates.duplicated().any(): errors.append("duplicate dates")
        if dates.min()!=START or dates.max()!=END:
            errors.append(f"date range {dates.min()} to {dates.max()}")
        expected=pd.Series(pd.date_range(START,END,freq="MS"),name="Date")
        if not dates.reset_index(drop=True).equals(expected):
            errors.append("dates are not a complete ordered monthly sequence")
    numeric=df.select_dtypes(include="number")
    if np.isinf(numeric.to_numpy()).any(): errors.append("infinite numeric values")
    predictors=[c for c in df if c!="Date" and not c.startswith("Future")]
    missing=df[predictors].isna().sum(); missing=missing[missing>0]
    if not missing.empty: errors.append(f"predictor missingness {missing.to_dict()}")
    for target,count in TARGET_MISSING.items():
        if target not in df: errors.append(f"missing target {target}")
        elif int(df[target].isna().sum())!=count:
            errors.append(f"{target} missing={df[target].isna().sum()}, expected {count}")
    if errors: raise SystemExit("FINAL DATASET CHECK FAILED:\n- "+"\n- ".join(errors))
    print("FINAL DATASET CHECK PASSED")
    print(f"File: {path}")
    print(f"Shape: {ROWS} rows x {COLUMNS} columns")
    print(f"Range: {START.date()} to {END.date()}")
    print("Duplicate dates: 0 | Infinite values: 0 | Missing predictors: 0")

if __name__=="__main__":
    validate(arguments().input.resolve())
