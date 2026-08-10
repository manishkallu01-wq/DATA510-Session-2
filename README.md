# Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

**DATA 510 – Data Science Studio (DS3), Session 2**  
**Willamette University | Summer 2026**  
**Author:** Manish R. Kallu

[View the live project portfolio](https://manishkallu01-wq.github.io/) · [Browse project deliverables](deliverables/) · [View the project board](https://github.com/users/manishkallu01-wq/projects/1)

## Project Overview

This capstone examines whether publicly available macroeconomic indicators improve forecasts of future U.S. unemployment and identifies the indicators with the strongest historical relationships to labor-market conditions.

The final analytical dataset combines nearly 70 years of monthly U.S. economic history, from **April 1956 through December 2025**. It contains **837 observations, 40 columns, and 35 predictors** derived from six public series:

- Unemployment rate (BLS/FRED)
- Consumer Price Index (BLS/FRED)
- Federal funds rate (Federal Reserve/FRED)
- Real GDP (BEA/FRED)
- Consumer sentiment (University of Michigan/FRED)
- Recession indicator (NBER/FRED)

Quarterly GDP was converted to monthly frequency, the sources were aligned by date, and lagged, momentum, ratio, and composite features were engineered for multi-horizon forecasting.

## Research Questions

1. To what extent can publicly available macroeconomic indicators improve forecasting of future U.S. unemployment across 3-month, 6-month, and 12-month horizons?
2. Which macroeconomic indicators demonstrate the strongest and most consistent historical relationships with unemployment across U.S. economic cycles between 1956 and 2025?

## Final Results

Models were evaluated with a chronological train/test split using MAE, RMSE, and R².

| Forecast horizon | Selected model | MAE | RMSE | R² |
| --- | --- | ---: | ---: | ---: |
| 3 months | Ridge Regression | 0.349 | 1.020 | 0.720 |
| 6 months | Extra Trees | 0.725 | 1.277 | 0.563 |
| 12 months | Extra Trees | 1.195 | 1.729 | 0.205 |

The 3-month model produced the strongest forecast performance. Accuracy declined at longer horizons, showing that public macroeconomic indicators are most useful as near-term early-warning signals rather than precise long-range forecasts.

For the historical relationship analysis, **consumer sentiment was the strongest overall external indicator**, reaching a correlation of **r = −0.496 at the 12-month horizon**. These relationships are regime-dependent associations and should not be interpreted as causal effects.

## Repository Structure

| Path | Purpose |
| --- | --- |
| [`data/`](data/) | Raw, processed, and final analytical datasets |
| [`src/`](src/) | Data preparation, feature engineering, analysis, and modeling code |
| [`notebooks/`](notebooks/) | Exploratory analysis and model-development notebooks |
| [`deliverables/`](deliverables/) | Final report, poster, and milestone submissions |
| [`studio/`](studio/) | Studio briefs, critiques, and collaboration artifacts |
| [`BACKLOG.md`](BACKLOG.md) | Project backlog |
| [`CHARTER.md`](CHARTER.md) | Project charter and governance |

## Reproducing the Analysis

1. Clone the repository:
   ```bash
   git clone https://github.com/manishkallu01-wq/DATA510-Session-2.git
   cd DATA510-Session-2
   ```
2. Use Python 3 and install the analysis packages used by the project:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn xgboost
   ```
3. Review the source files in [`src/`](src/) and notebooks in [`notebooks/`](notebooks/).
4. Run the data preparation and feature-engineering workflow before the modeling workflow.
5. Compare reproduced metrics and visualizations with the final materials in [`deliverables/`](deliverables/).

The workflow uses a time-ordered split to avoid training on future observations. Random seeds are fixed where supported by the selected estimators.

## Limitations and Responsible Use

- NBER recession labels are retrospective and are not real-time signals.
- Some engineered composite features contain unemployment information and require careful interpretation.
- Structural breaks, including COVID-19, reduce stability across economic regimes.
- National aggregates can conceal state, industry, and demographic differences.
- Revised historical data may differ from the vintages available at an actual forecast date.
- Results rely on one chronological holdout period and do not include formal prediction intervals.
- Correlation and feature importance indicate association, not causation.
- Serial dependence may make conventional independent-observation interpretations inappropriate.

The models are educational decision-support tools. They should not be used alone for policy, investment, employment, or other high-stakes decisions.

## Final Deliverables

- Integrated and feature-engineered macroeconomic dataset
- Lead-lag relationship and economic-cycle analysis
- 3-, 6-, and 12-month unemployment forecasting models
- Model evaluation and feature-importance analysis
- Final research report
- Final poster presentation
- Live project portfolio
- Reproducible code and documentation

**Project status: Complete and ready for submission.**

## Data Attribution

The project uses publicly available data from the U.S. Bureau of Labor Statistics, Federal Reserve Economic Data, U.S. Bureau of Economic Analysis, University of Michigan Surveys of Consumers, and National Bureau of Economic Research. Source organizations retain ownership of their respective data.
