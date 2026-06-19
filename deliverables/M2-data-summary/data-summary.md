# 📊 Milestone 2: Data Summary

## Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

**Author:** Manish R Kallu

**Course:** DATA 510 – Capstone Project

**Studio Session:** 2

**Dataset Version:** `capstone_capstone_plus_final.csv`

---

# 🎯 1. Research Question Reminder

The goal of this project is to understand how major macroeconomic indicators influence unemployment in the United States and whether those indicators can improve unemployment forecasting across multiple forecasting horizons.

### Primary Research Question

> To what extent can publicly available macroeconomic indicators improve forecasting of future U.S. unemployment across 3-month, 6-month, and 12-month forecasting horizons?

### Secondary Research Question

> Which macroeconomic indicators have the strongest historical relationship with unemployment across U.S. economic cycles?

To answer these questions, six public economic datasets were collected from FRED, standardized to a common monthly timeline, and integrated into a single analysis-ready dataset. The resulting dataset spans nearly 70 years of U.S. economic history and contains all information required to answer the approved research questions. At this stage, data collection and engineering work are complete, allowing the remainder of the project to focus on analysis, forecasting, visualization, and reporting.

---

# 📦 2. Data Inventory

## Source Datasets

| Dataset  | Source                             | License / Terms        | Date Range | Rows | Refresh Policy      | Repository Location               |
| -------- | ---------------------------------- | ---------------------- | ---------- | ---- | ------------------- | --------------------------------- |
| UNRATE   | FRED / Bureau of Labor Statistics  | Public Government Data | 1956–2026  | 838  | Monthly             | `data/raw/unemployment.csv`       |
| CPIAUCSL | FRED / Bureau of Labor Statistics  | Public Government Data | 1956–2026  | 838  | Monthly             | `data/raw/inflation.csv`          |
| FEDFUNDS | FRED / Federal Reserve             | Public Government Data | 1956–2026  | 838  | Monthly             | `data/raw/federal_funds.csv`      |
| GDP      | FRED / Bureau of Economic Analysis | Public Government Data | 1956–2026  | 838  | Quarterly → Monthly | `data/raw/gdp.csv`                |
| UMCSENT  | University of Michigan / FRED      | Public Research Data   | 1956–2026  | 838  | Monthly             | `data/raw/consumer_sentiment.csv` |
| USREC    | NBER / FRED                        | Public Economic Data   | 1956–2026  | 838  | Monthly             | `data/raw/recession.csv`          |

## Final Analysis Dataset

| Metric              | Value                              |
| ------------------- | ---------------------------------- |
| File Name           | `capstone_capstone_plus_final.csv` |
| Repository Location | `data/processed/`                  |
| Observation Period  | April 1956 – January 2026          |
| Total Records       | 838                                |
| Total Variables     | 40                                 |
| Source Variables    | 6                                  |
| Engineered Features | 27                                 |
| Forecast Targets    | 4                                  |

---

# 🏗️ 3. Schema and Organization

## Repository Data Layout

```text
data/
├── raw/
│   ├── unemployment.csv
│   ├── inflation.csv
│   ├── federal_funds.csv
│   ├── gdp.csv
│   ├── consumer_sentiment.csv
│   └── recession.csv
│
├── processed/
│   └── capstone_capstone_plus_final.csv
│
├── README.md
└── SCHEMA.md
```

## Primary Key

* `Date`

## Join Strategy

All datasets were standardized to monthly frequency and merged using the `Date` field as the common key.

## Data Layers

### Raw Layer

Contains original source datasets downloaded from FRED.

### Processed Layer

Contains the final analysis-ready dataset used for forecasting, visualization, and statistical analysis.

## Dataset Structure

### Core Economic Indicators

* UnemploymentRate
* ConsumerPriceIndex
* FederalFundsRate
* GrossDomesticProduct
* ConsumerSentiment
* RecessionIndicator

### Engineered Features

The final dataset includes lag variables, momentum indicators, growth rates, policy indicators, economic stress measures, recession risk indicators, and forecasting targets engineered from the original source variables.

---

# ⚙️ 4. Ingestion Status

Data ingestion and integration have been completed.

### Workflow Summary

1. Retrieved six approved economic datasets from FRED.
2. Standardized all timestamps and variable names.
3. Converted GDP observations into a monthly analytical framework.
4. Aligned datasets using a common monthly timeline.
5. Merged all datasets on the Date field.
6. Generated engineered features including:

   * Lag variables
   * Growth indicators
   * Momentum indicators
   * Policy measures
   * Composite economic indicators
7. Generated forecasting targets.
8. Validated the final dataset.

### Pipeline Status

✅ Data acquisition complete

✅ Data integration complete

✅ Feature engineering complete

✅ Validation complete

✅ Analysis-ready dataset generated

The ingestion process successfully produced:

```text
data/processed/capstone_capstone_plus_final.csv
```

No additional ingestion work is required.

---

# 🔍 5. Data Quality and Profiling

Several validation checks were performed to ensure the final dataset is suitable for analysis and forecasting.

## Dataset Validation Results

| Validation Check         | Result |
| ------------------------ | ------ |
| Total Records            | 838    |
| Total Variables          | 40     |
| Duplicate Rows           | 0      |
| Duplicate Dates          | 0      |
| Missing Monthly Periods  | 0      |
| Infinite Values          | 0      |
| Missing Predictor Values | 0      |

## Missing Value Assessment

The only missing values occur in future forecasting targets.

| Variable               | Missing Values |
| ---------------------- | -------------- |
| FutureUnemployment_3M  | 3              |
| FutureUnemployment_6M  | 6              |
| FutureUnemployment_12M | 12             |

These values are expected because future unemployment observations do not exist beyond the final months of the dataset.

## Data Quality Findings

### Duplicates

* No duplicate rows detected.
* No duplicate dates detected.

### Missingness

* No missing predictor variables.
* Missing target values occur only because of forecasting horizon construction.

### Outliers

Periods such as the 1980 inflation shock, the 2008 financial crisis, and the COVID-19 recession contain extreme observations. These observations were intentionally retained because they represent real economic events and are important for forecasting performance evaluation.

### Known Limitations

* GDP is originally published quarterly and was aligned to monthly frequency.
* Historical economic relationships may change across different economic eras.
* Observational economic data cannot establish causal relationships.

---

# ♻️ 6. Reproducibility

The project repository contains all data processing scripts, validation scripts, and documentation necessary to reproduce the analysis-ready dataset.

## Environment

* Python 3.12
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib

## Validation Script

```bash
import pandas as pd
from pathlib import Path

# =========================
# 1. Load dataset
# =========================

file_path = Path.home() / "Downloads" / "capstone_capstone_plus_final.csv"

df = pd.read_csv(file_path)

print("\n✅ File loaded successfully")
print(f"File path: {file_path}")

# =========================
# 2. Basic shape checks
# =========================

print("\n==============================")
print("BASIC DATASET INFO")
print("==============================")

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn names:")
for col in df.columns:
    print(f"- {col}")

# =========================
# 3. Date checks
# =========================

print("\n==============================")
print("DATE CHECKS")
print("==============================")

date_col = None

for col in df.columns:
    if col.lower() in ["date", "observation_date", "month"]:
        date_col = col
        break

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    print(f"Date column detected: {date_col}")
    print(f"Start date: {df[date_col].min()}")
    print(f"End date: {df[date_col].max()}")
    print(f"Duplicate dates: {df[date_col].duplicated().sum()}")
    print(f"Missing dates: {df[date_col].isna().sum()}")

    expected_months = pd.date_range(
        start=df[date_col].min(),
        end=df[date_col].max(),
        freq="MS"
    )

    actual_months = pd.to_datetime(df[date_col]).dt.to_period("M").dt.to_timestamp()
    missing_months = sorted(set(expected_months) - set(actual_months))

    print(f"Expected monthly periods: {len(expected_months)}")
    print(f"Missing monthly periods: {len(missing_months)}")

    if missing_months:
        print("Missing months:")
        for m in missing_months[:20]:
            print(m.strftime("%Y-%m"))
else:
    print("⚠️ No date column detected")

# =========================
# 4. Duplicate checks
# =========================

print("\n==============================")
print("DUPLICATE CHECKS")
print("==============================")

print(f"Duplicate rows: {df.duplicated().sum()}")

# =========================
# 5. Missing value checks
# =========================

print("\n==============================")
print("MISSING VALUE CHECKS")
print("==============================")

missing = df.isna().sum()
missing = missing[missing > 0]

if missing.empty:
    print("✅ No missing values found")
else:
    print("Columns with missing values:")
    print(missing)

# =========================
# 6. Infinite value checks
# =========================

print("\n==============================")
print("INFINITE VALUE CHECKS")
print("==============================")

numeric_df = df.select_dtypes(include="number")

inf_count = numeric_df.apply(lambda x: x.isin([float("inf"), float("-inf")]).sum())
inf_count = inf_count[inf_count > 0]

if inf_count.empty:
    print("✅ No infinite values found")
else:
    print("Columns with infinite values:")
    print(inf_count)

# =========================
# 7. Required source variable checks
# =========================

print("\n==============================")
print("REQUIRED SOURCE VARIABLE CHECKS")
print("==============================")

required_keywords = [
    "Unemployment",
    "Inflation",
    "FederalFunds",
    "GDP",
    "ConsumerSentiment",
    "Recession"
]

for keyword in required_keywords:
    matches = [col for col in df.columns if keyword.lower() in col.lower()]
    if matches:
        print(f"✅ {keyword}: {matches}")
    else:
        print(f"❌ {keyword}: NOT FOUND")

# =========================
# 8. Forecast target checks
# =========================

print("\n==============================")
print("FORECAST TARGET CHECKS")
print("==============================")

forecast_targets = [
    "FutureUnemployment_3M",
    "FutureUnemployment_6M",
    "FutureUnemployment_12M"
]

for target in forecast_targets:
    if target in df.columns:
        print(f"✅ {target} found | Missing values: {df[target].isna().sum()}")
    else:
        print(f"❌ {target} missing")

# =========================
# 9. Engineered feature checks
# =========================

print("\n==============================")
print("ENGINEERED FEATURE CHECKS")
print("==============================")

engineered_keywords = [
    "Lag",
    "Growth",
    "Momentum",
    "Change",
    "Shock",
    "Stress",
    "Pressure",
    "Risk",
    "Acceleration",
    "Deterioration",
    "RealInterest"
]

engineered_cols = []

for col in df.columns:
    if any(keyword.lower() in col.lower() for keyword in engineered_keywords):
        engineered_cols.append(col)

print(f"Detected engineered features: {len(engineered_cols)}")

for col in engineered_cols:
    print(f"- {col}")

# =========================
# 10. Numeric summary
# =========================

print("\n==============================")
print("NUMERIC SUMMARY")
print("==============================")

print(numeric_df.describe().T)

# =========================
# 11. Proposal consistency check
# =========================

print("\n==============================")
print("PROPOSAL CONSISTENCY CHECK")
print("==============================")

expected_rows = 838
expected_cols = 40

if df.shape[0] == expected_rows:
    print(f"✅ Row count matches proposal: {expected_rows}")
else:
    print(f"⚠️ Row count mismatch: expected {expected_rows}, found {df.shape[0]}")

if df.shape[1] == expected_cols:
    print(f"✅ Column count matches proposal: {expected_cols}")
else:
    print(f"⚠️ Column count mismatch: expected {expected_cols}, found {df.shape[1]}")

print("\n✅ Dataset validation checks completed")
```

Successful execution confirms:

* 838 rows
* 40 columns
* 0 duplicate rows
* 0 duplicate dates
* 0 infinite values
* 0 missing predictor values

The dataset can be regenerated from documented source files without additional manual intervention.

---

# ⚖️ 7. Ethics and Access Controls

## Privacy and Data Handling

✅ No personally identifiable information (PII)

✅ No protected health information (PHI)

✅ No individual-level records

✅ No sensitive personal data

## Access Controls

All datasets originate from publicly available economic data sources and do not require authentication, restricted access agreements, or special permissions.

## Responsible Use

Forecasting results will be interpreted as statistical estimates rather than guarantees of future economic outcomes. Findings will be presented as predictive relationships and correlations rather than causal claims. All data sources, transformations, and assumptions are documented to support transparency and reproducibility.

---

# ❄️ 8. Freeze Statement

The project data scope is now frozen.

All datasets required to answer the approved research questions have been collected, integrated, validated, and documented. No additional data ingestion work is planned for the remainder of the project.

The final analysis-ready dataset contains:

* 838 observations
* 40 variables
* 27 engineered features
* 3 unemployment forecasting targets
* 1 labor market shock forecasting target

Future project work will focus on:

* Exploratory Data Analysis (EDA)
* Statistical Analysis
* Forecast Modeling
* Model Evaluation
* Dashboard Development
* Visualization
* Final Report and Poster Preparation

### Final Dataset Status

✅ Data acquisition complete

✅ Data integration complete

✅ Feature engineering complete

✅ Data quality validation complete

✅ Dataset frozen for analysis

**Final Dataset:** `capstone_capstone_plus_final.csv`
