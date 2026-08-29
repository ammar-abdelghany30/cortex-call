# CortexCall — EEG Motor Imagery Classification

> **Project Goal:** Classify whether a subject is imagining **LEFT** or **RIGHT** hand movement using raw EEG signals only (no physical movement).
>
> **Target Audience:** Research team + assistive-technology demo.

---

## 📅 Week 1 Focus: Exploratory Data Analysis (EDA)

We are analyzing **2,160 raw EEG Motor Imagery trials** to evaluate dataset quality, class balance, signal characteristics, artifacts, and time-frequency behavior before designing the final preprocessing pipeline.

The raw EEG files follow the naming convention:

```text
cellula_MI_data_1.csv
cellula_MI_data_2.csv
...
cellula_MI_data_2160.csv
```

Initial dataset validation confirmed:

* **2,160 EEG CSV files**
* Trial IDs are continuous from **1 to 2160**
* **No missing trial IDs**
* **No duplicate trial IDs**
* `labels.csv` originally contains **2,400 labels**
* The final **240 extra labels are intentionally discarded**, as confirmed with the project instructor
* The resulting dataset contains **2,160 aligned EEG trial-label pairs**
* Target labels are standardized to `left` and `right`
* The shared `DataLoader` successfully loads individual EEG trials and their corresponding labels
* The first inspected trial has shape `(2500, 5)`; consistency across all trials will be verified during EDA

> ⚠️ **IMPORTANT:** Do **not** perform final data cleaning or filtering during the EDA phase. EDA findings will determine the preprocessing rules, epoch windows, artifact-rejection criteria, and band-pass frequencies implemented in Week 2.

---

## 🔗 Data Loading & Alignment

All team members use the shared `src/data_loader.py`.

The loader:

1. Discovers all EEG CSV files.
2. Extracts the numeric trial ID from each filename.
3. Sorts EEG files numerically by trial ID.
4. Loads the master labels file.
5. Removes the confirmed 240 trailing extra labels.
6. Standardizes labels to `left` / `right`.
7. Creates a one-to-one manifest between EEG trials and labels.
8. Provides individual trial loading for EDA and later pipeline stages.

Conceptually:

```text
cellula_MI_data_1.csv    ──→ Trial 1    ──→ left/right
cellula_MI_data_2.csv    ──→ Trial 2    ──→ left/right
...
cellula_MI_data_2160.csv ──→ Trial 2160 ──→ left/right
```

This shared loader is the single source of truth for dataset alignment.

---

## 📁 Repository Structure

```text
cortex-call/
├── data/                    # Local raw & processed data (Gitignored)
│   ├── labels.csv
│   └── MI CSV/              # 2160 raw EEG trials
│
├── src/                     # Shared codebase
│   ├── data_loader.py       # EEG discovery, label alignment & trial loading
│   ├── check_eeg_files.py   # Raw EEG filename/numbering validation
│   └── config.py            # Global pipeline configuration
│
├── notebooks/               # Task-specific EDA notebooks & summary
│   ├── eda_a.ipynb   # Data usability, balance & completeness
│   ├── eda_b.ipynb   # Time-domain waveform analysis (C3/C4)
│   ├── eda_c.ipynb   # PSD & ERD frequency analysis
│   ├── eda_d.ipynb   # Artifact & outlier distribution statistics
│   └── eda_summary.md       # Converged conclusions & preprocessing decisions
│
├── models/                  # Saved weights (.pt, .pkl - Gitignored)
├── app/                     # Streamlit web demo (deployment stage)
└── reports/                 # Reports, documentation, figures & presentations
```

---

## 📋 EDA Rules

* Everyone imports and uses `src/data_loader.py` — **do not rewrite dataset alignment logic inside individual notebooks**.
* EDA notebooks can work in parallel.
* Raw data remains unchanged.
* Any filtering performed inside an EDA notebook is **exploratory only**.
* Do not permanently remove trials, channels, or samples during EDA without evidence.
* Do not assume all trials have identical dimensions until this is verified across the complete dataset.
* Record important anomalies and observations rather than silently correcting them.
* Final findings from all EDA tasks are consolidated into `eda_summary.md`.
* `eda_summary.md` becomes the source of truth for designing the Week 2 cleaning and preprocessing pipeline.

---

## 🎯 Goal by End of EDA phase

By the end of EDA, we should understand:

* Whether all **2,160 trials** are structurally usable
* Whether trial lengths and EEG channels are consistent
* LEFT vs RIGHT class balance
* Missing, invalid, or extreme signal values
* EEG amplitude distributions and potential artifacts
* Time-domain behavior, particularly around **C3/C4**
* Frequency-domain behavior and relevant motor-imagery activity
* Whether meaningful LEFT vs RIGHT differences appear, particularly in the **8–30 Hz** motor-related frequency range
* Which trials/artifacts may require rejection
* Which frequency band(s) should be retained
* Which epoch/time window should be used

These findings will determine the **cleaning, filtering, artifact rejection, epoching, and preprocessing rules** used in the next stage.

---

## ✅ Current Project Status

```text
Raw Dataset
    │
    ▼
EEG File Inspection              ✓
    │
    ├── 2160 files
    ├── IDs 1–2160
    ├── No missing IDs
    └── No duplicate IDs
    │
    ▼
Label Validation                 ✓
    │
    ├── 2400 original labels
    └── 240 confirmed extras removed
    │
    ▼
Data Loader & Alignment          ✓
    │
    └── 2160 EEG-label pairs
    │
    ▼
Exploratory Data Analysis        
    │
    ▼
Cleaning & EEG Preprocessing    ← CURRENT PHASE
    │
    ▼
Feature Engineering / Modeling
    │
    ▼
LEFT / RIGHT Classification
```
