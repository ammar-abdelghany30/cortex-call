# CortexCall — EDA Phase (Week 1)

## What we're doing this week

Exploring ~2000 raw EEG trial files (LEFT vs RIGHT hand imagery) to answer
one core question: **is this data usable, and what does it look like?**

We are NOT cleaning or filtering the data yet. That happens next week,
once EDA gives us real answers to base those decisions on.

## Structure
src/
data_loader.py # shared — loads files, standardizes columns,
# attaches labels, checks sampling rate.
# No filtering or cleaning here.

notebooks/
eda_person_a.ipynb # data usability: class balance, consistency, NaNs
eda_person_b.ipynb # raw signal plots: LEFT vs RIGHT, C3/C4
eda_person_c.ipynb # PSD/ERD analysis: is there a real signal difference?
eda_person_d.ipynb # artifact/outlier check: how messy is the data?
eda_summary.md # our converged conclusions — written after all 4
# notebooks are done, this feeds next week's config


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