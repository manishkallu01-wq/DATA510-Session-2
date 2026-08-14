# 🗃️ Data Directory

This folder contains the six public source series and the submitted analysis-ready workbook for **Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators**.

## 📁 Contents

| Path | Purpose |
| --- | --- |
| [`raw/`](raw/) | Six original public macroeconomic CSV files used for optional reconstruction |
| [`processed/capstone_plus_final.xlsx`](processed/capstone_plus_final.xlsx) | Submitted common input for the final machine-learning and RQ2 correlation analyses |
| [`SCHEMA.md`](SCHEMA.md) | Column definitions, units, feature descriptions, and target notation |

## 📥 Raw Source Files

| File | Series | Measure | Provider |
| --- | --- | --- | --- |
| [`UNRATE.csv`](raw/UNRATE.csv) | UNRATE | U.S. unemployment rate | Bureau of Labor Statistics via FRED |
| [`CPIAUCSL.csv`](raw/CPIAUCSL.csv) | CPIAUCSL | Consumer Price Index | Bureau of Labor Statistics via FRED |
| [`FEDFUNDS.csv`](raw/FEDFUNDS.csv) | FEDFUNDS | Effective federal funds rate | Federal Reserve via FRED |
| [`GDP.csv`](raw/GDP.csv) | GDP | Gross Domestic Product, current dollars | Bureau of Economic Analysis via FRED |
| [`UMCSENT.csv`](raw/UMCSENT.csv) | UMCSENT | Consumer sentiment | University of Michigan via FRED |
| [`USREC.csv`](raw/USREC.csv) | USREC | U.S. recession indicator | NBER via FRED |

These files contain aggregate public economic data. They do not contain personal records, protected attributes, credentials, or individual employment histories. Source organizations retain ownership, and downstream users remain responsible for the providers' applicable terms and attribution requirements.

## ✅ Submitted Processed Dataset

The final report identifies `data/processed/capstone_plus_final.xlsx` as the common analysis-ready input for both research questions.

| Attribute | Final value |
| --- | --- |
| Study period | April 1956-December 2025 |
| Grain | One observation per month |
| Rows | 837 |
| Columns | 40 |
| Predictors | 35 |
| Duplicate dates | 0 |
| Infinite numeric values | 0 |
| Unexpected missing predictor values | 0 |
| Intentional missing unemployment targets | 3 at 3M, 6 at 6M, and 12 at 12M |

Future-target missing values occur only at the end of the series because those future unemployment observations are not yet available.

## 🔁 Two Supported Uses

### Use the submitted dataset directly

Most readers should read or download [`processed/capstone_plus_final.xlsx`](processed/capstone_plus_final.xlsx). The final analysis scripts in [`../deliverables/M5-final/`](../deliverables/M5-final/) use this submitted workbook through its public, read-only GitHub URL.

### Reconstruct a local dataset

The optional scripts in [`../src/`](../src/) read the six files in `raw/`, create a local `super_dataset.csv`, engineer a local `capstone_plus_final.xlsx`, and validate that local workbook.

Generated reconstruction files default to the user's local `Downloads` folder. The scripts do not write generated datasets into this repository and do not commit, push, or upload anything to GitHub.

## ⚠️ Interpretation Boundaries

- Quarterly GDP is aligned to the monthly panel before feature engineering.
- Historical values may include revisions and are not a real-time vintage archive.
- NBER recession dates are retrospective and must not be represented as contemporaneously available signals.
- Unemployment-derived features are not independent external evidence.
- The dataset supports national historical analysis; it does not support individual or subgroup predictions.

Return to the [project README](../README.md) for methods, results, and responsible-use guidance.
