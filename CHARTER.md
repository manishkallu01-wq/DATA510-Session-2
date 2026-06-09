# Studio Charter: Forecasting and Explaining U.S. Unemployment Through Macroeconomic Indicators

**Owner team:** Manish R Kallu 

**Owner Product Lead:** Manish R Kallu

**Peer Stakeholder POs:** Brandon Smith, Jon Garrow, Jackson Garro

**Instructor / Sponsor:** Lucas Cordova (`LucasCordova` on GitHub)

**GitHub repo:** https://github.com/manishkallu01-wq/DATA510-Session-2/tree/main

**GitHub Projects board:** https://github.com/users/manishkallu01-wq/projects/1

**Discord category:** https://discord.com/channels/1277725100816203942/1508588739063054376

**Studio Session:** 2

**Studio formed:** 25 May 2026

## Vision

To build a unified, data-driven understanding of how major economic disruptions affect unemployment trends across industries and regions in the United States. If successful, this project will help researchers, policymakers, and job seekers better interpret labor market behavior and economic resilience over time.

## Mission

This semester, the owner team will collect, integrate, and analyze historical U.S. economic datasets to study unemployment patterns using data engineering, visualization, and machine learning techniques. The team will produce forecasting insights, dashboards, and research findings based on public economic indicators.

## Context

- **Users / affected parties:** Economic researchers, workforce analysts, policymakers, businesses monitoring labor trends, students, and job seekers.

- **Data sources (proposed):** FRED API, BLS datasets, U.S. Census Bureau datasets, CPI and inflation indicators, GDP datasets, unemployment datasets, and publicly available government economic APIs. All datasets are publicly accessible and contain minimal or no personally identifiable information (PII).

- **Constraints:** Semester timeline, dataset integration complexity, compute limitations, project scope management, and team coordination.

- **Ethics risks:** Potential bias in historical datasets, fairness concerns in regional comparisons, forecasting misinterpretation, and risk of overclaiming predictive accuracy.

## Success criteria by milestone

- **M1, proposal (W4):** Finalized research questions, approved proposal, identified datasets, and seeded backlog with at least 5 PBIs.

- **M2, data summary (W7):** Working ETL pipeline, integrated datasets, exploratory data analysis, missingness checks, and documented schema validation.

- **M3, poster rough draft (W10):** Initial dashboards, unemployment trend visualizations, and baseline forecasting model results completed.

- **M4, write-up rough draft (W12):** Draft methodology, analysis, visualizations, forecasting evaluation metrics, and findings completed.

- **M5, final write-up and poster (W14):** Final paper, polished poster, reproducible pipelines, dashboards, forecasting outputs, and documented conclusions supported by evidence.

## Working agreements (internal to owner team)

- **Sync rhythm:** One async standup per weekday in Discord and one weekly live sync meeting before class.

- **Code review:** Every major pull request must be reviewed by at least one teammate before merging.

- **Decision rule:** Consensus preferred; unresolved disagreements decided by the Owner Product Lead after discussion.

## Working agreements (triad with peer POs)

- **Studio Brief due:** By 5 PM the day before class, committed to `studio/briefs/` and linked in `#project-studio`.

- **Studio Critique due:** By the end of class or within 24 hours after class if additional review time is needed.

- **Priority conflict resolution:** Owner team integrates peer feedback in good faith; the instructor arbitrates unresolved conflicts if necessary.

## Response SLAs (Service Level Agreements)

A **Service Level Agreement** is a written promise the triad makes about *how fast* each side responds when a specific signal arrives. Every row must have an answer before this Charter is committed. See [Response SLAs](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html#response-slas-service-level-agreements) for the full definition.

| When this signal arrives... | Who responds | By when |
|-----------------------------|--------------|---------|
| Peer PO files a **Studio Brief** (commits to `studio/briefs/...`, links in GitHub Studio) | Owner team | Acknowledge within 24 hours with adopt/defer/decline feedback |
| Peer PO files a **Studio Critique** | Owner team | Respond within 24 hours and add follow-up tasks to backlog if needed |
| Owner team posts an **Iteration Review** in `README.md` | Both peer POs | Review before the next Studio Session |
| Owner team flags a **blocker** in `#project-blockers` | Instructor and tagged peer PO | Respond by the next Studio Session or sooner if urgent |
| Anyone asks a clarifying question in `#project-general` | Whoever is tagged (default: owner team) | Reply within 48 hours |

## Definition of Ready (PBI)

A PBI is ready to be pulled out of `Backlog` and moved into `Create` when it has:

- A one-sentence hypothesis or user story.
- A named **Create**, **Observe**, **Analyze** triple.
- A milestone tag (`M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`).
- A T-shirt size estimate (S, M, L, XL).
- WIP slack on the board: `Create + Observe + Analyze` is below the team's WIP cap (owners + 1).

## Definition of Done (PBI)

A PBI is done, and may be moved from `Analyze` into `Done`, when:

- The Create artifact is in the repo or linked from the issue.
- The Observe results are recorded somewhere referenceable (notebook output, processed dataset, draft results section).
- The Analyze writeup names a next step (continue, pivot, kill, or decompose into new PBIs).
- A peer PO has either signed off in `#<project>-studio` or filed a Studio Critique covering it.
- The card is linked under *Completed PBIs* in the next Iteration Review in `README.md`.

## Context map

> Optional. Replace this block with a Mermaid `flowchart LR` showing how users, data, constraints, and ethics risks flow into the owner team and out to the capstone outcome. See the [`charter-inception.qmd` template](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html) for a starting Mermaid diagram.

## Stakeholder alignment memo (one-page summary)

### Why we exist

This project exists to improve understanding of how economic disruptions influence unemployment trends across industries and regions in the United States. The team aims to create integrated economic datasets, forecasting models, and visualizations that support labor market analysis and economic research.

### What we will deliver to peer POs every week

- An Iteration Review update in `README.md`
- Progress summaries and backlog updates
- Adopt/defer/decline decisions for Studio Brief feedback

### What we need from peer POs every week

- A Studio Brief before class with questions, risks, or requirements
- A Studio Critique after class evaluating project progress and deliverables

### How to reach us

- **Discord category:** [`project-general`](https://discord.com/channels/1277725100816203942/1508588739063054376), [`project-studio`](https://discord.com/channels/1277725100816203942/1508588756880461834), [`project-blockers`](https://discord.com/channels/1277725100816203942/1508588778426597466)
- **GitHub repo:** https://github.com/manishkallu01-wq/DATA510-Session-2/tree/main
- **GitHub Projects board:** https://github.com/users/manishkallu01-wq/projects/1
