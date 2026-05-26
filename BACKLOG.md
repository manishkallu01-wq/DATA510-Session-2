# Backlog: Economic Disruption and Unemployment Trend Analysis

This file is the **human-readable mirror** of the GitHub Projects (v2) Iterative Development board for this repository. Every row here is also represented as a GitHub issue, added to the board, tagged with a milestone label, and sized.

## Conventions

- Each item contains: id, title, hypothesis or user story, **Create / Observe / Analyze** triple, milestone tag, size, and GitHub issue reference.
- Items are ordered top to bottom by **priority**.
- Milestone tags: `M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`.
- Sizes: S, M, L, XL.
- Workflow columns on the board: `Backlog` → `Create` → `Observe` → `Analyze` → `Done`.
- WIP cap: `Create + Observe + Analyze` ≤ `owners + 1`.
- Definition of Ready and Definition of Done are documented in `CHARTER.md`.

## Items

### PBI-001

- **Title:** Acquire and validate FRED unemployment datasets
- **Hypothesis:** FRED unemployment datasets provide reliable and sufficiently complete historical indicators for long-term unemployment trend analysis.
- **Create:** Build FRED API ingestion scripts and document dataset schemas in `data/README.md`.
- **Observe:** Validate row counts, missing values, historical date coverage, and schema consistency.
- **Analyze:** Determine whether FRED datasets satisfy project feasibility requirements for proposal objectives.
- **Tag:** `M1-proposal`
- **Size:** M
- **GitHub issue:** #1

### PBI-002

- **Title:** Acquire and integrate BLS labor market datasets
- **Hypothesis:** BLS labor market datasets improve industry-level unemployment analysis and complement FRED economic indicators.
- **Create:** Develop ETL workflows for BLS datasets and normalize schema formats.
- **Observe:** Verify time-frequency alignment, missingness, and compatibility across datasets.
- **Analyze:** Evaluate whether BLS integration improves analytical depth and supports the research questions.
- **Tag:** `M1-proposal`
- **Size:** M
- **GitHub issue:** #2

### PBI-003

- **Title:** Finalize project research questions and proposal framing
- **Hypothesis:** The project research questions can be refined into measurable and testable economic analysis objectives.
- **Create:** Finalize proposal research questions and update `CHARTER.md` documentation.
- **Observe:** Validate clarity through peer stakeholder feedback and Studio Brief critiques.
- **Analyze:** Refine wording, scope, and framing based on stakeholder responses.
- **Tag:** `M1-proposal`
- **Size:** S
- **GitHub issue:** #3

### PBI-004

- **Title:** Build unified economic indicators dataset
- **Hypothesis:** Public economic datasets from multiple APIs can be merged into a clean analytical dataset for downstream analysis.
- **Create:** Integrate unemployment, GDP, CPI, inflation, and recession indicator datasets into a unified schema.
- **Observe:** Validate joins, timestamps, feature consistency, and null-value handling.
- **Analyze:** Identify integration limitations and required preprocessing transformations.
- **Tag:** `M1-proposal`
- **Size:** L
- **GitHub issue:** #4

### PBI-005

- **Title:** Perform exploratory data analysis on unemployment trends
- **Hypothesis:** Historical unemployment datasets contain measurable patterns associated with recessions, inflation, COVID-19, layoffs, and economic disruptions.
- **Create:** Generate exploratory visualizations and descriptive statistical summaries.
- **Observe:** Identify trend changes during major economic disruptions and recession periods.
- **Analyze:** Determine which variables demonstrate the strongest relationships with unemployment trends.
- **Tag:** `M1-proposal`
- **Size:** M
- **GitHub issue:** #5

### PBI-006

- **Title:** Develop baseline unemployment forecasting models
- **Hypothesis:** Historical economic indicators can support baseline unemployment forecasting performance.
- **Create:** Train baseline forecasting models using unemployment and economic indicator datasets.
- **Observe:** Evaluate forecasting accuracy using RMSE and validation metrics.
- **Analyze:** Compare forecasting outputs against baseline assumptions and historical unemployment behavior.
- **Tag:** `M2-data-summary`
- **Size:** L
- **GitHub issue:** #6

### PBI-007

- **Title:** Create interactive unemployment trend dashboards
- **Hypothesis:** Interactive dashboards improve interpretation and communication of unemployment and economic indicator relationships.
- **Create:** Build dashboards using Plotly, Tableau, or Power BI.
- **Observe:** Validate usability, filtering functionality, and visualization clarity.
- **Analyze:** Determine which visualizations most effectively communicate project findings to stakeholders.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **GitHub issue:** #7

### PBI-008

- **Title:** Evaluate ethics and bias risks in forecasting outputs
- **Hypothesis:** Forecasting models may contain fairness, interpretability, and deployment limitations that require documentation and mitigation.
- **Create:** Document ethics considerations, forecasting assumptions, and project limitations.
- **Observe:** Review fairness concerns, interpretability limitations, and risks of misleading conclusions.
- **Analyze:** Recommend safeguards and transparency practices for project reporting.
- **Tag:** `ethics`
- **Size:** S
- **GitHub issue:** #8

### PBI-009

- **Title:** Draft final project methodology and analytical write-up
- **Hypothesis:** A reproducible methodology and clearly documented findings will support credible and interpretable project conclusions.
- **Create:** Write methodology, findings, visualizations, discussion, and conclusions sections.
- **Observe:** Validate documentation completeness and reproducibility of analytical workflows.
- **Analyze:** Revise findings and documentation structure based on peer and instructor feedback.
- **Tag:** `M4-writeup-draft`
- **Size:** L
- **GitHub issue:** #9

### PBI-010

- **Title:** Finalize poster and presentation deliverables
- **Hypothesis:** A polished poster and presentation will effectively communicate project insights, methodology, and technical contributions.
- **Create:** Design final poster, presentation visuals, and summary findings.
- **Observe:** Gather stakeholder feedback on readability, clarity, and presentation quality.
- **Analyze:** Refine final deliverables before final submission and presentation.
- **Tag:** `M5-final`
- **Size:** M
- **GitHub issue:** #10
