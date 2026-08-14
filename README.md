# 📊 Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

> **DATA 510 – Session 2**  
> **Willamette University | Summer 2026**  
> **Author and Product Lead: Manish R. Kallu**

[🌐 Live Project Portfolio](https://manishkallu01-wq.github.io/capstone.html) · [📁 Project Deliverables](deliverables/) · [🗂️ Project Board](https://github.com/users/manishkallu01-wq/projects/1)

---

## Project Overview

This capstone examines how well public macroeconomic indicators forecast U.S. unemployment three, six, and twelve months ahead. It also studies their historical lead-lag relationships with unemployment without treating correlation as causation.

The monthly dataset covers April 1956 through December 2025. The workflow includes source validation, temporal alignment, feature engineering, chronological model evaluation, and a separate correlation analysis.

| Project element | Final specification |
| --- | --- |
| 📅 Study period | April 1956–December 2025 |
| 🗓️ Time frequency | Monthly |
| 📊 Final dataset | 837 observations × 40 columns |
| 🧠 Predictors | 35 |
| 🏛️ Public series | 6 |
| 🔭 Forecast horizons | 3, 6, and 12 months |
| 🤖 Selected models | Ridge Regression and Extra Trees |
| ✅ Validation design | Chronological train/validation/test split with horizon embargo |
| 📏 Evaluation metrics | MAE, RMSE, and R² |
| 🎯 Best result | 3-month Ridge Regression, R² = 0.720 |

Forecast performance is strongest at three months and declines at longer horizons.

---

## 👥 Project Team and Stakeholders

| Role | Name | Project involvement |
| --- | --- | --- |
| 👨‍💻 Owner, Author, and Product Lead | **Manish R. Kallu** | Led the data engineering, analysis, modeling, interpretation, and final communication |
| 🎓 Instructor and Project Sponsor | **Lucas P. Cordova, Ph.D.** | Provided course direction, milestone expectations, and academic oversight |
| 🤝 Peer Stakeholder / Product Owner | **Brandon Smith** | Reviewed project clarity, stakeholder relevance, and communication of practical value |
| 🤝 Peer Stakeholder / Product Owner | **Jon Garrow** | Reviewed research-question framing and clarity of project communication |
| 🤝 Peer Stakeholder / Product Owner | **Jackson Garro** | Participated in the peer stakeholder review process and iterative studio feedback |

Peer feedback was used to improve the framing of the research questions, make the stakeholder value more explicit, clarify the distinction between forecasting and causal explanation, and strengthen the presentation of results and limitations.

### Intended Stakeholders

The project is relevant to:

- 🏛️ **Policymakers and public agencies** monitoring signs of labor-market stress
- 📈 **Economists and researchers** studying lead-lag relationships across economic cycles
- 🏢 **Businesses and workforce planners** preparing for changes in hiring demand
- 💼 **Investors and risk teams** evaluating broader economic conditions
- 👷 **Workforce-development organizations** anticipating changes in unemployment conditions
- 🎓 **Students and practitioners** seeking a reproducible applied macroeconomic forecasting example

---

## ❓ Research Questions

### Primary Research Question

> Can future U.S. unemployment be forecast three, six, and twelve months ahead using publicly available macroeconomic indicators?

### Secondary Research Question

> Which macroeconomic indicators show the strongest and most consistent historical relationship with unemployment across economic environments and business cycles?

The questions address two distinct objectives:

1. **Forecasting:** measuring out-of-sample predictive performance at multiple future horizons.
2. **Historical interpretation:** identifying indicators with strong lead-lag relationships while avoiding unsupported causal claims.

---

## 🗃️ Data Sources

Six public macroeconomic series were integrated into one monthly analytical dataset.

| Series | Measure | Source organization | Project role |
| --- | --- | --- | --- |
| **UNRATE** | U.S. unemployment rate | Bureau of Labor Statistics via FRED | Outcome, baseline signal, and labor-market context |
| **CPIAUCSL** | Consumer Price Index | Bureau of Labor Statistics via FRED | Inflation conditions |
| **FEDFUNDS** | Effective federal funds rate | Federal Reserve via FRED | Monetary-policy conditions |
| **GDP** | Gross Domestic Product, current dollars | Bureau of Economic Analysis via FRED | Economic growth |
| **UMCSENT** | Consumer sentiment | University of Michigan via FRED | Household expectations and confidence |
| **USREC** | U.S. recession indicator | NBER via FRED | Economic-cycle context |

### Data Scope

- **Final date range:** April 1956–December 2025
- **Final analytical observations:** 837 monthly rows
- **Final columns:** 40
- **Predictors used in the modeling framework:** 35
- **Geographic scope:** United States
- **Unit of analysis:** Month

All source organizations retain ownership of their respective data. This repository uses the data for educational and academic analysis.

---

## 🏗️ Data Engineering Pipeline

The project follows a structured, reproducible pipeline:

1. 📥 **Acquire source data**  
   Download the six approved public macroeconomic series.

2. 🔍 **Validate each source**  
   Check date types, coverage, duplicates, missing values, invalid values, and frequency.

3. 🗓️ **Standardize temporal frequency**  
   Carry each quarterly GDP value across the three months of its quarter so it can be aligned with the monthly series.

4. 🔗 **Merge on the monthly date key**  
   Integrate all six sources into a unified time-indexed dataset.

5. 🧹 **Handle valid mid-series gaps**  
   Apply controlled interpolation only where appropriate; do not backfill observations before a series was first published.

6. 🛠️ **Engineer forecasting features**  
   Create lagged, momentum, acceleration, ratio, and composite economic indicators.

7. 🎯 **Create future targets**  
   Generate unemployment outcomes for the 3-, 6-, and 12-month forecast horizons.

8. ⏳ **Split chronologically**  
   Preserve temporal order so models are evaluated only on future observations not seen during training.

9. 🤖 **Train and compare models**  
   Evaluate candidate approaches at each forecast horizon.

10. 📊 **Interpret and communicate results**  
    Compare metrics, analyze historical relationships, document limitations, and present results through the report, poster, repository, and portfolio.

---

## 🧠 Feature Engineering

The engineered features were designed to capture changes in economic direction, policy conditions, stress, and cross-indicator relationships.

### Future Targets

- `FutureUnemployment_3M`
- `FutureUnemployment_6M`
- `FutureUnemployment_12M`

### Lagged Signals

- `FederalFundsLag6`
- `GDPGrowthLag6`
- `ConsumerSentimentLag6`

### Momentum and Acceleration

- `UnemploymentMomentum`
- `GDPGrowthMomentum`
- `InflationAcceleration`
- `ConsumerConfidenceDeterioration`

### Ratios and Composite Indicators

- `GrowthToInflationRatio`
- `InflationUnemploymentRatio`
- `MonetaryTighteningIndex`
- `EconomicStressIndex`
- `RecessionRiskScore`
- `LaborMarketShock`

These engineered variables help represent economic dynamics that may not be visible from contemporaneous raw values alone. Features containing unemployment-derived information are interpreted carefully because they can strengthen prediction while limiting claims about fully external early-warning power.

---

## 🔬 Modeling and Validation

### Candidate Modeling Strategy

The analysis compared linear and tree-based approaches across the three forecast horizons.

For each horizon, the model with the lowest validation RMSE—using validation MAE as a tiebreaker—was selected, refitted on the full pre-test period, and evaluated once on the untouched test set. The selected model was retained even when another algorithm later achieved a lower test RMSE.

The final selected models were:

- 📈 **Ridge Regression** for the 3-month horizon
- 🌲 **Extra Trees** for the 6-month horizon
- 🌲 **Extra Trees** for the 12-month horizon

### Why a Chronological Split?

A random split would allow observations from later years to influence training for earlier years, creating unrealistic leakage in a time-series forecasting setting. The project therefore uses a **chronological train/validation/test design**. Validation begins in January 1989, testing begins in January 1999, and an embargo equal to each forecast horizon prevents development labels from extending into the next split.

### Evaluation Metrics

| Metric | Meaning |
| --- | --- |
| **MAE** | Average absolute forecast error in unemployment-rate percentage points |
| **RMSE** | Error measure that gives greater weight to larger misses |
| **R²** | Proportion of variation explained in the held-out period |

---

## 🏆 Final Forecasting Results

| Forecast horizon | Selected model | MAE | RMSE | R² |
| --- | --- | ---: | ---: | ---: |
| **3 months** | **Ridge Regression** | **0.349** | **1.020** | **0.720** |
| **6 months** | **Extra Trees** | **0.725** | **1.277** | **0.563** |
| **12 months** | **Extra Trees** | **1.195** | **1.729** | **0.205** |

### Result Interpretation

- 🥇 **Three months:** strongest and most practically useful forecasting horizon.
- 📉 **Six months:** moderate predictive value, but larger errors and lower explained variation.
- 🔭 **Twelve months:** limited incremental value; only 0.6% better than persistence and 0.9% worse than the unemployment-only baseline, so it should be treated as a broad scenario rather than a reliable one-year prediction.
- ⚠️ **Overall:** forecast uncertainty grows with the horizon, so results should be treated as directional early-warning evidence rather than exact future unemployment estimates.

The 3-month Ridge Regression result—**MAE 0.349 and R² 0.720**—shows that the combined macroeconomic feature set can provide useful near-term information while retaining a relatively interpretable model structure.

---

## 🔎 Historical Indicator Findings

For the secondary research question, consumer sentiment produced the strongest overall historical external relationship with future unemployment.

> **Consumer sentiment reached r = −0.496 at the 12-month horizon.**

The negative relationship is economically intuitive: weaker consumer confidence often accompanies expectations of slower activity and can precede worsening labor-market conditions. However:

- the strength of the relationship varies across economic regimes;
- correlation does not establish causation;
- revised historical data do not reproduce the information available at each original forecast date; and
- recession periods and structural breaks can change relationships between variables.

Recession status ranked second. Consumer sentiment was strongly negative at a six-month lead before 2020 but reversed to **+0.67 during 2020–2025**, so the final period is interpreted cautiously as possible regime instability rather than a permanent structural change.

The project therefore presents these findings as **historical associations**, not causal estimates.

---

## 💡 Key Conclusions

1. Public macroeconomic data support useful three-month forecasts and moderately informative six-month forecasts, but not a reliable twelve-month prediction.
2. The 3-month horizon provides the strongest balance of accuracy and practical usefulness.
3. Forecast quality weakens meaningfully at 6 and 12 months.
4. Consumer sentiment is the strongest overall historical external indicator in the lead-lag analysis.
5. Economic relationships are regime-dependent and should not be assumed to remain constant.
6. Model outputs should complement—not replace—expert economic judgment.
7. Interpretability, temporal validation, and transparent limitations are essential for responsible use.

---

## ⚠️ Limitations

- **Retrospective recession labels:** NBER recession dates are not available as real-time signals when recessions begin.
- **Unemployment-derived composite features:** some engineered indicators incorporate unemployment information and must not be described as purely external predictors.
- **Structural breaks:** COVID-19 and other major disruptions can change relationships learned from historical data.
- **National aggregation:** U.S.-level values can conceal state, industry, demographic, and regional differences.
- **Data revisions:** current historical values may differ from the data vintages available at the original forecast date.
- **Single chronological split:** results depend on one held-out period and may vary under rolling-origin validation.
- **No formal prediction intervals:** point metrics do not fully express forecast uncertainty.
- **Association versus causation:** correlations and model importance do not prove causal effects.
- **Serial dependence:** monthly observations are related over time and are not fully independent.
- **Limited indicator set:** the analysis uses six approved public series and does not cover every possible labor-market driver.

### Future Work

Future extensions could:

- add state-, industry-, and demographic-level labor-market data;
- introduce additional leading indicators and real-time data vintages;
- evaluate rolling and expanding-window validation;
- construct formal forecast intervals;
- test dedicated time-series and deep-learning methods;
- study alternative forecast horizons; and
- monitor performance across changing economic regimes.

---

## 🛡️ Responsible Use

This project is an educational decision-support demonstration. Its forecasts should not be used alone for employment, investment, public-policy, lending, or other high-stakes decisions.

Responsible use requires:

- reviewing the forecast horizon and error metrics;
- accounting for uncertainty and structural change;
- separating predictive associations from causal conclusions;
- combining outputs with domain expertise and current economic information; and
- revalidating models before applying them to a new period or decision context.

---

## 📦 Repository Structure

| Path | Purpose |
| --- | --- |
| [`data/`](data/) | Read-only raw source files and the submitted processed dataset |
| [`src/`](src/) | Optional dataset reconstruction, feature-engineering, and validation scripts |
| [`notebooks/`](notebooks/) | Notebook guidance; no notebook is required for the submitted final workflow |
| [`deliverables/M5-final/`](deliverables/M5-final/) | Final machine-learning and correlation scripts, results, figures, report, and poster |
| [`deliverables/`](deliverables/) | All milestone submissions |
| [`studio/`](studio/) | Studio briefs, critiques, and stakeholder-feedback artifacts |
| [`BACKLOG.md`](BACKLOG.md) | Human-readable project backlog |
| [`CHARTER.md`](CHARTER.md) | Project charter and governance |

---

## 🔁 Reproducing the Analysis

### 1. Clone the Repository

```bash
git clone https://github.com/manishkallu01-wq/DATA510-Session-2.git
cd DATA510-Session-2
```

### 2. Create a Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

### 3. Install the Core Packages

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn scipy openpyxl joblib
```

### 4. Choose the Appropriate Workflow

Dataset construction and statistical analysis are separate stages in this repository.

#### A. Reconstruct and validate a local dataset from the raw files — optional

Use this path only when rebuilding the dataset from the six source CSV files in [`data/raw/`](data/raw/):

```bash
python src/rebuild.py
python src/eng_variables.py
python src/checks.py
```

The stages are deliberately separate:

1. [`src/rebuild.py`](src/rebuild.py) reads the six repository CSVs, aligns and merges them, and exports `~/Downloads/super_dataset.csv`.
2. [`src/eng_variables.py`](src/eng_variables.py) reads that local super dataset, engineers the submitted feature schema, and exports `~/Downloads/capstone_plus_final.xlsx`.
3. [`src/checks.py`](src/checks.py) reads the local engineered workbook and checks its shape, schema, date sequence, duplicates, infinite values, predictor completeness, and intentional missing future targets.

These scripts are for dataset construction and validation. They are not the machine-learning or correlation-analysis scripts.

The raw repository files are only read. Generated datasets are saved to the user's local `Downloads` folder, not to the repository. The scripts do not commit, push, or otherwise write to GitHub, and no GitHub write access is required. Use `--raw-dir`, `--input`, or `--output` only when a different local path is needed.

#### B. Use the final processed dataset directly

Dataset reconstruction is not required for most users. For modeling, correlation analysis, or review of the submitted work, read or download [`data/processed/capstone_plus_final.xlsx`](data/processed/capstone_plus_final.xlsx) directly. This submitted 837-row × 40-column workbook is the common analysis-ready input used for both research questions.

#### C. Run the final analyses

The Python scripts for the machine-learning workflow and the separate Research Question 2 correlation analysis are available in [`deliverables/M5-final/`](deliverables/M5-final/). They read the submitted `capstone_plus_final.xlsx` through its public, read-only GitHub URL and are separate from the optional dataset-construction scripts in `src/`.

Generated model results, correlation tables, and figures are stored alongside the final analysis materials in [`deliverables/M5-final/`](deliverables/M5-final/).

Random seeds are fixed where supported by the estimators. The chronological evaluation design must be retained to avoid training on future observations.

---

## 📚 Final Deliverables

The completed project includes:

- ✅ Integrated monthly macroeconomic dataset
- ✅ Feature-engineered analytical dataset
- ✅ Data validation and preparation workflow
- ✅ Exploratory and lead-lag relationship analysis
- ✅ 3-, 6-, and 12-month unemployment forecasting models
- ✅ Model comparison using MAE, RMSE, and R²
- ✅ Feature and indicator interpretation
- ✅ Limitations, ethics, and responsible-use documentation
- ✅ Final research report
- ✅ Final poster presentation
- ✅ Live project portfolio
- ✅ Reproducible source code and repository documentation

The [final report](deliverables/M5-final/M5-Final-Report.pdf), [final poster](deliverables/M5-final/M5%20poster%20Final.pdf), milestone materials, and supporting artifacts are available in [`deliverables/`](deliverables/) and through the [live portfolio](https://manishkallu01-wq.github.io/capstone.html).

---

## 🗓️ Milestone Completion Summary

| Milestone | Focus | Final status |
| --- | --- | --- |
| **M1 – Proposal** | Scope, motivation, literature, research questions, and plan | ✅ Complete |
| **M2 – Data Summary** | Source integration, validation, EDA, and dataset documentation | ✅ Complete |
| **M3 – Poster Draft** | Visual communication of methods and preliminary findings | ✅ Complete |
| **M4 – Write-up Draft** | Full methods, results, discussion, and limitations | ✅ Complete |
| **M5 – Final Portfolio** | Final report, poster, repository, and public portfolio | ✅ Complete |

Studio critiques and peer reviews informed the milestone revisions. Reusable templates remain in the studio directory and are clearly identified as templates.

---

## 🧰 Technology Stack

- 🐍 **Programming:** Python
- 🐼 **Data processing:** Pandas and NumPy
- 🤖 **Machine learning:** Scikit-learn and XGBoost
- 📊 **Visualization:** Matplotlib and Seaborn
- 📂 **Version control:** Git and GitHub
- 📝 **Communication:** Research report, poster, README, and public portfolio

---

## 📬 Project Links

- 🌐 **Portfolio:** [manishkallu01-wq.github.io](https://manishkallu01-wq.github.io/)
- 💻 **Repository:** [DATA510-Session-2](https://github.com/manishkallu01-wq/DATA510-Session-2)
- 📁 **Deliverables:** [Final project artifacts](deliverables/)
- 🗂️ **Project Board:** [DATA 510 project board](https://github.com/users/manishkallu01-wq/projects/1)
- 🔗 **LinkedIn:** [Manish Kallu](https://www.linkedin.com/in/manish-kallu-583b61421/)
