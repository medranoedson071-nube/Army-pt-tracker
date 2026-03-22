import json
import os

class ScoreTracker:
    def __init__(self, filepath="data/records.json"):
        self.filepath = filepath
        os.makedirs("data", exist_ok=True)

    def save_record(self, soldier_name, score, passed, date):
        records = self.load_records()
        records.append({
            "soldier": soldier_name,
            "score": score,
            "passed": passed,
            "date": str(date)
        })
        with open(self.filepath, "w") as f:
            json.dump(records, f, indent=2)

    def load_records(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r") as f:
            return json.load(f)

    def show_history(self, soldier_name):
        records = self.load_records()
        history = [r for r in records if r["soldier"] == soldier_name]
        if not history:
            print(f"No records found for {soldier_name}")
        for r in history:
            status = "PASS" if r["passed"] else "FAIL"
            print(f"{r['date']} | Score: {r['score']} | {status}")
