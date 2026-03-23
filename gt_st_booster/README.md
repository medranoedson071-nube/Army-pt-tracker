# GT-ST Booster — ASVAB Practice Module

A self-contained Python module for practicing the ASVAB subtests that drive
your **GT (General Technical)** and **ST (Skilled Technical)** composite scores.

---

## Composite Score Reference

| Composite | Formula              | Common Use |
|-----------|----------------------|------------|
| **GT**    | VE (WK + PC) + AR    | Most MOS, officer/warrant eligibility |
| **ST**    | MC + GS + AS + EI    | Technical/STEM MOS |

A GT score of **110+** is competitive for many advanced MOS and officer programs.

---

## Subtests Covered

| Code | Full Name                    | Feeds |
|------|------------------------------|-------|
| AR   | Arithmetic Reasoning         | GT    |
| WK   | Word Knowledge               | GT    |
| PC   | Paragraph Comprehension      | GT    |
| MC   | Mechanical Comprehension     | ST    |
| GS   | General Science              | ST    |
| AS   | Assembling Objects           | ST    |
| EI   | Electronics Information      | ST    |

---

## How to Run

### Standalone (recommended)
From the repo root:
```
python -m gt_st_booster
```

### Via Army Tracker main menu
```
python main.py
```
Then select option **2. GT-ST Booster (ASVAB Practice)**.

---

## Module Structure

```
gt_st_booster/
├── __init__.py          # Package entry; exports run_booster_menu
├── __main__.py          # Standalone entry point (python -m gt_st_booster)
├── questions.py         # Question bank — 65 questions across 7 subtests
├── quiz.py              # Interactive quiz runner
├── score_calculator.py  # GT/ST composite score estimator and report printer
└── README.md            # This file
```

---

## Quiz Features

- **Per-question feedback** — immediate correct/incorrect with explanation
- **Individual subtest mode** — practice one subtest at a time
- **Full practice mode** — run all 7 subtests in sequence
- **Score report** — estimated GT and ST percentages with visual progress bar and pass/needs-work status

---

## No External Dependencies

This module uses only Python standard library. No `pip install` required.
