# CortexCall — EEG Motor Imagery Classification

> **Project Goal:** Classify whether a subject is imagining **LEFT** or **RIGHT** hand movement using raw EEG signals only (no physical movement).
> **Target Audience:** Research team + assistive-technology demo.

---

## 📅 Week 1 Focus: Exploratory Data Analysis (EDA)

We are analyzing **~2,000 raw EEG trial files** (Excel/CSV) and a master labels sheet to determine signal quality, class balance, and time-frequency behavior.

> ⚠️ **IMPORTANT:** **DO NOT** perform final data cleaning or filtering this week. EDA will inform the preprocessing rules, epoch windows, and band-pass frequencies implemented in Week 2.

---

## 📁 Repository Structure

```text
cortex-call/
├── data/                    # Local raw & processed data (Gitignored)
├── src/                     # Shared codebase
│   ├── data_loader.py       # Shared loader script
│   └── config.py            # Global pipeline configuration
├── notebooks/               # Task-specific notebooks & summary
│   ├── eda_person_a.ipynb   # Data usability, balance & completeness
│   ├── eda_person_b.ipynb   # Time-domain waveform analysis (C3/C4)
│   ├── eda_person_c.ipynb   # PSD & ERD frequency analysis
│   ├── eda_person_d.ipynb   # Artifact & outlier distribution statistics
│   └── eda_summary.md       # Converged conclusions & decisions
├── models/                  # Saved weights (.pt, .pkl - Gitignored)
├── app/                     # Streamlit web demo (Deployment stage)
└── reports/                 # Final reports, presentation slides, figures

```
## Rules

- Everyone imports `data_loader.py` — nobody rewrites loading logic.
- All 4 notebooks work in parallel, no one waits on anyone else.
- Any filtering inside a notebook is exploratory only (just to look) —
  it's not a final decision and doesn't affect the shared data or other
  notebooks.
- Findings go into `eda_summary.md` once everyone's done — this becomes
  the source of truth for next week's actual cleaning pipeline.

## Goal by end of week

Know whether the data shows a real LEFT vs RIGHT difference (mainly on
C3/C4, 8–30 Hz), and have enough evidence to choose filter band, epoch
window, and rejection rules for next week.