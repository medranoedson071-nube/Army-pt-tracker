# Army PT Tracker

A Python command-line application that calculates ACFT scores, 
tracks pass/fail status, and saves score history for individual soldiers.

---

## The Problem

Army physical fitness tracking is often done manually — paper scorecards,
spreadsheets, or memory. This tool automates ACFT score calculation and
maintains a persistent history so soldiers and leaders can track fitness
trends over time.

---

## Features

- Calculates total ACFT score across all 6 events
- Determines pass/fail based on the 360-point threshold
- Saves score history to a local JSON file
- Displays full score history by soldier name
- Clean object-oriented architecture with 4 classes

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

---

## Project Structure

army-pt-tracker/
├── main.py          # Entry point, contains all classes
├── scores.json      # Auto-generated score history file
└── README.md

---

## Author

Edson Medrano
Active Duty U.S. Army | AI Software Engineering Student
GitHub: github.com/medranoedson071-nube
