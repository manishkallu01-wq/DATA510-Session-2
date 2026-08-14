# 📊 Milestone 2: Data Summary

## Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

**Author:** Manish R. Kallu

**Studio Session:** 2

**Milestone status:** ✅ Complete

**M2 analysis-ready dataset:** `data/processed/capstone_plus_final.xlsx`

---

## 🎯 1. Research Questions

### Primary Research Question

> Can future U.S. unemployment be forecast three, six, and twelve months ahead using publicly available macroeconomic indicators?

### Secondary Research Question

> Which external macroeconomic indicators show the strongest and most consistent historical relationships with unemployment across forecast horizons and historical periods?

The two questions serve different purposes. Research Question 1 evaluates out-of-sample prediction. Research Question 2 evaluates historical lead-lag associations. Neither correlation nor model importance establishes causation.

Six public macroeconomic series were aligned to a monthly timeline and integrated into the common analysis-ready dataset. The final modeling period covers April 1956 through December 2025.

---

## 📦 2. Data Inventory

### Raw Source Series

| File | Series | Measure | Provider | Native frequency |
| --- | --- | --- | --- | --- |
| [`UNRATE.csv`](../../data/raw/UNRATE.csv) | UNRATE | U.S. unemployment rate | Bureau of Labor Statistics via FRED | Monthly |
| [`CPIAUCSL.csv`](../../data/raw/CPIAUCSL.csv) | CPIAUCSL | Consumer Price Index | Bureau of Labor Statistics via FRED | Monthly |
| [`FEDFUNDS.csv`](../../data/raw/FEDFUNDS.csv) | FEDFUNDS | Effective federal funds rate | Federal Reserve via FRED | Monthly |
| [`GDP.csv`](../../data/raw/GDP.csv) | GDP | Gross Domestic Product, current dollars | Bureau of Economic Analysis via FRED | Quarterly |
| [`UMCSENT.csv`](../../data/raw/UMCSENT.csv) | UMCSENT | Consumer sentiment | University of Michigan via FRED | Monthly |
| [`USREC.csv`](../../data/raw/USREC.csv) | USREC | U.S. recession indicator | NBER via FRED | Monthly |

The source files contain aggregate public economic observations. They contain no individual records, protected attributes, credentials, or personal identifiers. Source organizations retain ownership, and users remain responsible for applicable provider terms and attribution requirements.

### Final Analysis Dataset

| Attribute | Final specification |
| --- | --- |
| File | [`data/processed/capstone_plus_final.xlsx`](../../data/processed/capstone_plus_final.xlsx) |
| Observation period | April 1956-December 2025 |
| Grain | One row per month |
| Rows | 837 |
| Columns | 40 |
| Predictors | 35 |
| Public source series | 6 |
| Primary forecast horizons | 3, 6, and 12 months |
| Primary key | `Date` |

The workbook is the validated processed input prepared at M2 for the project's later analytical work.
It contains 837 rows, 40 columns, and 35 predictors.

---

## 🏗️ 3. Data Organization and Schema

### Repository Layout

```text
data/
├── raw/
│   ├── CPIAUCSL.csv
│   ├── FEDFUNDS.csv
│   ├── GDP.csv
│   ├── UMCSENT.csv
│   ├── UNRATE.csv
│   └── USREC.csv
├── processed/
│   └── capstone_plus_final.xlsx
├── README.md
└── SCHEMA.md

src/
├── rebuild.py
├── eng_variables.py
├── checks.py
└── README.md

deliverables/
└── M2-data-summary/
    ├── data-summary.md
    └── README.md
```

Dataset-construction code is maintained centrally in `src/`; it is not duplicated inside the milestone folder.

### Join and Frequency Strategy

1. Parse and standardize the source dates.
2. Establish a complete monthly date sequence.
3. Carry quarterly GDP values across the corresponding monthly panel.
4. Align the other approved series to the monthly date key.
5. Handle valid mid-series gaps without backfilling observations before a series begins.
6. Merge the six series using `Date` as the one-row-per-month key.
7. Engineer lagged, rate-of-change, momentum, ratio, stress, and future-target variables.
8. Trim to the fully usable April 1956-December 2025 modeling period.

### Core Source Columns

- `UnemploymentRate`
- `ConsumerPriceIndex`
- `FederalFundsRate`
- `GrossDomesticProduct`
- `ConsumerSentiment`
- `RecessionIndicator`

### Predictor Groups

| Group | Examples | Purpose |
| --- | --- | --- |
| Labor persistence | `UnemploymentRate`, `UnemploymentLag1`, `UnemploymentLag3`, `UnemploymentLag6`, `UnemploymentLag12` | Represent persistence and delayed labor-market adjustment |
| Labor change | `UnemploymentChange1M`, `UnemploymentChange3M`, `UnemploymentMomentum` | Capture emerging improvement or deterioration |
| Prices and policy | `InflationRateYoY`, inflation lags, federal-funds-rate lags, `RealInterestRate` | Represent inflation pressure and monetary conditions |
| Output | `GrossDomesticProduct`, `GDPGrowthYoY`, GDP growth lags and momentum | Represent expansion, contraction, and production trends |
| Expectations | `ConsumerSentiment`, sentiment lags, confidence deterioration | Represent household expectations |
| Regime and composites | `RecessionIndicator`, `EconomicStressIndex`, `RecessionRiskScore` | Describe historical regimes and combined stress |

### Forecast Targets

- `FutureUnemployment_3M`
- `FutureUnemployment_6M`
- `FutureUnemployment_12M`
- `FutureLaborMarketShock_6M`

The final 3, 6, and 12 values of the corresponding unemployment targets are intentionally missing because future unemployment is not observable beyond the end of the dataset.

The full column dictionary is documented in [`data/SCHEMA.md`](../../data/SCHEMA.md).

---

## ⚙️ 4. Construction Pipeline

### Supported Current Sequence

The maintained scripts in [`src/`](../../src/) separate reconstruction, engineering, and validation:

1. [`src/rebuild.py`](../../src/rebuild.py) reads the six raw CSVs and creates a local monthly `super_dataset.csv`.
2. [`src/eng_variables.py`](../../src/eng_variables.py) reads that local super dataset and creates a local engineered `capstone_plus_final.xlsx`.
3. [`src/checks.py`](../../src/checks.py) validates the local engineered final workbook.

Run from the repository root:

```bash
python src/rebuild.py
python src/eng_variables.py
python src/checks.py
```

Default local outputs:

| Stage | Output | Expected result |
| --- | --- | --- |
| Reconstruction | `~/Downloads/super_dataset.csv` | 858 rows x 7 columns; July 1954-December 2025 |
| Feature engineering | `~/Downloads/capstone_plus_final.xlsx` | 837 rows x 40 columns; April 1956-December 2025 |
| Validation | Console result | Final dataset checks pass |

Use `--raw-dir`, `--input`, or `--output` only when a different local path is needed.

### Repository Access Boundary

The repository provides read-only source context for public users. Generated reconstruction files default to the user's local `Downloads` folder, not to `data/processed/` or another repository path.

The scripts do not invoke Git, create commits, push branches, or upload generated datasets. No GitHub write access is required.

### Analysis-Ready Dataset Path

Dataset reconstruction is optional. Readers may use the validated [`capstone_plus_final.xlsx`](../../data/processed/capstone_plus_final.xlsx) directly.

---

## 🔍 5. Data Quality Results

| Validation check | Final result |
| --- | ---: |
| Rows | 837 |
| Columns | 40 |
| Predictors | 35 |
| Date range | 1956-04-01 to 2025-12-01 |
| Duplicate dates | 0 |
| Missing monthly periods | 0 |
| Infinite numeric values | 0 |
| Unexpected missing predictor values | 0 |
| Missing `FutureUnemployment_3M` values | 3 |
| Missing `FutureUnemployment_6M` values | 6 |
| Missing `FutureUnemployment_12M` values | 12 |

### Quality Interpretation

- Missing unemployment targets occur only at the end of the series because their future observations do not yet exist.
- Crisis-period extremes were retained because they represent real economic events, not data-entry errors.
- Quarterly GDP was aligned to the monthly panel before feature engineering.
- No random imputation was used to invent observations beyond available series coverage.

---

## ⚠️ 6. Limitations

- **Historical revisions:** current values may differ from the vintages available at an original forecast date.
- **Quarterly GDP:** GDP is carried into a monthly representation and is not a native monthly release.
- **Retrospective recession labels:** NBER dates are historical descriptors and are not available in real time when recessions begin.
- **Unemployment-derived features:** some composites incorporate unemployment information and are not independent external evidence.
- **Structural breaks:** events such as COVID-19 can disrupt relationships learned from earlier periods.
- **National aggregation:** U.S. totals conceal state, industry, demographic, and occupational differences.
- **Association, not causation:** correlations and feature importance do not establish causal effects.
- **Serial dependence:** monthly observations are related over time.

---

## ⚖️ 7. Ethics, Access, and Responsible Use

### Privacy

- ✅ Aggregate public economic data only
- ✅ No personally identifiable information
- ✅ No protected health information
- ✅ No individual employment histories
- ✅ No secrets, credentials, or restricted records

### Responsible Use

Forecasts are statistical estimates, not guarantees. National results must not be represented as individual predictions or used alone for employment, investment, lending, or public-policy decisions.

Research Question 2 is designed to describe historical association rather than causation. Relationship strength and direction must be evaluated across horizons and historical periods during the analytical stage.

---

## ❄️ 8. Final Data Freeze Record

The approved six-series scope is complete and frozen for the submitted analysis.

| Final item | Status |
| --- | --- |
| Raw source inventory | ✅ Complete |
| Monthly integration | ✅ Complete |
| Feature engineering | ✅ Complete |
| Future-target construction | ✅ Complete |
| Quality validation | ✅ Complete |
| Common processed workbook | ✅ Complete |

Changes to input data, feature definitions, date ranges, random seeds, package versions, hyperparameters, or model configurations must be documented as a new analysis version rather than a direct reproduction of submitted results.

The M2 milestone ends with a validated, documented, analysis-ready dataset. Model selection, forecasting results, correlation findings, and final communication artifacts are outside this milestone's scope.
