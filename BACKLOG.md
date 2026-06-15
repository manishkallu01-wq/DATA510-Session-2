# Backlog: Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

This file is the **human-readable mirror** of the GitHub Projects (v2) Iterative Development board for this repository. Every row here is also represented as a GitHub issue, added to the board, tagged with a milestone label, and sized.

## Conventions

* Each item contains: id, title, hypothesis or user story, **Create / Observe / Analyze** triple, milestone tag, size, and GitHub issue reference.
* Items are ordered by priority.
* Milestone tags: `M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`.
* Sizes: S, M, L, XL.
* Workflow columns: `Backlog` → `Create` → `Observe` → `Analyze` → `Done`.
* Definition of Ready and Definition of Done are documented in `CHARTER.md`.

---

## PBI-001

* **Title:** Acquire and validate approved macroeconomic datasets
* **Hypothesis:** Publicly available macroeconomic datasets provide sufficient historical coverage and quality to support unemployment forecasting and analysis.
* **Create:** Acquire UNRATE, CPIAUCSL, FEDFUNDS, GDP, UMCSENT, and USREC datasets.
* **Observe:** Validate schema consistency, date coverage, missing values, and source reliability.
* **Analyze:** Determine dataset suitability for the research questions.
* **Tag:** `M1-proposal`
* **Size:** M
* **GitHub issue:** #1

---

## PBI-002

* **Title:** Build integrated analytical dataset
* **Hypothesis:** Multiple macroeconomic indicators can be integrated into a unified analytical dataset suitable for forecasting and statistical analysis.
* **Create:** Standardize and merge approved datasets into a common monthly framework.
* **Observe:** Validate joins, temporal alignment, duplicates, and data quality.
* **Analyze:** Evaluate dataset readiness for downstream analysis.
* **Tag:** `M1-proposal`
* **Size:** L
* **GitHub issue:** #2

---

## PBI-003

* **Title:** Finalize research questions and project scope
* **Hypothesis:** Clearly defined research questions improve analytical focus and project outcomes.
* **Create:** Finalize proposal, research questions, and project documentation.
* **Observe:** Review stakeholder and instructor feedback.
* **Analyze:** Refine scope and project objectives.
* **Tag:** `M1-proposal`
* **Size:** S
* **GitHub issue:** #3

---

## PBI-004

* **Title:** Engineer forecasting and analytical features
* **Hypothesis:** Engineered features improve the ability to identify relationships and forecast unemployment trends.
* **Create:** Develop lag variables, momentum metrics, growth indicators, and composite economic measures.
* **Observe:** Review feature distributions and quality metrics.
* **Analyze:** Assess feature usefulness and analytical value.
* **Tag:** `M2-data-summary`
* **Size:** L
* **GitHub issue:** #4

---

## PBI-005

* **Title:** Perform exploratory data analysis
* **Hypothesis:** Historical economic indicators contain measurable patterns associated with unemployment behavior.
* **Create:** Generate summary statistics, trend analyses, and exploratory visualizations.
* **Observe:** Identify trends, anomalies, and economic cycle patterns.
* **Analyze:** Determine which indicators demonstrate the strongest historical relationships with unemployment.
* **Tag:** `M2-data-summary`
* **Size:** M
* **GitHub issue:** #5

---

## PBI-006

* **Title:** Conduct statistical relationship analysis
* **Hypothesis:** Certain macroeconomic indicators consistently exhibit stronger relationships with unemployment than others.
* **Create:** Perform correlation, trend, and lead-lag analyses.
* **Observe:** Measure relationship strength and direction.
* **Analyze:** Identify key indicators associated with unemployment movements.
* **Tag:** `M2-data-summary`
* **Size:** M
* **GitHub issue:** #6

---

## PBI-007

* **Title:** Develop unemployment forecasting models
* **Hypothesis:** Macroeconomic indicators improve forecasting performance relative to historical unemployment trends alone.
* **Create:** Train Linear Regression, Random Forest, and XGBoost forecasting models.
* **Observe:** Evaluate model performance using RMSE, MAE, and R².
* **Analyze:** Compare forecasting performance across prediction horizons.
* **Tag:** `M3-poster-draft`
* **Size:** L
* **GitHub issue:** #7

---

## PBI-008

* **Title:** Create visualizations and stakeholder-facing outputs
* **Hypothesis:** Visual analytics improve communication of technical findings and economic insights.
* **Create:** Develop trend charts, correlation heatmaps, feature importance visuals, and forecasting comparisons.
* **Observe:** Evaluate clarity and stakeholder usefulness.
* **Analyze:** Refine outputs based on feedback.
* **Tag:** `M3-poster-draft`
* **Size:** M
* **GitHub issue:** #8

---

## PBI-009

* **Title:** Evaluate ethics, risks, and limitations
* **Hypothesis:** Transparent discussion of limitations improves responsible interpretation of forecasting results.
* **Create:** Document assumptions, risks, limitations, and ethical considerations.
* **Observe:** Review potential misuse and interpretation risks.
* **Analyze:** Develop mitigation and communication strategies.
* **Tag:** `ethics`
* **Size:** S
* **GitHub issue:** #9

---

## PBI-010

* **Title:** Complete final report and presentation deliverables
* **Hypothesis:** A well-documented and reproducible project improves communication, credibility, and stakeholder value.
* **Create:** Prepare final write-up, poster, visualizations, and supporting documentation.
* **Observe:** Collect stakeholder and instructor feedback.
* **Analyze:** Refine final deliverables before submission.
* **Tag:** `M5-final`
* **Size:** L
* **GitHub issue:** #10
