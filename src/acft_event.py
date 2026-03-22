class ACFTEvent:
    def __init__(self, name, raw_score, points):
        self.name = name
        self.raw_score = raw_score
        self.points = points

    def __str__(self):
        return f"{self.name}: {self.raw_score} ({self.points} pts)"
