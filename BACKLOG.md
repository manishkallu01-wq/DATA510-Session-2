# 🗂️ Final Backlog: Forecasting and Explaining U.S. Unemployment



## 📋 Conventions

- Workflow: `Backlog` → `Create` → `Observe` → `Analyze` → `Done`
- Final status: ✅ Done
- Sizes: S, M, L, or XL
- Milestones: `M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, and `ethics`
- Definitions of Ready and Done: [`CHARTER.md`](CHARTER.md)
- GitHub board: [DATA 510 project board](https://github.com/users/manishkallu01-wq/projects/1)

---

## ✅ Completion Summary

| PBI | Original GitHub issue title | Milestone | Size | Status |
| --- | --- | --- | --- | --- |
| [001](#pbi-001) | Acquire and validate FRED unemployment datasets | M1 | M | ✅ Done |
| [002](#pbi-002) | Acquire and integrate BLS labor market datasets | M1 | L | ✅ Done |
| [003](#pbi-003) | Finalize project research questions and proposal framing | M1 | S | ✅ Done |
| [004](#pbi-004) | Build unified economic indicators dataset | M2 | L | ✅ Done |
| [005](#pbi-005) | Perform exploratory data analysis on unemployment trends | M2 | M | ✅ Done |
| [006](#pbi-006) | Develop baseline unemployment forecasting models | M3 | L | ✅ Done |
| [007](#pbi-007) | Create interactive unemployment trend dashboards | M3 | M | ✅ Done |
| [008](#pbi-008) | Evaluate ethics and bias risks in forecasting outputs | Ethics | S | ✅ Done |
| [009](#pbi-009) | Draft final project methodology and analytical write-up | M4 | L | ✅ Done |
| [010](#pbi-010) | Finalize poster and presentation deliverables | M5 | L | ✅ Done |

---

## PBI-001

**Title:** Acquire and validate FRED unemployment datasets
**GitHub issue:** [#1](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/1)
**Tag / size / status:** `M1-proposal` / M / ✅ Done

- **Create:** Acquired the approved FRED-hosted source files, beginning with the U.S. unemployment rate.
- **Observe:** Checked schema, date parsing, coverage, duplicates, missing values, and numeric validity.
- **Analyze:** Confirmed that the unemployment series provided sufficient monthly history for the approved forecast horizons.
- **Final evidence:** `UNRATE.csv` and the other approved source files are available in [`data/raw/`](data/raw/).

## PBI-002

**Title:** Acquire and integrate BLS labor market datasets
**GitHub issue:** [#2](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/2)
**Tag / size / status:** `M1-proposal` / L / ✅ Done

- **Create:** Evaluated labor-market and macroeconomic inputs available through BLS, FRED, BEA, the Federal Reserve, the University of Michigan, and NBER.
- **Observe:** Compared coverage, frequency, relevance, and compatibility with the monthly unemployment outcome.
- **Analyze:** Refined the initial acquisition concept into the approved six-series scope: `UNRATE`, `CPIAUCSL`, `FEDFUNDS`, `GDP`, `UMCSENT`, and `USREC`.
- **Final disposition:** No additional BLS labor-market series were added beyond the approved project scope.

## PBI-003

**Title:** Finalize project research questions and proposal framing
**GitHub issue:** [#3](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/3)
**Tag / size / status:** `M1-proposal` / S / ✅ Done

- **Create:** Finalized separate forecasting and historical-relationship research questions.
- **Observe:** Reviewed instructor and peer stakeholder feedback on scope, usefulness, and interpretation.
- **Analyze:** Clarified that Research Question 1 evaluates out-of-sample forecasts, while Research Question 2 evaluates historical associations rather than causal effects.
- **Final evidence:** The final framing appears in the [project report](deliverables/M5-final/M5-Final-Report.pdf), [README](README.md), and [portfolio](https://manishkallu01-wq.github.io/capstone.html).

## PBI-004

**Title:** Build unified economic indicators dataset
**GitHub issue:** [#4](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/4)
**Tag / size / status:** `M2-data-summary` / L / ✅ Done

- **Create:** Standardized the date key, aligned quarterly GDP to monthly frequency, merged the six approved series, engineered forecasting features, and created future unemployment targets.
- **Observe:** Checked the date sequence, coverage, duplicates, missing values, infinite values, feature schema, and intentional end-of-series target gaps.
- **Analyze:** Confirmed a final analysis-ready dataset covering April 1956 through December 2025.
- **Final evidence:** [`data/processed/capstone_plus_final.xlsx`](data/processed/capstone_plus_final.xlsx) contains 837 monthly observations, 40 columns, and 35 predictors.

The optional scripts in [`src/`](src/) reconstruct the dataset locally. They read repository raw files and export `super_dataset.csv` and `capstone_plus_final.xlsx` to the user's local `Downloads` folder. They do not upload, commit, or push generated datasets to GitHub.

## PBI-005

**Title:** Perform exploratory data analysis on unemployment trends
**GitHub issue:** [#5](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/5)
**Tag / size / status:** `M2-data-summary` / M / ✅ Done

- **Create:** Produced summary statistics, unemployment trends, economic-cycle comparisons, lead-lag profiles, and correlation visualizations.
- **Observe:** Identified crisis-period errors, regime changes, and differences in indicator direction and strength across horizons.
- **Analyze:** Established the historical context used to interpret both forecasting performance and Research Question 2.
- **Final evidence:** Tables and figures are available in [`deliverables/M5-final/analysis-results/`](deliverables/M5-final/analysis-results/) and [`deliverables/M5-final/Plots/`](deliverables/M5-final/Plots/).

## PBI-006

**Title:** Develop baseline unemployment forecasting models
**GitHub issue:** [#6](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/6)
**Tag / size / status:** `M3-poster-draft` / L / ✅ Done

- **Create:** Evaluated Linear Regression, Ridge Regression, Random Forest, Extra Trees, Gradient Boosting, and XGBoost at 3-, 6-, and 12-month horizons, alongside persistence and unemployment-only baselines.
- **Observe:** Compared validation and test MAE, RMSE, and R² under a chronological train/validation/test split with a horizon-specific embargo.
- **Analyze:** Selected each model using the lowest validation RMSE, with validation MAE as the tiebreaker, before evaluating the untouched test set.

| Horizon | Selected model | Test MAE | Test RMSE | Test R² |
| --- | --- | ---: | ---: | ---: |
| 3 months | Ridge Regression | 0.349 | 1.020 | 0.720 |
| 6 months | Extra Trees | 0.725 | 1.277 | 0.563 |
| 12 months | Extra Trees | 1.195 | 1.729 | 0.205 |

The 3-month model is the strongest result, the 6-month model retains moderate value, and the 12-month model is suitable only for broad scenario-level interpretation.

## PBI-007

**Title:** Create interactive unemployment trend dashboards
**GitHub issue:** [#7](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/7)
**Tag / size / status:** `M3-poster-draft` / M / ✅ Done

- **Create:** Developed stakeholder-facing unemployment, model-comparison, prediction, feature-importance, and correlation visuals.
- **Observe:** Reviewed legibility, technical accuracy, narrative fit, and stakeholder usefulness.
- **Analyze:** Prioritized a polished public portfolio, final poster, and reproducible static analytical figures over an unsupported standalone dashboard claim.
- **Final evidence:** [Public capstone portfolio](https://manishkallu01-wq.github.io/capstone.html), [final poster](deliverables/M5-final/M5%20poster%20Final.pdf), and [final plots](deliverables/M5-final/Plots/).

## PBI-008

**Title:** Evaluate ethics and bias risks in forecasting outputs
**GitHub issue:** [#8](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/8)
**Tag / size / status:** `ethics` / S / ✅ Done

- **Create:** Documented responsible-use boundaries, forecast uncertainty, retrospective recession labels, unemployment-derived features, revisions, aggregation, structural breaks, and associational interpretation.
- **Observe:** Assessed how national forecasts or historical relationships could be overstated or misapplied.
- **Analyze:** Required explicit separation of forecasting from causation and prohibited high-stakes use without current evidence, domain expertise, and revalidation.
- **Final evidence:** Ethics and limitations are documented in the final report, [README](README.md), [Charter](CHARTER.md), and portfolio.

## PBI-009

**Title:** Draft final project methodology and analytical write-up
**GitHub issue:** [#9](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/9)
**Tag / size / status:** `M4-writeup-draft` / L / ✅ Done

- **Create:** Drafted the problem statement, data pipeline, feature engineering, validation design, modeling, correlation analysis, results, limitations, recommendations, and reproducibility sections.
- **Observe:** Reconciled narrative claims with generated result tables and stakeholder feedback.
- **Analyze:** Revised the write-up to retain validation-selected models, report weak 12-month performance transparently, and distinguish historical association from causation.
- **Final evidence:** [M4 materials](deliverables/M4-writeup-draft/) and the [final M5 report](deliverables/M5-final/M5-Final-Report.pdf).

## PBI-010

**Title:** Finalize poster and presentation deliverables
**GitHub issue:** [#10](https://github.com/manishkallu01-wq/DATA510-Session-2/issues/10)
**Tag / size / status:** `M5-final` / L / ✅ Done

- **Create:** Finalized the report, poster, supporting figures, analytical scripts, result files, repository documentation, and public portfolio.
- **Observe:** Crosschecked artifact names, links, metrics, model-selection wording, RQ2 findings, limitations, and reproducibility instructions.
- **Analyze:** Consolidated the final message: useful 3-month forecasting, moderate 6-month value, limited 12-month reliability, and consumer sentiment as the strongest overall historical external relationship.
- **Final evidence:** [`deliverables/M5-final/`](deliverables/M5-final/) and the [public portfolio](https://manishkallu01-wq.github.io/capstone.html).

## 🏁 Backlog Status

**All ten PBIs are complete and their GitHub issues are closed.** No unfinished work is represented as part of the submitted project.
