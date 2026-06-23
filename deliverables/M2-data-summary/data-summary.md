# 📊 Milestone 2: Data Summary

## Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

**Author:** Manish R Kallu

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
| Engineered Features | 29                                 |
| Forecast Targets    | 4                                  |

---

# 🏗️ 3. Schema and Organization

## Repository Data Layout

```text
DATA510-Session-2/
│
├── data/
│   ├── raw/
│   │   ├── unemployment.csv
│   │   ├── inflation.csv
│   │   ├── federal_funds.csv
│   │   ├── gdp.csv
│   │   ├── consumer_sentiment.csv
│   │   └── recession.csv
│   │
│   ├── processed/
│   │   └── capstone_capstone_plus_final.csv
│   │
│   ├── README.md
│   └── SCHEMA.md
│
├── deliverables/
│   └── M2-data-summary/
│       ├── data-summary.md
│       ├── rebuild.py
│       └── eng_variables.py
│
├── notebooks/
├── src/
├── CHARTER.md
├── BACKLOG.md
└── README.md
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

Data ingestion and dataset construction have been completed.

### Workflow Summary

1. Retrieved six approved economic datasets from FRED.
2. Standardized timestamps and variable names.
3. Converted GDP observations into a monthly analytical framework.
4. Merged all datasets using the `Date` field.
5. Generated engineered features using `eng_variables.py`.
6. Constructed forecasting targets and composite indicators.
7. Rebuilt and validated the final analytical dataset using `rebuild.py`.
8. Verified dataset quality through automated validation checks.

### Repository Artifacts

| File | Purpose |
|--------|---------|
| `deliverables/M2-data-summary/rebuild.py` | Rebuilds the final analytical dataset |
| `deliverables/M2-data-summary/eng_variables.py` | Creates engineered variables and forecasting targets |
| `data/processed/capstone_capstone_plus_final.csv` | Final analysis-ready dataset |

### Pipeline Status

✅ Data acquisition complete

✅ Data integration complete

✅ Feature engineering complete

✅ Dataset rebuild process documented

✅ Validation complete

✅ Analysis-ready dataset generated

No additional ingestion work is required. The final dataset contains all variables necessary to answer the approved research questions.

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

The repository contains scripts required to reconstruct the final analysis-ready dataset.

### Environment

- Python 3.12
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib

### Rebuild Workflow

```bash
python deliverables/M2-data-summary/rebuild.py
```

### Validation Script

```bash
python deliverables/M2-data-summary/checks.py
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
