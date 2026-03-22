import json
import os

class ScoreTracker:
    def __init__(self, filepath="scores.json"):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump({}, f)

    def save_record(self, name, score, passed, date):
        with open(self.filepath, "r") as f:
            data = json.load(f)
        if name not in data:
            data[name] = []
        data[name].append({
            "score": score,
            "passed": passed,
            "date": str(date)
        })
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def show_history(self, name):
        with open(self.filepath, "r") as f:
            data = json.load(f)
        if name not in data:
            print("No records found.")
            return
        for record in data[name]:
            status = "PASS" if record["passed"] else "FAIL"
            print(f"  {record['date']} | Score: {record['score']} | {status}")
