# 🛠️ Dataset Reconstruction Scripts

Use these scripts only to reconstruct and validate the dataset. The submitted machine-learning and Research Question 2 analyses are kept separately in `deliverables/M5-final/`.

## 📁 Scripts

| Script | Reads | Produces | Responsibility |
| --- | --- | --- | --- |
| [`rebuild.py`](rebuild.py) | Six CSV files in [`../data/raw/`](../data/raw/) | Local `~/Downloads/super_dataset.csv` | Parse, align, and merge the approved macroeconomic series |
| [`eng_variables.py`](eng_variables.py) | Local `super_dataset.csv` | Local `~/Downloads/capstone_plus_final.xlsx` | Engineer the final 40-column schema and future targets |
| [`checks.py`](checks.py) | Local `capstone_plus_final.xlsx` | Validation messages only | Check shape, date sequence, duplicates, infinities, predictor completeness, and target missingness |

## ▶️ Default Workflow

Run these commands from the repository root:

```bash
python src/rebuild.py
python src/eng_variables.py
python src/checks.py
```

The expected local reconstruction is:

- `super_dataset.csv`: 858 rows x 7 columns, July 1954-December 2025
- `capstone_plus_final.xlsx`: 837 rows x 40 columns, April 1956-December 2025
- final validation: 35 predictors, no duplicate dates, no infinite values, no unexpected missing predictors, and intentional future-target gaps

Use `--raw-dir`, `--input`, or `--output` when a different local path is required.

## 🔒 Local Outputs and Repository Access

The repository supplies the source files and scripts. By default, reconstructed datasets are written to the user's `Downloads` folder, not to `data/processed/` or any other repository path.

These scripts do not invoke Git, create commits, push branches, or upload files. Public users need only read and download repository content; GitHub write access is not required.

## 🧪 Final Analysis Code

The submitted analyses are stored separately:

- [`../deliverables/M5-final/ML Analysis.py`](../deliverables/M5-final/ML%20Analysis.py) performs the six-model forecasting comparison.
- [`../deliverables/M5-final/Correlation analysis.py`](../deliverables/M5-final/Correlation%20analysis.py) performs the separate RQ2 lead-lag and historical-period correlation analysis.

Both final scripts use the submitted [`../data/processed/capstone_plus_final.xlsx`](../data/processed/capstone_plus_final.xlsx) as their common input.

See the [root README](../README.md) for the final model-selection rule, results, findings, and limitations.
