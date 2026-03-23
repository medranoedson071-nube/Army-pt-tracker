# Army PT Tracker

A Python command-line application that calculates ACFT scores, 
tracks pass/fail status, saves score history for individual soldiers,
and includes a full **GT-ST ASVAB Booster** for composite score practice.

---

## The Problem

Army physical fitness and ASVAB readiness are often tracked manually — paper scorecards,
spreadsheets, or memory. This tool automates ACFT score calculation and ASVAB subtest
practice, maintaining persistent history so soldiers and leaders can track fitness
and academic trends over time.

---

## Features

### ACFT Tracker
- Calculates total ACFT score across all 6 events
- Determines pass/fail based on the 360-point threshold
- Saves score history to a local JSON file
- Displays full score history by soldier name

### GT-ST Booster (ASVAB Practice)
- Practice questions for **all ASVAB subtests** that feed GT and ST composites:
  - **GT (General Technical):** AR (Arithmetic Reasoning) + VE (Word Knowledge + Paragraph Comprehension)
  - **ST (Skilled Technical):** MC (Mechanical Comprehension) + GS (General Science) + AS (Assembling Objects) + EI (Electronics Information)
- 10 practice questions per subtest (65 total, 5 for PC)
- Immediate feedback with explanations after each answer
- Estimated GT and ST percentage scores with pass/needs-work status
- Run individual subtests or all at once

---

## Tech Stack

- Python 3
- Object-Oriented Programming (OOP)
- JSON file storage
- Developed and tested on Windows and Android (Termux)

---

## How to Run

1. Clone the repo:
   git clone https://github.com/medranoedson071-nube/army-pt-tracker.git

2. Navigate into the folder:
   cd army-pt-tracker

3. Run the program:
   python main.py

4. Choose from the main menu:
   - Option 1: ACFT Score Tracker
   - Option 2: GT-ST Booster (ASVAB Practice)

---

## Project Structure

```
army-pt-tracker/
├── main.py                       # Entry point and main menu
├── scores.json                   # Auto-generated ACFT score history
├── src/
│   ├── soldier.py                # Soldier class
│   ├── acft_event.py             # ACFTEvent class
│   ├── acft_record.py            # ACFTRecord class
│   └── score_tracker.py          # ScoreTracker class (JSON persistence)
├── gt_st_booster/
│   ├── __init__.py               # Package entry point
│   ├── questions.py              # ASVAB question bank (AR, WK, PC, MC, GS, AS, EI)
│   ├── quiz.py                   # Interactive quiz runner
│   └── score_calculator.py       # GT/ST composite score estimator
└── README.md
```

---

## ASVAB Composite Score Reference

| Composite | Formula         | Purpose |
|-----------|-----------------|---------|
| GT        | VE + AR         | Officer/warrant officer eligibility, many MOS |
| ST        | MC + AS + EI + GS | Technical MOS eligibility |

A GT score of **110+** is required for many competitive MOS and officer programs.

---

## Author

Edson Medrano
Active Duty U.S. Army | AI Software Engineering Student
GitHub: github.com/medranoedson071-nube
