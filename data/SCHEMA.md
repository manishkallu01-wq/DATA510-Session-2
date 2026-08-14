# 🧾 Final Dataset Schema

This file documents the submitted analysis-ready workbook for **Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators**.

## 📌 Dataset Profile

| Attribute | Final value |
| --- | --- |
| File | [`data/processed/capstone_plus_final.xlsx`](processed/capstone_plus_final.xlsx) |
| Study period | April 1956-December 2025 |
| Grain | One row per month |
| Primary key | `Date` |
| Rows | 837 |
| Columns | 40 |
| Predictors | 35 |
| Future targets | 4 |
| Duplicate dates | 0 |
| Infinite numeric values | 0 |
| Unexpected missing predictor values | 0 |

The final 3, 6, and 12 entries of the corresponding future-unemployment targets are intentionally missing because those future observations do not exist beyond December 2025.

## 🔑 Key and Source Variables

| Column | Type | Unit | Description |
| --- | --- | --- | --- |
| `Date` | Date | Month | Monthly observation key |
| `UnemploymentRate` | Numeric | Percent | U.S. unemployment rate |
| `ConsumerPriceIndex` | Numeric | Index | Consumer Price Index for All Urban Consumers |
| `FederalFundsRate` | Numeric | Percent | Effective federal funds rate |
| `GrossDomesticProduct` | Numeric | Billions of current dollars | Quarterly GDP aligned to the monthly panel |
| `ConsumerSentiment` | Numeric | Index | University of Michigan consumer sentiment |
| `RecessionIndicator` | Integer | 0/1 | NBER historical recession indicator |

## 📈 Inflation, Growth, and Policy Features

| Column | Type | Unit | Construction or meaning |
| --- | --- | --- | --- |
| `InflationRateYoY` | Numeric | Percent | 12-month percent change in CPI |
| `GDPGrowthYoY` | Numeric | Percent | 12-month percent change in GDP |
| `RealInterestRate` | Numeric | Percentage points | Federal funds rate minus year-over-year inflation |
| `InflationLag3` | Numeric | Percent | Inflation rate lagged 3 months |
| `FederalFundsLag3` | Numeric | Percent | Federal funds rate lagged 3 months |
| `GDPGrowthLag3` | Numeric | Percent | GDP growth lagged 3 months |
| `InflationLag6` | Numeric | Percent | Inflation rate lagged 6 months |
| `FederalFundsLag6` | Numeric | Percent | Federal funds rate lagged 6 months |
| `GDPGrowthLag6` | Numeric | Percent | GDP growth lagged 6 months |
| `InflationAcceleration` | Numeric | Percentage-point change | One-month change in year-over-year inflation |
| `GDPGrowthMomentum` | Numeric | Percentage-point change | Current GDP growth minus its 3-month lag |
| `MonetaryTighteningIndex` | Numeric | Percentage points | Current federal funds rate minus its 6-month lag |
| `PolicyPressureScore` | Numeric | Score | Federal funds rate multiplied by inflation |

## 👷 Labor-Market Features

| Column | Type | Unit | Construction or meaning |
| --- | --- | --- | --- |
| `UnemploymentChange1M` | Numeric | Percentage points | Current unemployment minus its 1-month lag |
| `UnemploymentChange3M` | Numeric | Percentage points | Current unemployment minus its 3-month lag |
| `UnemploymentLag1` | Numeric | Percent | Unemployment rate lagged 1 month |
| `UnemploymentLag3` | Numeric | Percent | Unemployment rate lagged 3 months |
| `UnemploymentLag6` | Numeric | Percent | Unemployment rate lagged 6 months |
| `UnemploymentLag12` | Numeric | Percent | Unemployment rate lagged 12 months |
| `UnemploymentMomentum` | Numeric | Percentage points | Three-month unemployment change |
| `LaborMarketShock` | Integer | 0/1 | 1 when the 3-month unemployment increase is at least 0.5 percentage points |

## 💭 Consumer-Sentiment Features

| Column | Type | Unit | Construction or meaning |
| --- | --- | --- | --- |
| `ConsumerSentimentMomentum3M` | Numeric | Index points | Current sentiment minus its 3-month lag |
| `ConsumerSentimentLag3` | Numeric | Index | Consumer sentiment lagged 3 months |
| `ConsumerSentimentLag6` | Numeric | Index | Consumer sentiment lagged 6 months |
| `ConsumerConfidenceDeterioration` | Numeric | Index points | 6-month sentiment lag minus current sentiment |

## 🧮 Ratios and Composite Features

| Column | Type | Unit | Construction or meaning |
| --- | --- | --- | --- |
| `EconomicStressIndex` | Numeric | Standardized score | Mean standardized unemployment, inflation, and federal funds rate |
| `InflationUnemploymentRatio` | Numeric | Ratio | Inflation divided by unemployment |
| `GrowthToInflationRatio` | Numeric | Ratio | GDP growth divided by inflation |
| `RecessionRiskScore` | Numeric | Score | Economic stress index plus recession and labor-shock indicators |

Composite features that incorporate unemployment or retrospective recession information must not be described as independent real-time external signals.

## 🎯 Future Targets

| Column | Type | Unit | Construction or meaning |
| --- | --- | --- | --- |
| `FutureUnemployment_3M` | Numeric | Percent | Unemployment shifted 3 months forward |
| `FutureUnemployment_6M` | Numeric | Percent | Unemployment shifted 6 months forward |
| `FutureUnemployment_12M` | Numeric | Percent | Unemployment shifted 12 months forward |
| `FutureLaborMarketShock_6M` | Numeric | 0/1 | Labor-market-shock indicator shifted 6 months forward |

## ✅ Complete Column Order

1. `Date`
2. `UnemploymentRate`
3. `ConsumerPriceIndex`
4. `FederalFundsRate`
5. `GrossDomesticProduct`
6. `ConsumerSentiment`
7. `RecessionIndicator`
8. `InflationRateYoY`
9. `GDPGrowthYoY`
10. `RealInterestRate`
11. `UnemploymentChange1M`
12. `UnemploymentChange3M`
13. `ConsumerSentimentMomentum3M`
14. `UnemploymentLag1`
15. `UnemploymentLag3`
16. `UnemploymentLag6`
17. `UnemploymentLag12`
18. `InflationLag3`
19. `FederalFundsLag3`
20. `GDPGrowthLag3`
21. `ConsumerSentimentLag3`
22. `InflationLag6`
23. `FederalFundsLag6`
24. `GDPGrowthLag6`
25. `ConsumerSentimentLag6`
26. `EconomicStressIndex`
27. `LaborMarketShock`
28. `InflationAcceleration`
29. `GDPGrowthMomentum`
30. `UnemploymentMomentum`
31. `MonetaryTighteningIndex`
32. `PolicyPressureScore`
33. `ConsumerConfidenceDeterioration`
34. `InflationUnemploymentRatio`
35. `GrowthToInflationRatio`
36. `RecessionRiskScore`
37. `FutureUnemployment_3M`
38. `FutureUnemployment_6M`
39. `FutureUnemployment_12M`
40. `FutureLaborMarketShock_6M`

## 🔁 Reconstruction Reference

The maintained workflow is documented in [`../src/README.md`](../src/README.md):

1. `src/rebuild.py` reads the six raw CSVs and creates local `super_dataset.csv`.
2. `src/eng_variables.py` creates local `capstone_plus_final.xlsx`.
3. `src/checks.py` validates the local final workbook.

Generated reconstruction files default to the user's local `Downloads` folder and are not written or pushed to the repository.
