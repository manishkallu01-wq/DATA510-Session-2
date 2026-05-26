# Backlog: Economic Disruption and Unemployment Trend Analysis

This file is the **human-readable mirror** of the GitHub Projects (v2) Iterative Development board for this repo. Every row here is also a GitHub issue, added to the board, tagged with a milestone label, and sized.

## Conventions

- Each item has: id, title, hypothesis or user story, **Create / Observe / Analyze** triple, milestone tag, size.
- Items are ordered top to bottom by **priority**.
- Milestone tags: `M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`.
- Sizes: S, M, L, XL.
- The board has five columns: `Backlog` → `Create` → `Observe` → `Analyze` → `Done`.
- WIP cap: `Create + Observe + Analyze` ≤ `owners + 1` at any time.
- Definition of Ready and Definition of Done live in `CHARTER.md`.

## Items

### PBI-001

- **Title:** Acquire and document FRED unemployment datasets
- **Hypothesis:** FRED unemployment datasets are accessible, license-compatible, and sufficient for long-term unemployment trend analysis.
- **Create:** Build ingestion scripts and document schema in `data/README.md`.
- **Observe:** Check row counts, missing values, date ranges, and consistency across datasets.
- **Analyze:** Determine whether FRED datasets meet project feasibility requirements.
- **Tag:** `M1-proposal`
- **Size:** M
- **GitHub issue:** To be added

### PBI-002

- **Title:** Acquire and integrate BLS labor market datasets
- **Hypothesis:** BLS datasets provide industry-level unemployment insights that complement FRED economic indicators.
- **Create:** Develop ETL pipeline for BLS datasets and normalize schema formats.
- **Observe:** Validate time frequency alignment and missingness across datasets.
- **Analyze:** Evaluate whether BLS integration improves analytical depth.
- **Tag:** `M1-proposal`
- **Size:** M
- **GitHub issue:** To be added

### PBI-003

- **Title:** Draft and finalize research questions
- **Hypothesis:** The project research questions can be framed as measurable and testable economic analysis questions.
- **Create:** Add finalized research questions to proposal and `CHARTER.md`.
- **Observe:** Verify clarity through peer review and Studio Brief feedback.
- **Analyze:** Revise wording and scope based on stakeholder feedback.
- **Tag:** `M1-proposal`
- **Size:** S
- **GitHub issue:** To be added

### PBI-004

- **Title:** Build unified economic indicators dataset
- **Hypothesis:** Economic indicators from multiple public APIs can be merged into a clean analytical dataset.
- **Create:** Combine unemployment, inflation, GDP, CPI, and recession indicators into a unified schema.
- **Observe:** Validate joins, timestamps, feature consistency, and null values.
- **Analyze:** Identify integration challenges and required transformations.
- **Tag:** `M2-data-summary`
- **Size:** L
- **GitHub issue:** To be added

### PBI-005

- **Title:** Perform exploratory data analysis on unemployment trends
- **Hypothesis:** Historical unemployment data contains measurable patterns linked to major economic disruptions.
- **Create:** Generate exploratory visualizations and statistical summaries.
- **Observe:** Identify trend shifts during recessions, inflation spikes, and COVID-19 periods.
- **Analyze:** Determine which variables show strongest relationships with unemployment.
- **Tag:** `M2-data-summary`
- **Size:** M
- **GitHub issue:** To be added

### PBI-006

- **Title:** Develop baseline unemployment forecasting model
- **Hypothesis:** Historical economic indicators can support predictive unemployment forecasting.
- **Create:** Train baseline forecasting models using economic indicators and unemployment data.
- **Observe:** Evaluate forecasting accuracy using RMSE and validation metrics.
- **Analyze:** Compare model performance against baseline assumptions.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **GitHub issue:** To be added

### PBI-007

- **Title:** Create interactive unemployment trend dashboard
- **Hypothesis:** Interactive dashboards improve interpretation of economic and unemployment relationships.
- **Create:** Build dashboards using Plotly, Tableau, or Power BI.
- **Observe:** Verify usability, filtering, and visualization clarity.
- **Analyze:** Identify which visualizations communicate findings most effectively.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **GitHub issue:** To be added

### PBI-008

- **Title:** Evaluate ethics and bias risks in forecasting outputs
- **Hypothesis:** Economic forecasting outputs may contain interpretability and fairness limitations.
- **Create:** Document ethics considerations and forecasting limitations.
- **Observe:** Review risks related to bias, fairness, and misleading conclusions.
- **Analyze:** Recommend safeguards and limitations for interpretation.
- **Tag:** `ethics`
- **Size:** S
- **GitHub issue:** To be added

### PBI-009

- **Title:** Draft final project report and methodology
- **Hypothesis:** A reproducible methodology and documented findings will clearly support project conclusions.
- **Create:** Write methodology, findings, visualizations, and conclusions sections.
- **Observe:** Validate reproducibility and completeness of documentation.
- **Analyze:** Revise based on peer review and instructor feedback.
- **Tag:** `M4-writeup-draft`
- **Size:** L
- **GitHub issue:** To be added

### PBI-010

- **Title:** Finalize poster and presentation deliverables
- **Hypothesis:** A polished poster and presentation will effectively communicate project insights and technical contributions.
- **Create:** Design final poster, presentation visuals, and summary findings.
- **Observe:** Gather peer feedback on readability and presentation quality.
- **Analyze:** Refine final deliverables before submission.
- **Tag:** `M5-final`
- **Size:** M
- **GitHub issue:** To be added
