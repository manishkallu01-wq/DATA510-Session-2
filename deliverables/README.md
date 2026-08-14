# 📦 Project Deliverables

The deliverables are organized by DATA 510 milestone. Each folder preserves the work submitted at that stage of the project.

## 🗂️ Milestone Index

| Folder | Stage | Primary contents | Status |
| --- | --- | --- | --- |
| [`M1-Proposal/`](M1-Proposal/) | Project proposal | Proposal PDF and Markdown source | ✅ Complete |
| [`M2-data-summary/`](M2-data-summary/) | Data summary | Milestone narrative and historical construction scripts | ✅ Complete |
| [`M3-poster-draft/`](M3-poster-draft/) | Poster draft | 48 x 36 draft poster PDF | ✅ Complete |
| [`M4-writeup-draft/`](M4-writeup-draft/) | Write-up draft | Draft PDFs, Quarto source, and references | ✅ Complete |
| [`M5-final/`](M5-final/) | Final submission | Final report, poster, analysis scripts, result tables, and figures | ✅ Complete |

## Final Record

Use [`M5-final/M5-Final-Report.pdf`](M5-final/M5-Final-Report.pdf) for the final conclusions, metrics, model-selection rule, RQ2 findings, limitations, and reproducibility statement.

Earlier milestone folders preserve work at that point in the course. Their preliminary wording, filenames, dataset counts, planned methods, or results must not override the final report.

## 🏆 Final Results Snapshot

| Horizon | Selected model | Test MAE | Test RMSE | Test R² |
| --- | --- | ---: | ---: | ---: |
| 3 months | Ridge Regression | 0.349 | 1.020 | 0.720 |
| 6 months | Extra Trees | 0.725 | 1.277 | 0.563 |
| 12 months | Extra Trees | 1.195 | 1.729 | 0.205 |

Consumer sentiment was the strongest overall external historical relationship with unemployment, reaching Pearson `r = -0.496` at twelve months. Its six-month relationship reversed to `+0.67` during 2020-2025, so the final period is interpreted cautiously as possible regime instability.

## 🔁 Reproducibility Boundary

- Optional dataset reconstruction and validation: [`../src/`](../src/)
- Submitted processed input: [`../data/processed/capstone_plus_final.xlsx`](../data/processed/capstone_plus_final.xlsx)
- Final ML and correlation scripts: [`M5-final/`](M5-final/)
- Public portfolio: [capstone project page](https://manishkallu01-wq.github.io/capstone.html)

All public artifacts can be inspected or downloaded without GitHub write access.
