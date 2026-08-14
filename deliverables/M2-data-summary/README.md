# 🗃️ M2 - Data Summary

This folder preserves the completed data-summary milestone. It documents the project's intermediate data inventory, integration plan, quality review, and early reconstruction code as they existed at M2.

## 📁 Artifacts

| File | Purpose |
| --- | --- |
| [`data-summary.md`](data-summary.md) | Milestone data inventory, schema discussion, quality assessment, ethics, and freeze statement |
| [`rebuild.py`](rebuild.py) | Historical M2 reconstruction script |
| [`eng_variables.py`](eng_variables.py) | Historical M2 feature-engineering script |
| [`checks.py`](checks.py) | Historical M2 validation script |

## ⚠️ Historical Snapshot

The scripts and counts in this folder are retained for milestone traceability. They are not the supported final reconstruction workflow and may contain preliminary filenames, paths, row counts, or validation expectations.

Do not use the M2 copies to override later work.

## ✅ Final Data Specification

| Attribute | Final value |
| --- | --- |
| Common input | `data/processed/capstone_plus_final.xlsx` |
| Study period | April 1956-December 2025 |
| Rows | 837 |
| Columns | 40 |
| Predictors | 35 |
| Duplicate dates | 0 |
| Infinite values | 0 |
| Unexpected missing predictors | 0 |

The only intentional missing unemployment targets are the final 3, 6, and 12 observations for the corresponding forecast horizons.

## 🔁 Supported Current Workflow

Use the maintained scripts in [`../../src/`](../../src/):

1. `src/rebuild.py` reads [`../../data/raw/`](../../data/raw/) and exports a local `super_dataset.csv`.
2. `src/eng_variables.py` engineers and exports a local `capstone_plus_final.xlsx`.
3. `src/checks.py` validates that local final workbook.

Generated files default to the user's local `Downloads` folder and are not written or pushed to the repository.

For submitted analyses and final conclusions, use [`../M5-final/`](../M5-final/) and the [root README](../../README.md).
