from datetime import date
from src.acft_event import ACFTEvent

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
        return self.total_score() >= 360

    def __str__(self):
        result = "PASS" if self.passed() else "FAIL"
        return f"{self.soldier} | Score: {self.total_score()} | {result} | Date: {self.date}"
