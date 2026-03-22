from datetime import date
import json
import os

PASSING_SCORE = 360

class Soldier:
    def __init__(self, name, rank, unit, age, gender):
        self.name = name
        self.rank = rank
        self.unit = unit
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"{self.rank} {self.name} | Unit: {self.unit} | Age: {self.age}"

class ACFTEvent:
    def __init__(self, name, raw_score, points):
        self.name = name
        self.raw_score = raw_score
        self.points = points
    def __str__(self):
        return f"{self.name}: {self.raw_score} ({self.points} pts)"

class ACFTRecord:
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
    def __init__(self, filepath="scores.json"):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump({}, f)
    def save_record(self, name, score, passed, date):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
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
    soldier = Soldier("Medrano", "SPC", "1-10 CAV", 25, "M")
    events = [
        ACFTEvent("3 Rep Max Deadlift", 200, 70),
        ACFTEvent("Standing Power Throw", 8.5, 65),
        ACFTEvent("Hand Release Push-Up", 35, 70),
        ACFTEvent("Sprint Drag Carry", 120, 65),
        ACFTEvent("Leg Tuck", 10, 65),
        ACFTEvent("2 Mile Run", 1560, 70)
    ]
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
