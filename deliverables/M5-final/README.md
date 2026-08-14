# 🏆 M5 - Final Submission

M5 contains the submitted report, poster, analysis scripts, result tables, and figures for **Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators**.

## Final Report

Use [`M5-Final-Report.pdf`](M5-Final-Report.pdf) for the submitted methodology, model-selection rule, numerical results, Research Question 2 findings, limitations, recommendations, and reproducibility statement.

## 📁 Primary Artifacts

| Artifact | Purpose |
| --- | --- |
| [`M5-Final-Report.pdf`](M5-Final-Report.pdf) | Final 16-page project report |
| [`M5 poster Final.pdf`](M5%20poster%20Final.pdf) | Final poster |
| [`ML Analysis.py`](ML%20Analysis.py) | Six-model forecasting comparison for 3-, 6-, and 12-month targets |
| [`Correlation analysis.py`](Correlation%20analysis.py) | Separate RQ2 Pearson/Spearman, lead-lag, period-stability, and recession-comparison analysis |
| [`analysis-results/`](analysis-results/) | Submitted RQ2 tables and an inventory of earlier development-run CSV exports |
| [`Plots/`](Plots/) | Final ML and correlation figures |

Both analysis scripts read the submitted [`../../data/processed/capstone_plus_final.xlsx`](../../data/processed/capstone_plus_final.xlsx) through its public, read-only GitHub URL.

The [analysis-results inventory](analysis-results/README.md) separates submitted RQ2 tables from older lowercase development exports. Final selected-model metrics must come from the report and submitted six-model script, not from those earlier CSVs.

## 📊 Final Dataset

| Attribute | Final value |
| --- | --- |
| Study period | April 1956-December 2025 |
| Rows | 837 |
| Columns | 40 |
| Predictors | 35 |
| Forecast targets | 3, 6, and 12 months |

## 🤖 Validation and Model Selection

The workflow uses a chronological train/validation/test split with a horizon-specific embargo. For each horizon, the model with the lowest validation RMSE was selected; validation MAE served as the tiebreaker. The selected model was then refitted on the full pre-test period and evaluated once on the untouched test set.

A different model's lower test RMSE does not retroactively change the selected model.

## 🥇 Final Forecasting Results

| Horizon | Selected model | Test MAE | Test RMSE | Test R² |
| --- | --- | ---: | ---: | ---: |
| 3 months | Ridge Regression | 0.349 | 1.020 | 0.720 |
| 6 months | Extra Trees | 0.725 | 1.277 | 0.563 |
| 12 months | Extra Trees | 1.195 | 1.729 | 0.205 |

The three-month model is the strongest operational result. Six-month performance is moderately informative. Twelve-month performance has limited incremental value and is best treated as scenario-level evidence rather than a reliable one-year prediction.

## 🔎 Research Question 2

Consumer sentiment was the strongest full-sample external historical relationship with unemployment at every horizon, strengthening from Pearson `r = -0.351` in the same month to `r = -0.496` at twelve months. Recession status ranked second.

At a six-month lead, the consumer-sentiment relationship reversed to `+0.67` during 2020-2025. Because that period is short and includes the pandemic and recovery, the reversal is interpreted as possible regime instability, not a permanent structural change.

These are historical associations, not causal estimates.

## ⚠️ Reproducibility and Limitations

Results can change if the input data, feature definitions, date ranges, seeds, packages, hyperparameters, or model configurations change. Such changes constitute a new analysis version rather than direct reproduction of the submitted results.

Important limitations include retrospective NBER labels, unemployment-derived composite features, structural breaks, national aggregation, revised historical data, a single chronological split, no formal prediction intervals, and serial dependence.

All artifacts are available for public inspection and download. Running the scripts does not require GitHub write access.

## 📌 Milestone Status

✅ M5 completed.
