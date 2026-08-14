# 📓 Notebooks Directory

No notebooks are part of the submitted final reproducibility path in this repository. This folder is retained only as a documented location for exploratory work if future analysis is added.

## ✅ Authoritative Analysis Locations

| Task | Authoritative location |
| --- | --- |
| Dataset reconstruction and validation | [`../src/`](../src/) |
| Final machine-learning analysis | [`../deliverables/M5-final/ML Analysis.py`](../deliverables/M5-final/ML%20Analysis.py) |
| Final RQ2 correlation analysis | [`../deliverables/M5-final/Correlation analysis.py`](../deliverables/M5-final/Correlation%20analysis.py) |
| Submitted processed dataset | [`../data/processed/capstone_plus_final.xlsx`](../data/processed/capstone_plus_final.xlsx) |
| Final report, poster, results, and figures | [`../deliverables/M5-final/`](../deliverables/M5-final/) |

Readers do not need a notebook to reproduce or inspect the submitted results.

## 🧭 Future Notebook Conventions

If notebooks are added later:

- use one notebook for one clearly stated analytical question;
- preserve chronological ordering for time-series work;
- restart and run all cells before sharing;
- move reusable construction logic into `../src/`;
- do not duplicate the final ML or correlation scripts;
- write generated outputs locally unless a maintainer intentionally versions a reviewed artifact; and
- document any changed data, feature, package, seed, or model configuration as a new analysis version.

Return to the [project README](../README.md) for the supported workflows.
