import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

# =====================================================
# LOAD DATASET
# =====================================================

DOWNLOADS = Path.home() / "Downloads"

INPUT_FILE = DOWNLOADS / "capstone_dataset.csv"

OUTPUT_FILE = (
    DOWNLOADS /
    "capstone_dataset_feature_engineered.csv"
)

df = pd.read_csv(INPUT_FILE)

df["observation_date"] = pd.to_datetime(
    df["observation_date"]
)

df = df.sort_values(
    "observation_date"
)

# =====================================================
# DERIVED ECONOMIC FEATURES
# =====================================================

# -----------------------------
# Inflation Rate (YoY)
# -----------------------------

df["INFLATION_YOY"] = (
    (
        df["CPIAUCSL"]
        - df["CPIAUCSL"].shift(12)
    )
    /
    df["CPIAUCSL"].shift(12)
) * 100

# -----------------------------
# GDP Growth (YoY)
# -----------------------------

df["GDP_GROWTH_YOY"] = (
    (
        df["GDP"]
        - df["GDP"].shift(12)
    )
    /
    df["GDP"].shift(12)
) * 100

# -----------------------------
# Unemployment Change
# -----------------------------

df["UNRATE_CHANGE_1M"] = (
    df["UNRATE"]
    .diff(1)
)

# -----------------------------
# 3 Month Change
# -----------------------------

df["UNRATE_CHANGE_3M"] = (
    df["UNRATE"]
    .diff(3)
)

# -----------------------------
# Consumer Sentiment Momentum
# -----------------------------

df["UMCSENT_MOMENTUM_3M"] = (
    df["UMCSENT"]
    -
    df["UMCSENT"].shift(3)
)

# -----------------------------
# Real Interest Rate
# -----------------------------

df["REAL_INTEREST_RATE"] = (
    df["FEDFUNDS"]
    -
    df["INFLATION_YOY"]
)

# =====================================================
# LAG FEATURES
# =====================================================

for lag in [1, 3, 6, 12]:

    df[f"UNRATE_LAG_{lag}"] = (
        df["UNRATE"]
        .shift(lag)
    )

for lag in [3, 6]:

    df[f"CPI_LAG_{lag}"] = (
        df["INFLATION_YOY"]
        .shift(lag)
    )

    df[f"FEDFUNDS_LAG_{lag}"] = (
        df["FEDFUNDS"]
        .shift(lag)
    )

    df[f"GDP_LAG_{lag}"] = (
        df["GDP_GROWTH_YOY"]
        .shift(lag)
    )

    df[f"UMCSENT_LAG_{lag}"] = (
        df["UMCSENT"]
        .shift(lag)
    )

# =====================================================
# ECONOMIC STRESS INDEX
# =====================================================

stress_features = [
    "UNRATE",
    "INFLATION_YOY",
    "FEDFUNDS"
]

temp = df[stress_features].copy()

temp = temp.dropna()

scaler = StandardScaler()

scaled = scaler.fit_transform(temp)

df.loc[
    temp.index,
    "ECONOMIC_STRESS_INDEX"
] = scaled.mean(axis=1)

# =====================================================
# LABOR MARKET SHOCK FLAG
# =====================================================

df["LABOR_MARKET_SHOCK"] = 0

df.loc[
    df["UNRATE_CHANGE_3M"] >= 0.5,
    "LABOR_MARKET_SHOCK"
] = 1

# =====================================================
# DROP INITIAL ROWS
# =====================================================

df = df.dropna().reset_index(drop=True)

# =====================================================
# SAVE
# =====================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

# =====================================================
# REPORT
# =====================================================

print("\nFEATURE ENGINEERING COMPLETE")
print("=" * 60)

print("\nRows:")
print(len(df))

print("\nColumns:")
print(len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDate Range:")
print(
    df["observation_date"].min(),
    "to",
    df["observation_date"].max()
)

print("\nOutput:")
print(OUTPUT_FILE)
