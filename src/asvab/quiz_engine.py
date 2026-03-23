"""
Quiz Engine
-----------
Drives a single quiz session for one ASVAB subtest.
Handles shuffling, answer checking, scoring, and feedback.
"""

import random
from .question_bank import QUESTION_BANK, SUBTEST_INFO


class QuizResult:
    """Holds the outcome of a completed quiz."""

    def __init__(self, subtest: str, total: int, correct: int, missed: list):
        self.subtest = subtest
        self.total = total
        self.correct = correct
        self.missed = missed  # list of question dicts that were answered wrong

    @property
    def score_pct(self) -> float:
        return (self.correct / self.total * 100) if self.total else 0.0

    @property
    def passed(self) -> bool:
        return self.score_pct >= 70.0

    def summary(self) -> str:
        status = "PASS ✓" if self.passed else "FAIL ✗"
        return (
            f"\n{'─'*50}\n"
            f"  {SUBTEST_INFO[self.subtest]['name']} ({self.subtest}) Quiz Results\n"
            f"{'─'*50}\n"
            f"  Score  : {self.correct}/{self.total} ({self.score_pct:.1f}%)\n"
            f"  Status : {status}  (pass threshold: 70%)\n"
            f"{'─'*50}"
        )


class QuizEngine:
    """Runs an interactive command-line quiz for a given subtest."""

    def __init__(self, subtest: str, num_questions: int = 10, shuffle: bool = True):
        if subtest not in QUESTION_BANK:
            raise ValueError(f"Unknown subtest: {subtest}. Choose from {list(QUESTION_BANK.keys())}")
        self.subtest = subtest
        self.num_questions = min(num_questions, len(QUESTION_BANK[subtest]))
        self.shuffle = shuffle

    def run(self) -> QuizResult:
        """Run the quiz interactively. Returns a QuizResult."""
        questions = list(QUESTION_BANK[self.subtest])
        if self.shuffle:
            random.shuffle(questions)
        questions = questions[: self.num_questions]

        info = SUBTEST_INFO[self.subtest]
        print(f"\n{'═'*60}")
        print(f"  ASVAB Subtest: {info['name']} ({self.subtest})")
        print(f"  Composites  : {', '.join(info['composite'])}")
        print(f"  Questions   : {self.num_questions}")
        print(f"{'═'*60}")
        print(f"  {info['description']}\n")
        print("  Enter the letter of your answer (A / B / C / D).")
        print("  Type 'quit' at any time to stop.\n")

        correct_count = 0
        missed = []

        for idx, q in enumerate(questions, start=1):
            print(f"Q{idx}. {q['question']}")
            for choice in q["choices"]:
                print(f"    {choice}")

            while True:
                raw = input("  Your answer: ").strip().upper()
                if raw == "QUIT":
                    print("\n  Quiz stopped early.")
                    answered = idx - 1
                    return QuizResult(
                        self.subtest, answered, correct_count, missed
                    )
                if raw in ("A", "B", "C", "D"):
                    break
                print("  Please enter A, B, C, or D.")

            if raw == q["answer"]:
                print("  ✓ Correct!\n")
                correct_count += 1
            else:
                print(f"  ✗ Incorrect. Correct answer: {q['answer']}")
                print(f"  Explanation: {q['explanation']}\n")
                missed.append(q)

        result = QuizResult(self.subtest, self.num_questions, correct_count, missed)
        print(result.summary())

        if missed:
            show = input("\n  Review missed questions? (y/n): ").strip().lower()
            if show == "y":
                self._review_missed(missed)

        return result

    def _review_missed(self, missed: list) -> None:
        print(f"\n{'─'*50}")
        print("  REVIEW – Missed Questions")
        print(f"{'─'*50}")
        for i, q in enumerate(missed, start=1):
            print(f"\n  {i}. {q['question']}")
            for choice in q["choices"]:
                marker = "◄ CORRECT" if choice.startswith(q["answer"]) else ""
                print(f"      {choice}  {marker}")
            print(f"     Explanation: {q['explanation']}")
        print(f"{'─'*50}\n")
