import pandas as pd
from pathlib import Path

# =====================================================
# CONFIGURATION
# =====================================================

DOWNLOADS = Path.home() / "Downloads"

FILES = {
    "UNRATE": DOWNLOADS / "UNRATE.csv",
    "CPIAUCSL": DOWNLOADS / "CPIAUCSL.csv",
    "FEDFUNDS": DOWNLOADS / "FEDFUNDS.csv",
    "GDP": DOWNLOADS / "GDP.csv",
    "UMCSENT": DOWNLOADS / "UMCSENT.csv",
    "USREC": DOWNLOADS / "USREC.csv"
}

# =====================================================
# LOAD FRED FILE
# =====================================================

def load_fred(file_path, metric_name):

    df = pd.read_csv(file_path)

    df.columns = [c.strip() for c in df.columns]

    df.rename(
        columns={
            df.columns[0]: "observation_date",
            df.columns[1]: metric_name
        },
        inplace=True
    )

    df["observation_date"] = pd.to_datetime(
        df["observation_date"],
        errors="coerce"
    )

    df[metric_name] = pd.to_numeric(
        df[metric_name],
        errors="coerce"
    )

    df = (
        df
        .drop_duplicates(subset=["observation_date"])
        .sort_values("observation_date")
        .reset_index(drop=True)
    )

    return df

# =====================================================
# LOAD DATASETS
# =====================================================

print("Loading datasets...")

unrate = load_fred(FILES["UNRATE"], "UNRATE")
cpi = load_fred(FILES["CPIAUCSL"], "CPIAUCSL")
fedfunds = load_fred(FILES["FEDFUNDS"], "FEDFUNDS")
gdp = load_fred(FILES["GDP"], "GDP")
umcsent = load_fred(FILES["UMCSENT"], "UMCSENT")
usrec = load_fred(FILES["USREC"], "USREC")

# =====================================================
# GDP QUARTERLY TO MONTHLY
# =====================================================

print("Converting GDP quarterly data to monthly...")

gdp = gdp.set_index("observation_date")

monthly_dates = pd.date_range(
    start=gdp.index.min(),
    end=gdp.index.max(),
    freq="MS"
)

gdp = gdp.reindex(monthly_dates)

gdp.index.name = "observation_date"

gdp["GDP"] = gdp["GDP"].ffill()

gdp = gdp.reset_index()

# =====================================================
# MERGE USING UNRATE AS MASTER
# =====================================================

print("Merging datasets...")

master = unrate.copy()

master = master.merge(
    cpi,
    how="left",
    on="observation_date"
)

master = master.merge(
    fedfunds,
    how="left",
    on="observation_date"
)

master = master.merge(
    gdp,
    how="left",
    on="observation_date"
)

master = master.merge(
    umcsent,
    how="left",
    on="observation_date"
)

master = master.merge(
    usrec,
    how="left",
    on="observation_date"
)

# =====================================================
# CLEANING
# =====================================================

master = master.sort_values(
    "observation_date"
)

master["GDP"] = master["GDP"].ffill()

master["FEDFUNDS"] = master["FEDFUNDS"].ffill()

master["UMCSENT"] = master["UMCSENT"].ffill()

master["USREC"] = (
    master["USREC"]
    .ffill()
    .fillna(0)
)

master = master.dropna(
    subset=[
        "UNRATE",
        "CPIAUCSL"
    ]
)

master = master.reset_index(drop=True)

# =====================================================
# SAVE FULL DATASET
# =====================================================

full_output = DOWNLOADS / "capstone_final_clean.csv"

master.to_csv(
    full_output,
    index=False
)

# =====================================================
# CREATE MODELING DATASET
# =====================================================

model_df = master.dropna(
    subset=[
        "FEDFUNDS",
        "UMCSENT"
    ]
).copy()

model_df.reset_index(
    drop=True,
    inplace=True
)

model_output = DOWNLOADS / "capstone_modeling_dataset.csv"

model_df.to_csv(
    model_output,
    index=False
)

# =====================================================
# QUALITY REPORT
# =====================================================

print("\n" + "=" * 60)
print("FULL DATASET")
print("=" * 60)

print(f"Rows: {len(master)}")
print(f"Columns: {len(master.columns)}")

print("\nDate Range:")
print(
    master["observation_date"].min(),
    "to",
    master["observation_date"].max()
)

print("\nMissing Values:")
print(master.isnull().sum())

print("\nUSREC Distribution:")
print(master["USREC"].value_counts())

print("\nDuplicate Dates:")
print(
    master["observation_date"]
    .duplicated()
    .sum()
)

print("\nSaved:")
print(full_output)

print("\n" + "=" * 60)
print("MODELING DATASET")
print("=" * 60)

print(f"Rows: {len(model_df)}")

print("\nDate Range:")
print(
    model_df["observation_date"].min(),
    "to",
    model_df["observation_date"].max()
)

print("\nSaved:")
print(model_output)

print("\nSUCCESS")
