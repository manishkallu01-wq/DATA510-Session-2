# 📜 Studio Charter: Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

**👨‍💻 Owner, Author, and Product Lead:** Manish R. Kallu

**🤝 Peer Stakeholder / Product Owners:** Brandon Smith, Jon Garrow, and Jackson Garro

**🎓 Instructor and Project Sponsor:** Lucas P. Cordova, Ph.D. (`LucasCordova` on GitHub)

**🧭 Studio Session:** 2

**📅 Studio formation date:** May 25, 2026

**💻 Repository:** [DATA510-Session-2](https://github.com/manishkallu01-wq/DATA510-Session-2)

**🗂️ Project board:** [DATA 510 project board](https://github.com/users/manishkallu01-wq/projects/1)

**🌐 Portfolio:** [Public capstone portfolio](https://manishkallu01-wq.github.io/capstone.html)

**💬 Discord category:** [DATA 510 project workspace](https://discord.com/channels/1277725100816203942/1508588739063054376)

---

## 🌟 Vision

Improve understanding of how public macroeconomic indicators historically relate to U.S. unemployment and assess how much useful forecasting information they provide at three-, six-, and twelve-month horizons.

## 🎯 Mission

Integrate six public U.S. macroeconomic series into a transparent monthly analytical dataset; evaluate multiple forecasting models with chronological validation; analyze historical lead-lag relationships separately from prediction; and communicate the results, uncertainty, limitations, and responsible-use boundaries through reproducible project artifacts.

## 📌 Final Project Scope

| Element | Final specification |
| --- | --- |
| Study period | April 1956-December 2025 |
| Frequency | Monthly |
| Final dataset | 837 observations x 40 columns |
| Predictors | 35 |
| Public source series | 6 |
| Forecast horizons | 3, 6, and 12 months |
| Validation design | Chronological train/validation/test split with horizon embargo |
| Model-selection rule | Lowest validation RMSE; validation MAE as tiebreaker |
| Evaluation metrics | MAE, RMSE, and R² |

### ❓ Research Questions

1. Can future U.S. unemployment be forecast three, six, and twelve months ahead using publicly available macroeconomic indicators?
2. Which external macroeconomic indicators show the strongest and most consistent historical relationships with unemployment across forecast horizons and historical periods?

The first question concerns out-of-sample forecasting. The second concerns historical association. Neither correlation nor model importance is presented as evidence of causation.

---

## 🗃️ Data and Analytical Boundaries

### Approved Source Series

| Series | Measure | Source |
| --- | --- | --- |
| `UNRATE` | U.S. unemployment rate | Bureau of Labor Statistics via FRED |
| `CPIAUCSL` | Consumer Price Index | Bureau of Labor Statistics via FRED |
| `FEDFUNDS` | Effective federal funds rate | Federal Reserve via FRED |
| `GDP` | Gross Domestic Product, current dollars | Bureau of Economic Analysis via FRED |
| `UMCSENT` | Consumer sentiment | University of Michigan via FRED |
| `USREC` | U.S. recession indicator | NBER via FRED |

The final common analysis input is [`data/processed/capstone_plus_final.xlsx`](data/processed/capstone_plus_final.xlsx). It contains 837 monthly rows, 40 columns, and 35 predictors for the submitted modeling framework.

### 🛡️ Responsible-Use Boundaries

- The project uses aggregate public economic data and contains no individual or protected personal records.
- Forecasts are national, not state-, industry-, organization-, or person-level predictions.
- NBER recession dates are retrospective; `RecessionIndicator` and `RecessionRiskScore` are historical descriptors, not real-time signals.
- Revised historical data do not reproduce the information set available at each original forecast date.
- Unemployment-derived features are not independent external early-warning evidence.
- Results are educational decision-support evidence and must not be used alone for high-stakes employment, investment, lending, or public-policy decisions.

---

## 🏆 Final Outcomes

### Forecasting Results

| Horizon | Selected model | Test MAE | Test RMSE | Test R² |
| --- | --- | ---: | ---: | ---: |
| 3 months | Ridge Regression | 0.349 | 1.020 | 0.720 |
| 6 months | Extra Trees | 0.725 | 1.277 | 0.563 |
| 12 months | Extra Trees | 1.195 | 1.729 | 0.205 |

Models were selected using validation results before the untouched test set was inspected. The selected model was retained even when another algorithm later produced a lower test RMSE.

The three-month result is the strongest practical finding. The six-month result retains moderate predictive value. The twelve-month result provides limited incremental value and should be treated as scenario-level evidence rather than a reliable one-year prediction.

### 🔎 Historical-Relationship Results

Consumer sentiment was the strongest overall external historical indicator. Its full-sample Pearson relationship with unemployment strengthened from `r = -0.351` in the same month to `r = -0.496` at twelve months. Recession status ranked second.

The relationships were not stable in every period. At a six-month lead, the consumer-sentiment relationship reversed to `+0.67` during 2020-2025. This short pandemic-and-recovery period is interpreted cautiously as possible regime instability, not a permanent structural change.

---

## ✅ Milestone Completion

| Milestone | Completion evidence | Status |
| --- | --- | --- |
| M1 - Proposal | Research questions, approved scope, initial datasets, and backlog | ✅ Complete |
| M2 - Data Summary | Integrated dataset, validation, exploratory analysis, and feature documentation | ✅ Complete |
| M3 - Poster Draft | Initial visualizations, statistical findings, and baseline results | ✅ Complete |
| M4 - Write-up Draft | Draft methods, results, discussion, and limitations | ✅ Complete |
| M5 - Final Portfolio | Final report, poster, code, results, repository documentation, and public portfolio | ✅ Complete |

---

## 🔁 Reproducibility and Access

Dataset reconstruction and final analysis are separate workflows:

1. The optional scripts in [`src/`](src/) read the six raw repository CSVs and reconstruct the dataset locally.
2. `rebuild.py` exports `super_dataset.csv` to the audience member's local `Downloads` folder.
3. `eng_variables.py` reads that local file and exports `capstone_plus_final.xlsx` locally.
4. `checks.py` validates the locally engineered final workbook.
5. The submitted machine-learning and correlation-analysis scripts are in [`deliverables/M5-final/`](deliverables/M5-final/) and read the public, read-only submitted workbook.

Public users need only read and download repository content. The reconstruction scripts do not commit, push, or upload generated datasets to GitHub, and no GitHub write access is required. Repository commits remain a maintainer responsibility.

---

## 🤝 Working Agreements

### Maintainer Agreements

- Record major analytical decisions, assumptions, and methodology changes.
- Preserve chronological evaluation and the horizon embargo to prevent future-label leakage.
- Keep submitted results traceable to the final analysis scripts and result files.
- Treat changes to data, feature definitions, date ranges, seeds, packages, hyperparameters, or model configurations as a new analysis version.
- Incorporate stakeholder and instructor feedback when it improves clarity, stakeholder value, or analytical rigor.

### Peer-Studio Agreements

- Studio briefs were due by 5 PM on the day before class and were stored in `studio/briefs/`.
- Studio critiques were due by the end of class or within 24 hours when additional review time was needed.
- Feedback was reviewed in good faith and classified as adopted, deferred, or declined.
- Priority conflicts were resolved by reference to project scope, evidence quality, responsible use, and milestone requirements.

### ⏱️ Response Expectations During the Studio

| Signal | Responsible party | Expected response |
| --- | --- | --- |
| Peer PO submits a Studio Brief | Owner | Acknowledge within 24 hours |
| Peer PO submits a Studio Critique | Owner | Respond within 24 hours and record follow-up work when needed |
| Owner posts an iteration review | Peer POs | Review before the next studio session |
| Owner flags a blocker | Instructor and tagged Peer PO | Respond by the next studio session or sooner when urgent |
| A clarifying question is posted | Tagged participant | Reply within 48 hours |

---

## 🚦 Definition of Ready

A product backlog item was ready to move from `Backlog` to `Create` when it had:

- a clear objective or hypothesis;
- a named Create, Observe, and Analyze workflow;
- an appropriate milestone or project tag;
- a reasonable effort estimate; and
- testable acceptance criteria.

## ☑️ Definition of Done

A product backlog item was complete when:

- the required artifact was created and, when appropriate, committed by the maintainer;
- outputs, observations, or findings were documented;
- analytical conclusions and next steps were recorded;
- relevant stakeholder feedback was reviewed; and
- the work was traceable from the applicable milestone or iteration review.

---

## 📦 Deliverables

- Integrated and feature-engineered analytical dataset
- Dataset reconstruction and validation scripts
- Machine-learning and separate RQ2 correlation-analysis scripts
- Model comparisons, predictions, correlation tables, and figures
- Final research report and poster
- Limitations, ethics, and responsible-use documentation
- Public portfolio and repository documentation

Final submitted artifacts are available in [`deliverables/M5-final/`](deliverables/M5-final/) and through the [public portfolio](https://manishkallu01-wq.github.io/capstone.html).
