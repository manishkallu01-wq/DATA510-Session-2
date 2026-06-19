import pandas as pd
from pathlib import Path

# =========================
# 1. Load dataset
# =========================

file_path = Path.home() / "Downloads" / "capstone_capstone_plus_final.csv"

df = pd.read_csv(file_path)

print("\n✅ File loaded successfully")
print(f"File path: {file_path}")

# =========================
# 2. Basic shape checks
# =========================

print("\n==============================")
print("BASIC DATASET INFO")
print("==============================")

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn names:")
for col in df.columns:
    print(f"- {col}")

# =========================
# 3. Date checks
# =========================

print("\n==============================")
print("DATE CHECKS")
print("==============================")

date_col = None

for col in df.columns:
    if col.lower() in ["date", "observation_date", "month"]:
        date_col = col
        break

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    print(f"Date column detected: {date_col}")
    print(f"Start date: {df[date_col].min()}")
    print(f"End date: {df[date_col].max()}")
    print(f"Duplicate dates: {df[date_col].duplicated().sum()}")
    print(f"Missing dates: {df[date_col].isna().sum()}")

    expected_months = pd.date_range(
        start=df[date_col].min(),
        end=df[date_col].max(),
        freq="MS"
    )

    actual_months = pd.to_datetime(df[date_col]).dt.to_period("M").dt.to_timestamp()
    missing_months = sorted(set(expected_months) - set(actual_months))

    print(f"Expected monthly periods: {len(expected_months)}")
    print(f"Missing monthly periods: {len(missing_months)}")

    if missing_months:
        print("Missing months:")
        for m in missing_months[:20]:
            print(m.strftime("%Y-%m"))
else:
    print("⚠️ No date column detected")

# =========================
# 4. Duplicate checks
# =========================

print("\n==============================")
print("DUPLICATE CHECKS")
print("==============================")

print(f"Duplicate rows: {df.duplicated().sum()}")

# =========================
# 5. Missing value checks
# =========================

print("\n==============================")
print("MISSING VALUE CHECKS")
print("==============================")

missing = df.isna().sum()
missing = missing[missing > 0]

if missing.empty:
    print("✅ No missing values found")
else:
    print("Columns with missing values:")
    print(missing)

# =========================
# 6. Infinite value checks
# =========================

print("\n==============================")
print("INFINITE VALUE CHECKS")
print("==============================")

numeric_df = df.select_dtypes(include="number")

inf_count = numeric_df.apply(lambda x: x.isin([float("inf"), float("-inf")]).sum())
inf_count = inf_count[inf_count > 0]

if inf_count.empty:
    print("✅ No infinite values found")
else:
    print("Columns with infinite values:")
    print(inf_count)

# =========================
# 7. Required source variable checks
# =========================

print("\n==============================")
print("REQUIRED SOURCE VARIABLE CHECKS")
print("==============================")

required_keywords = [
    "Unemployment",
    "Inflation",
    "FederalFunds",
    "GDP",
    "ConsumerSentiment",
    "Recession"
]

for keyword in required_keywords:
    matches = [col for col in df.columns if keyword.lower() in col.lower()]
    if matches:
        print(f"✅ {keyword}: {matches}")
    else:
        print(f"❌ {keyword}: NOT FOUND")

# =========================
# 8. Forecast target checks
# =========================

print("\n==============================")
print("FORECAST TARGET CHECKS")
print("==============================")

forecast_targets = [
    "FutureUnemployment_3M",
    "FutureUnemployment_6M",
    "FutureUnemployment_12M"
]

for target in forecast_targets:
    if target in df.columns:
        print(f"✅ {target} found | Missing values: {df[target].isna().sum()}")
    else:
        print(f"❌ {target} missing")

# =========================
# 9. Engineered feature checks
# =========================

print("\n==============================")
print("ENGINEERED FEATURE CHECKS")
print("==============================")

engineered_keywords = [
    "Lag",
    "Growth",
    "Momentum",
    "Change",
    "Shock",
    "Stress",
    "Pressure",
    "Risk",
    "Acceleration",
    "Deterioration",
    "RealInterest"
]

engineered_cols = []

for col in df.columns:
    if any(keyword.lower() in col.lower() for keyword in engineered_keywords):
        engineered_cols.append(col)

print(f"Detected engineered features: {len(engineered_cols)}")

for col in engineered_cols:
    print(f"- {col}")

# =========================
# 10. Numeric summary
# =========================

print("\n==============================")
print("NUMERIC SUMMARY")
print("==============================")

print(numeric_df.describe().T)

# =========================
# 11. Proposal consistency check
# =========================

print("\n==============================")
print("PROPOSAL CONSISTENCY CHECK")
print("==============================")

expected_rows = 838
expected_cols = 40

if df.shape[0] == expected_rows:
    print(f"✅ Row count matches proposal: {expected_rows}")
else:
    print(f"⚠️ Row count mismatch: expected {expected_rows}, found {df.shape[0]}")

if df.shape[1] == expected_cols:
    print(f"✅ Column count matches proposal: {expected_cols}")
else:
    print(f"⚠️ Column count mismatch: expected {expected_cols}, found {df.shape[1]}")

print("\n✅ Dataset validation checks completed")