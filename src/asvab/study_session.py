"""
Study Session
-------------
Combines a tips review with an interactive quiz and saves the result
to the soldier's ASVAB progress history.
"""

from .question_bank import SUBTEST_INFO
from .quiz_engine import QuizEngine
from .progress_tracker import ASVABProgressTracker


class StudySession:
    """One study session for a soldier on a chosen subtest."""

    def __init__(self, soldier_name: str, tracker: ASVABProgressTracker):
        self.soldier_name = soldier_name
        self.tracker = tracker

    def run(self, subtest: str, num_questions: int = 10) -> None:
        info = SUBTEST_INFO[subtest]

        # ── Tips ─────────────────────────────────────────────────────
        print(f"\n{'═'*60}")
        print(f"  STUDY SESSION  –  {info['name']} ({subtest})")
        print(f"  Soldier: {self.soldier_name}")
        print(f"{'═'*60}")
        print(f"\n  📚 STUDY TIPS for {info['name']}:")
        for tip in info["tips"]:
            print(f"     • {tip}")

        last = self.tracker.latest_score(self.soldier_name, subtest)
        if last:
            print(
                f"\n  Last attempt ({last['date']}): "
                f"{last['correct']}/{last['total']} – {last['pct']}%"
            )

        input("\n  Press Enter to start the quiz…")

        # ── Quiz ─────────────────────────────────────────────────────
        engine = QuizEngine(subtest, num_questions=num_questions)
        result = engine.run()

        # ── Save ─────────────────────────────────────────────────────
        if result.total > 0:
            self.tracker.save_result(
                self.soldier_name, subtest, result.correct, result.total
            )
            print(f"  ✔ Result saved to {self.soldier_name}'s profile.\n")
