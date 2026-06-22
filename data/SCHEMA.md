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

## Engineered Variable Dictionary

## Notation

* `t` = current monthly observation
* `t-1` = one month before the current observation
* `t-3` = three months before the current observation
* `t-6` = six months before the current observation
* `t-12` = twelve months before the current observation
* `t+3`, `t+6`, `t+12` = future unemployment values used as forecasting targets

---

## Inflation and Growth Features

### `InflationRateYoY`

**Description:**
Year-over-year inflation rate calculated from the Consumer Price Index.

**Formula / Construction:**
`InflationRateYoY = percent change in ConsumerPriceIndex over 12 months`

**Purpose:**
This variable captures how much consumer prices increased or decreased compared with the same month one year earlier. It is used to represent inflation pressure in the economy.

**Interpretation:**
Higher values indicate stronger inflation. Lower or negative values indicate weak inflation or deflationary pressure.

---

### `GDPGrowthYoY`

**Description:**
Year-over-year economic growth calculated from Gross Domestic Product.

**Formula / Construction:**
`GDPGrowthYoY = percent change in GrossDomesticProduct over 12 months`

**Purpose:**
This feature captures broad economic growth conditions. Since unemployment often responds to changes in economic activity, GDP growth is included as a key explanatory variable.

**Interpretation:**
Positive values indicate economic expansion. Negative values indicate economic contraction or recession-like conditions.

---

### `RealInterestRate`

**Description:**
Approximate real interest rate after accounting for inflation.

**Formula / Construction:**
`RealInterestRate = FederalFundsRate - InflationRateYoY`

**Purpose:**
This variable estimates the inflation-adjusted stance of monetary policy. It helps distinguish between high nominal interest rates caused by policy tightening and high rates that are offset by inflation.

**Interpretation:**
Higher values generally indicate tighter monetary conditions. Lower or negative values indicate looser real borrowing conditions.

---

## Labor Market Change Features

### `UnemploymentChange1M`

**Description:**
One-month change in the unemployment rate.

**Formula / Construction:**
`UnemploymentChange1M = UnemploymentRate(t) - UnemploymentRate(t-1)`

**Purpose:**
This variable captures short-term movement in unemployment.

**Interpretation:**
Positive values mean unemployment increased from the previous month. Negative values mean unemployment decreased.

---

### `UnemploymentChange3M`

**Description:**
Three-month change in the unemployment rate.

**Formula / Construction:**
`UnemploymentChange3M = UnemploymentRate(t) - UnemploymentRate(t-3)`

**Purpose:**
This variable captures short-term labor market momentum over a slightly wider window than the one-month change.

**Interpretation:**
Positive values indicate labor market weakening. Negative values indicate labor market improvement.

---

### `UnemploymentMomentum`

**Description:**
Momentum measure for unemployment movement.

**Formula / Construction:**
This variable follows the project’s unemployment momentum logic and is aligned with the three-month unemployment change.

**Purpose:**
It summarizes whether unemployment is trending upward or downward over a recent short-term window.

**Interpretation:**
Higher values indicate worsening labor market momentum. Lower or negative values indicate improving labor market momentum.

---

### `LaborMarketShock`

**Description:**
Binary indicator for a current labor market shock.

**Formula / Construction:**
This project defines a labor market shock as a sharp deterioration in unemployment conditions based on recent unemployment movement.

**Purpose:**
This variable is used to identify periods where the labor market experiences abnormal stress rather than normal month-to-month variation.

**Interpretation:**

* `1` = labor market shock period
* `0` = no labor market shock

---

## Consumer Sentiment Features

### `ConsumerSentimentMomentum3M`

**Description:**
Three-month change in consumer sentiment.

**Formula / Construction:**
`ConsumerSentimentMomentum3M = ConsumerSentiment(t) - ConsumerSentiment(t-3)`

**Purpose:**
This variable captures whether consumer confidence is improving or deteriorating over the short term.

**Interpretation:**
Positive values mean sentiment improved over the last three months. Negative values mean sentiment weakened.

---

### `ConsumerConfidenceDeterioration`

**Description:**
Six-month deterioration in consumer confidence.

**Formula / Construction:**
`ConsumerConfidenceDeterioration = ConsumerSentimentLag6 - ConsumerSentiment`

**Purpose:**
This variable measures how much consumer sentiment has declined compared with six months earlier.

**Interpretation:**
Higher positive values indicate a larger decline in consumer confidence. Negative values indicate sentiment improved relative to six months earlier.

---

## Lag Features

Lag features preserve historical values of key indicators. They help forecasting models learn delayed relationships between macroeconomic conditions and unemployment.

### `UnemploymentLag1`

**Description:**
Unemployment rate from one month earlier.

**Formula / Construction:**
`UnemploymentLag1 = UnemploymentRate(t-1)`

**Purpose:**
Captures the most recent prior unemployment condition.

---

### `UnemploymentLag3`

**Description:**
Unemployment rate from three months earlier.

**Formula / Construction:**
`UnemploymentLag3 = UnemploymentRate(t-3)`

**Purpose:**
Allows models to learn short-term delayed labor market patterns.

---

### `UnemploymentLag6`

**Description:**
Unemployment rate from six months earlier.

**Formula / Construction:**
`UnemploymentLag6 = UnemploymentRate(t-6)`

**Purpose:**
Captures medium-term unemployment persistence.

---

### `UnemploymentLag12`

**Description:**
Unemployment rate from twelve months earlier.

**Formula / Construction:**
`UnemploymentLag12 = UnemploymentRate(t-12)`

**Purpose:**
Captures year-over-year labor market conditions and longer-term persistence.

---

### `InflationLag3`

**Description:**
Inflation rate from three months earlier.

**Formula / Construction:**
`InflationLag3 = InflationRateYoY(t-3)`

**Purpose:**
Captures delayed effects of inflation pressure on unemployment.

---

### `InflationLag6`

**Description:**
Inflation rate from six months earlier.

**Formula / Construction:**
`InflationLag6 = InflationRateYoY(t-6)`

**Purpose:**
Supports analysis of medium-term inflation effects on the labor market.

---

### `FederalFundsLag3`

**Description:**
Federal funds rate from three months earlier.

**Formula / Construction:**
`FederalFundsLag3 = FederalFundsRate(t-3)`

**Purpose:**
Captures short-term delayed monetary policy effects.

---

### `FederalFundsLag6`

**Description:**
Federal funds rate from six months earlier.

**Formula / Construction:**
`FederalFundsLag6 = FederalFundsRate(t-6)`

**Purpose:**
Captures medium-term delayed effects of monetary policy on unemployment.

---

### `GDPGrowthLag3`

**Description:**
GDP growth from three months earlier.

**Formula / Construction:**
`GDPGrowthLag3 = GDPGrowthYoY(t-3)`

**Purpose:**
Captures delayed relationship between economic growth and unemployment.

---

### `GDPGrowthLag6`

**Description:**
GDP growth from six months earlier.

**Formula / Construction:**
`GDPGrowthLag6 = GDPGrowthYoY(t-6)`

**Purpose:**
Allows models to evaluate whether prior economic growth conditions help explain future unemployment.

---

### `ConsumerSentimentLag3`

**Description:**
Consumer sentiment from three months earlier.

**Formula / Construction:**
`ConsumerSentimentLag3 = ConsumerSentiment(t-3)`

**Purpose:**
Captures delayed sentiment effects on labor market outcomes.

---

### `ConsumerSentimentLag6`

**Description:**
Consumer sentiment from six months earlier.

**Formula / Construction:**
`ConsumerSentimentLag6 = ConsumerSentiment(t-6)`

**Purpose:**
Captures medium-term confidence conditions that may precede labor market changes.

---

## Momentum and Acceleration Features

### `InflationAcceleration`

**Description:**
Month-to-month change in year-over-year inflation.

**Formula / Construction:**
`InflationAcceleration = InflationRateYoY(t) - InflationRateYoY(t-1)`

**Purpose:**
This feature captures whether inflation pressure is rising or falling.

**Interpretation:**
Positive values indicate inflation is accelerating. Negative values indicate inflation is slowing.

---

### `GDPGrowthMomentum`

**Description:**
Three-month change in year-over-year GDP growth.

**Formula / Construction:**
`GDPGrowthMomentum = GDPGrowthYoY(t) - GDPGrowthYoY(t-3)`

**Purpose:**
This variable captures whether economic growth is improving or weakening over a recent period.

**Interpretation:**
Positive values indicate improving growth momentum. Negative values indicate weakening growth momentum.

---

### `MonetaryTighteningIndex`

**Description:**
Six-month change in the federal funds rate.

**Formula / Construction:**
`MonetaryTighteningIndex = FederalFundsRate - FederalFundsLag6`

**Purpose:**
This variable measures how much monetary policy has tightened or loosened over the previous six months.

**Interpretation:**
Positive values indicate monetary tightening. Negative values indicate monetary easing.

---

## Ratio and Pressure Features

### `PolicyPressureScore`

**Description:**
Interaction between monetary policy and inflation.

**Formula / Construction:**
`PolicyPressureScore = FederalFundsRate * InflationRateYoY`

**Purpose:**
This feature captures periods where high inflation and high interest rates occur together.

**Interpretation:**
Higher values indicate stronger combined inflation and policy pressure.

---

### `InflationUnemploymentRatio`

**Description:**
Ratio of inflation to unemployment.

**Formula / Construction:**
`InflationUnemploymentRatio = InflationRateYoY / UnemploymentRate`

**Purpose:**
This feature compares inflation pressure relative to labor market slack.

**Interpretation:**
Higher values indicate inflation is high relative to unemployment. Lower values indicate inflation is weak relative to unemployment.

---

### `GrowthToInflationRatio`

**Description:**
Ratio of GDP growth to inflation.

**Formula / Construction:**
`GrowthToInflationRatio = GDPGrowthYoY / InflationRateYoY`

**Purpose:**
This variable compares real economic growth conditions against inflation pressure.

**Interpretation:**
Higher positive values may indicate strong growth relative to inflation. Negative values may indicate contraction, deflation, or unstable macroeconomic conditions.

**Important Caveat:**
This ratio can become very large when inflation is close to zero. Large values in this column should be interpreted carefully because near-zero denominators can amplify small differences.

---

## Composite Economic Indicators

### `EconomicStressIndex`

**Description:**
Composite indicator designed to summarize overall macroeconomic stress.

**Construction:**
This is a custom engineered index created from multiple macroeconomic signals in the feature engineering script.

**Purpose:**
The variable provides a single summary measure of economic pressure by combining information from labor market, inflation, growth, policy, and sentiment conditions.

**Interpretation:**
Higher values indicate greater economic stress. Lower values indicate more stable or favorable macroeconomic conditions.

---

### `RecessionRiskScore`

**Description:**
Composite score designed to summarize recession-related risk signals.

**Construction:**
This is a custom engineered score created from macroeconomic variables associated with downturn conditions.

**Purpose:**
The variable provides a simplified recession-risk measure for exploratory analysis, visualization, and modeling.

**Interpretation:**
Higher values indicate stronger recession-risk signals. Lower values indicate weaker recession-risk signals.

---

## Forecast Target Variables

These columns are future-looking target variables. They are used for forecasting tasks and should not be used as predictors when training models for the same forecast horizon.

### `FutureUnemployment_3M`

**Description:**
Unemployment rate three months after the current observation.

**Formula / Construction:**
`FutureUnemployment_3M = UnemploymentRate(t+3)`

**Purpose:**
This is a supervised learning target for three-month-ahead unemployment forecasting.

**Interpretation:**
The value represents the unemployment rate observed three months after the current month.

**Missing Values:**
The final three rows are missing because future unemployment values are unavailable for the final three months of the dataset.

---

### `FutureUnemployment_6M`

**Description:**
Unemployment rate six months after the current observation.

**Formula / Construction:**
`FutureUnemployment_6M = UnemploymentRate(t+6)`

**Purpose:**
This is a supervised learning target for six-month-ahead unemployment forecasting.

**Interpretation:**
The value represents the unemployment rate observed six months after the current month.

**Missing Values:**
The final six rows are missing because future unemployment values are unavailable for the final six months of the dataset.

---

### `FutureUnemployment_12M`

**Description:**
Unemployment rate twelve months after the current observation.

**Formula / Construction:**
`FutureUnemployment_12M = UnemploymentRate(t+12)`

**Purpose:**
This is a supervised learning target for twelve-month-ahead unemployment forecasting.

**Interpretation:**
The value represents the unemployment rate observed twelve months after the current month.

**Missing Values:**
The final twelve rows are missing because future unemployment values are unavailable for the final twelve months of the dataset.

---

### `FutureLaborMarketShock_6M`

**Description:**
Binary forecast target indicating whether unemployment increases meaningfully over the next six months.

**Formula / Construction:**
`FutureLaborMarketShock_6M = 1 if FutureUnemployment_6M - UnemploymentRate >= 0.5, else 0`

**Purpose:**
This variable supports classification-style forecasting. Instead of predicting the exact unemployment rate, it identifies whether the labor market is expected to deteriorate by at least 0.5 percentage points over the next six months.

**Interpretation:**

* `1` = unemployment increases by at least 0.5 percentage points within the six-month forecast horizon
* `0` = unemployment does not increase by at least 0.5 percentage points within the six-month forecast horizon

**Modeling Note:**
This is a target variable and should not be used as a predictor when training models to forecast future labor market shocks.

---

## Notes

* The dataset is observational and should not be used to make causal claims.
* GDP originates as quarterly data and is aligned into the monthly analytical panel.
* Outliers caused by real economic events, including recessions and COVID-era labor market disruption, are intentionally retained.
* The dataset is frozen for analysis after Milestone 2.
