## Final Dataset Schema

This file documents the schema for the final analysis-ready dataset used in the capstone project:

**Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators**

---

## Dataset Overview

**File name:** `capstone_capstone_plus_final.csv`

**Expected location:** `data/processed/capstone_capstone_plus_final.csv`

**Observation period:** April 1956 – January 2026

**Rows:** 838

**Columns:** 40

**Primary key:** `Date`

**Grain:** One row per month

**Project owner:** Manish R Kallu

---

## Primary Key

| Column | Type | Description                                                                          |
| ------ | ---- | ------------------------------------------------------------------------------------ |
| `Date` | Date | Monthly observation date. This is the primary key used to align all source datasets. |

---

## Source Variables

| Column                 | Type    | Unit                | Source File    | Description                                                                        |
| ---------------------- | ------- | ------------------- | -------------- | ---------------------------------------------------------------------------------- |
| `UnemploymentRate`     | Numeric | Percent             | `UNRATE.csv`   | U.S. unemployment rate. Main labor market outcome variable.                        |
| `ConsumerPriceIndex`   | Numeric | Index               | `CPIAUCSL.csv` | Consumer Price Index for All Urban Consumers. Used to measure inflation.           |
| `FederalFundsRate`     | Numeric | Percent             | `FEDFUNDS.csv` | Effective federal funds rate. Used as the monetary policy indicator.               |
| `GrossDomesticProduct` | Numeric | Billions of dollars | `GDP.csv`      | U.S. gross domestic product. Quarterly source data aligned into the monthly panel. |
| `ConsumerSentiment`    | Numeric | Index               | `UMCSENT.csv`  | University of Michigan consumer sentiment index.                                   |
| `RecessionIndicator`   | Integer | 0 / 1               | `USREC.csv`    | Recession flag where 1 indicates recession and 0 indicates non-recession.          |

---

## Inflation Features

| Column                       | Type    | Unit                    | Description                                                                                                 |
| ---------------------------- | ------- | ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| `InflationRateYoY`           | Numeric | Percent                 | Year-over-year inflation rate calculated from CPI.                                                          |
| `InflationLag3`              | Numeric | Percent                 | Inflation rate lagged by three months.                                                                      |
| `InflationLag6`              | Numeric | Percent                 | Inflation rate lagged by six months.                                                                        |
| `InflationAcceleration`      | Numeric | Percentage point change | Change in inflation rate over time, used to capture whether inflation pressure is increasing or decreasing. |
| `InflationUnemploymentRatio` | Numeric | Ratio                   | Ratio between inflation and unemployment, used to compare price pressure with labor market conditions.      |

---

## Economic Growth Features

| Column                   | Type    | Unit                    | Description                                                                                            |
| ------------------------ | ------- | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| `GDPGrowthYoY`           | Numeric | Percent                 | Year-over-year GDP growth rate.                                                                        |
| `GDPGrowthLag3`          | Numeric | Percent                 | GDP growth lagged by three months.                                                                     |
| `GDPGrowthLag6`          | Numeric | Percent                 | GDP growth lagged by six months.                                                                       |
| `GDPGrowthMomentum`      | Numeric | Percentage point change | Change in GDP growth over time, used to capture acceleration or slowdown in economic growth.           |
| `GrowthToInflationRatio` | Numeric | Ratio                   | Ratio between GDP growth and inflation, used to compare economic expansion against inflation pressure. |

---

## Monetary Policy Features

| Column                    | Type    | Unit          | Description                                                                                      |
| ------------------------- | ------- | ------------- | ------------------------------------------------------------------------------------------------ |
| `RealInterestRate`        | Numeric | Percent       | Federal funds rate adjusted by inflation.                                                        |
| `FederalFundsLag3`        | Numeric | Percent       | Federal funds rate lagged by three months.                                                       |
| `FederalFundsLag6`        | Numeric | Percent       | Federal funds rate lagged by six months.                                                         |
| `MonetaryTighteningIndex` | Numeric | Index / score | Derived indicator measuring restrictive monetary policy conditions.                              |
| `PolicyPressureScore`     | Numeric | Score         | Composite measure combining inflation and interest rate conditions to represent policy pressure. |

---

## Labor Market Features

| Column                 | Type    | Unit                    | Description                                                                     |
| ---------------------- | ------- | ----------------------- | ------------------------------------------------------------------------------- |
| `UnemploymentChange1M` | Numeric | Percentage point change | One-month change in unemployment rate.                                          |
| `UnemploymentChange3M` | Numeric | Percentage point change | Three-month change in unemployment rate.                                        |
| `UnemploymentLag1`     | Numeric | Percent                 | Unemployment rate lagged by one month.                                          |
| `UnemploymentLag3`     | Numeric | Percent                 | Unemployment rate lagged by three months.                                       |
| `UnemploymentLag6`     | Numeric | Percent                 | Unemployment rate lagged by six months.                                         |
| `UnemploymentLag12`    | Numeric | Percent                 | Unemployment rate lagged by twelve months.                                      |
| `UnemploymentMomentum` | Numeric | Percentage point change | Direction and speed of unemployment movement over time.                         |
| `LaborMarketShock`     | Integer | 0 / 1                   | Indicator for unusually large unemployment movement or labor market disruption. |

---

## Consumer Sentiment Features

| Column                            | Type    | Unit               | Description                                        |
| --------------------------------- | ------- | ------------------ | -------------------------------------------------- |
| `ConsumerSentimentMomentum3M`     | Numeric | Index point change | Three-month change in consumer sentiment.          |
| `ConsumerSentimentLag3`           | Numeric | Index              | Consumer sentiment lagged by three months.         |
| `ConsumerSentimentLag6`           | Numeric | Index              | Consumer sentiment lagged by six months.           |
| `ConsumerConfidenceDeterioration` | Numeric | Index point change | Measures decline in consumer confidence over time. |

---

## Composite Economic Indicators

| Column                | Type    | Unit  | Description                                                                                     |
| --------------------- | ------- | ----- | ----------------------------------------------------------------------------------------------- |
| `EconomicStressIndex` | Numeric | Score | Composite indicator combining labor market weakness, inflation pressure, and growth conditions. |
| `RecessionRiskScore`  | Numeric | Score | Composite indicator representing recessionary risk based on economic and labor market signals.  |

---

## Forecast Targets

| Column                      | Type    | Unit    | Description                                                                               |
| --------------------------- | ------- | ------- | ----------------------------------------------------------------------------------------- |
| `FutureUnemployment_3M`     | Numeric | Percent | Unemployment rate shifted three months into the future. Target for 3-month forecasting.   |
| `FutureUnemployment_6M`     | Numeric | Percent | Unemployment rate shifted six months into the future. Target for 6-month forecasting.     |
| `FutureUnemployment_12M`    | Numeric | Percent | Unemployment rate shifted twelve months into the future. Target for 12-month forecasting. |
| `FutureLaborMarketShock_6M` | Integer | 0 / 1   | Future labor market shock indicator six months ahead.                                     |

---

## Data Quality Expectations

The final dataset should satisfy the following checks:

| Check                    | Expected Result |
| ------------------------ | --------------- |
| Rows                     | 838             |
| Columns                  | 40              |
| Duplicate dates          | 0               |
| Duplicate rows           | 0               |
| Missing monthly periods  | 0               |
| Infinite values          | 0               |
| Missing predictor values | 0               |

The only expected missing values are in future target columns near the end of the dataset:

| Column                   | Expected Missing Values |
| ------------------------ | ----------------------- |
| `FutureUnemployment_3M`  | 3                       |
| `FutureUnemployment_6M`  | 6                       |
| `FutureUnemployment_12M` | 12                      |

These missing values are expected because future observations are not available beyond the final months of the dataset.

---

## Notes

* The dataset is observational and should not be used to make causal claims.
* GDP originates as quarterly data and is aligned into the monthly analytical panel.
* Outliers caused by real economic events, including recessions and COVID-era labor market disruption, are intentionally retained.
* The dataset is frozen for analysis after Milestone 2.
