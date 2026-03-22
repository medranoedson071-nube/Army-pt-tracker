from datetime import date
import json
import os

# === CONFIGURABLE CONSTANTS ===

PASSING_SCORE = 360

# All ACFT events in one place for easy editing/updating
ACFT_EVENTS = [
    {"name": "3 Rep Max Deadlift", "raw_score": 200, "points": 70},
    {"name": "Standing Power Throw", "raw_score": 8.5, "points": 65},
    {"name": "Hand Release Push-Up", "raw_score": 35, "points": 70},
    {"name": "Sprint Drag Carry", "raw_score": 120, "points": 65},
    {"name": "Leg Tuck", "raw_score": 10, "points": 65},
    {"name": "2 Mile Run", "raw_score": 1560, "points": 70},
]

class Soldier:
    """Represents a Soldier taking the ACFT."""
    def __init__(self, name, rank, unit, age, gender):
        self.name = name
        self.rank = rank
        self.unit = unit
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.rank} {self.name} | Unit: {self.unit} | Age: {self.age}"

class ACFTEvent:
    """Represents a single ACFT event and score/results."""
    def __init__(self, name, raw_score, points):
        self.name = name
        self.raw_score = raw_score
        self.points = points

    def __str__(self):
        return f"{self.name}: {self.raw_score} ({self.points} pts)"

class ACFTRecord:
    """Stores ACFT event results for one soldier on a given date."""
    def __init__(self, soldier, events=None):
        self.soldier = soldier
        self.events = events if events else []
        self.date = date.today()

    def add_event(self, event):
        self.events.append(event)

    def total_score(self):
        return sum(e.points for e in self.events)

    def passed(self):
        return self.total_score() >= PASSING_SCORE

    def __str__(self):
        result = "PASS" if self.passed() else "FAIL"
        return f"{self.soldier} | Score: {self.total_score()} | {result} | Date: {self.date}"

class ScoreTracker:
    """Manages ACFT score storage and history using a local JSON file."""
    def __init__(self, filepath="scores.json"):
        self.filepath = filepath
        if not os.path.exists(filepath):
            try:
                with open(filepath, "w") as f:
                    json.dump({}, f)
            except Exception as e:
                print(f"Could not create score file: {e}")

    def save_record(self, name, score, passed, date):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            print("Warning: Starting a new history file.")

        if name not in data:
            data[name] = []
        data[name].append({"score": score, "passed": passed, "date": str(date)})
        try:
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving the record: {e}")

    def show_history(self, name):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No history yet.")
            return
        if name not in data:
            print("No records found.")
            return
        for record in data[name]:
            status = "PASS" if record["passed"] else "FAIL"
            print(f"  {record['date']} | Score: {record['score']} | {status}")

def main():
    print("=== ACFT Tracker ===")
    # In the future, you can grab soldier info and events from user input here!

    soldier = Soldier("Medrano", "SPC", "1-10 CAV", 25, "male")  # Suggested better gender string

    # Use all ACFT_EVENTS for this run
    events = [ACFTEvent(e["name"], e["raw_score"], e["points"]) for e in ACFT_EVENTS]

    record = ACFTRecord(soldier)
    for event in events:
        record.add_event(event)
    print("\n=== ACFT RESULTS ===")
    print(record)
    print("\nEvent Breakdown:")
    for event in record.events:
        print(f"  {event}")

    tracker = ScoreTracker()
    tracker.save_record(soldier.name, record.total_score(), record.passed(), record.date)
    print("\nRecord saved.")

    print("\n=== SCORE HISTORY ===")
    tracker.show_history("Medrano")

if __name__ == "__main__":
    main()
