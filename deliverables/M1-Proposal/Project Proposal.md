# Forecasting U.S. Unemployment Using Macroeconomic Indicators

## A Data Engineering, Statistical Analysis, and Machine Learning Project

**Author:** Manish R. Kallu  
**Program:** DATA 510 Capstone Project  
**Institution:** Willamette University  
**Term:** Summer 2026

---

# Project Stakeholders

## Project Owner

- Manish R. Kallu

## Peer Stakeholder Product Owners

- Brandon Smith
- Jon Garrow
- Jackson Garro

## Instructor / Sponsor

- Lucas P. Cordova, Ph.D.

---

# Project Resources

## GitHub Repository

https://github.com/manishkallu01-wq/DATA510-Session-2/tree/main

## GitHub Project Board

https://github.com/users/manishkallu01-wq/projects/1

---

# 1. Problem Framing and Research Motivation

## 1.1 Background

The unemployment rate is one of the most important indicators used to evaluate the health of the United States economy. Government agencies, businesses, investors, workforce development organizations, researchers, and job seekers rely on labor market information to understand economic conditions and support decision-making.

Changes in unemployment influence:

- Hiring activity
- Workforce planning
- Consumer confidence
- Business investment
- Economic policy decisions

The original concept for this project focused on analyzing historical unemployment trends in the United States. During the charter and proposal development phases, publicly available datasets and academic literature were reviewed to evaluate whether a more consequential and analytically rigorous research problem could be addressed using available economic data.

The investigation revealed that unemployment is influenced by multiple macroeconomic forces, including:

- Inflation
- Monetary policy
- Economic growth
- Consumer sentiment
- Recessionary conditions

Prior research suggests that these indicators often provide useful information regarding future labor market outcomes and may improve forecasting performance when incorporated into predictive models.

---

## 1.2 Why This Problem Matters

Labor market conditions affect millions of individuals, businesses, and institutions across the United States.

Stakeholders include:

- Policymakers
- Employers
- Workforce organizations
- Researchers
- Job seekers

Although unemployment is widely monitored, it is generally considered a lagging indicator because labor market deterioration often becomes visible only after broader economic conditions have already changed.

This project investigates whether macroeconomic indicators can provide earlier signals regarding future unemployment conditions.

---

## 1.3 Literature Review

### Barnichon (2013)

Demonstrated that labor market dynamics improve unemployment forecasting performance compared to models relying exclusively on historical unemployment observations.

### Howrey (2001)

Found that consumer sentiment contains useful information regarding future economic activity and expectations.

### Chung et al. (2014)

Emphasized the importance of evaluating labor market conditions using multiple indicators rather than relying solely on unemployment statistics.

### Favara et al. (2022)

Demonstrated that financial and macroeconomic indicators contain valuable information regarding future economic conditions and recession risk.

---

## 1.4 Research Gap

Existing studies often:

- Focus on limited indicator sets
- Examine specific economic periods
- Emphasize forecasting performance
- Provide limited discussion of reproducible data engineering workflows

This project addresses these limitations by integrating six macroeconomic datasets spanning nearly seventy years of U.S. economic history into a unified analytical framework.

---

## 1.5 Research Questions

### Primary Research Question

> To what extent can publicly available macroeconomic indicators improve forecasting of future U.S. unemployment across 3-month, 6-month, and 12-month forecasting horizons?

### Secondary Research Question

> Which macroeconomic indicators demonstrate the strongest and most consistent historical relationships with unemployment across U.S. economic cycles between 1956 and 2025?

---

# 2. Data Sources

| Dataset | Source | Frequency |
|----------|----------|----------|
| UNRATE | Bureau of Labor Statistics | Monthly |
| CPIAUCSL | Bureau of Labor Statistics | Monthly |
| FEDFUNDS | Federal Reserve | Monthly |
| GDP | Bureau of Economic Analysis | Quarterly |
| UMCSENT | University of Michigan | Monthly |
| USREC | NBER | Monthly |

---

# 3. Data Engineering Plan

## Data Acquisition

Economic indicators are sourced from FRED.

## Data Standardization

Activities include:

- Date normalization
- Schema standardization
- Frequency alignment
- Variable naming consistency

## Data Integration

Activities include:

- Time-based joins
- Frequency reconciliation
- Historical alignment
- Cross-source validation

---

# 4. Feature Engineering

## Inflation Features

- InflationRateYoY
- InflationAcceleration
- InflationLag3
- InflationLag6

## Labor Market Features

- UnemploymentChange1M
- UnemploymentChange3M
- UnemploymentMomentum
- LaborMarketShock

## Economic Growth Features

- GDPGrowthYoY
- GDPGrowthMomentum
- GDPGrowthLag3
- GDPGrowthLag6

## Monetary Policy Features

- RealInterestRate
- MonetaryTighteningIndex
- FederalFundsLag3
- FederalFundsLag6

---

# 5. Machine Learning Approach

## Forecast Horizons

- 3 Months
- 6 Months
- 12 Months

## Candidate Models

### Linear Regression

Baseline model.

### Random Forest

Captures nonlinear relationships.

### XGBoost

High-performance gradient boosting framework.

---

# 6. Evaluation Metrics

- RMSE
- MAE
- R²

---

# 7. Expected Deliverables

- Integrated analytical dataset
- Statistical analysis
- Forecasting models
- Dashboard visualizations
- Final report
- Poster presentation

---

# References

Barnichon, R. (2013). Using labor force flows to forecast the labor market.

Chung, H., Fallick, B., Nekarda, C. J., & Ratner, D. (2014). Assessing the change in labor market conditions.

Favara, G., Gilchrist, S., Lewis, K., & Zakrajšek, E. (2022). Recession risk and the excess bond premium.

Howrey, E. P. (2001). Consumer sentiment and economic forecasting.
