#!/usr/bin/env python3
"""Build one monthly super dataset from the six raw FRED CSV files."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

SERIES = ("UNRATE", "CPIAUCSL", "FEDFUNDS", "GDP", "UMCSENT", "USREC")

def arguments():
    root = Path(__file__).resolve().parents[1]
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--raw-dir", type=Path, default=root / "data" / "raw")
    p.add_argument("--output", type=Path,
                   default=root / "data" / "processed" / "capstone_super_dataset.csv")
    return p.parse_args()

def read_series(raw_dir: Path, name: str) -> pd.DataFrame:
    path = raw_dir / f"{name}.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Missing raw file: {path}")
    df = pd.read_csv(path).iloc[:, :2].copy()
    df.columns = ["Date", name]
    # FRED exports in this project contain both ISO and M/D/YY date strings.
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", format="mixed")
    future_mask = df["Date"] > pd.Timestamp("2026-12-31")
    df.loc[future_mask, "Date"] = df.loc[future_mask, "Date"] - pd.DateOffset(years=100)
    df[name] = pd.to_numeric(df[name], errors="coerce")
    return (df.dropna(subset=["Date"]).drop_duplicates("Date", keep="last")
              .sort_values("Date").reset_index(drop=True))

def build(raw_dir: Path) -> pd.DataFrame:
    source = {name: read_series(raw_dir, name) for name in SERIES}
    start = max(df["Date"].min() for df in source.values())
    end = min(pd.Timestamp("2025-12-01"), source["UNRATE"]["Date"].max())
    result = pd.DataFrame({"Date": pd.date_range(start, end, freq="MS")})
    for name, df in source.items():
        result = result.merge(df, on="Date", how="left", validate="one_to_one")
    result["GDP"] = result["GDP"].ffill()
    for name in ("UNRATE", "CPIAUCSL", "FEDFUNDS", "UMCSENT", "USREC"):
        result[name] = result[name].interpolate(method="linear", limit_area="inside")
    result["USREC"] = result["USREC"].round().astype("Int64")
    return result

def main():
    args = arguments()
    df = build(args.raw_dir.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"Saved: {args.output}")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Range: {df.Date.min().date()} to {df.Date.max().date()}")

if __name__ == "__main__":
    main()
