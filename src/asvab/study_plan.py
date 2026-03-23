"""
Study Plan Generator
--------------------
Builds a personalized weekly ASVAB study plan based on the soldier's
weakest subtest scores (or a balanced default plan if no data exists).
"""

from .question_bank import SUBTEST_INFO
from .progress_tracker import ASVABProgressTracker

# Daily time blocks ─ each block = one study session
_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# GT-focus subtests and ST-focus subtests
_GT_SUBTESTS = ["WK", "PC", "AR"]
_ST_SUBTESTS = ["MC", "AO"]
_ALL_SUBTESTS = _GT_SUBTESTS + _ST_SUBTESTS


class StudyPlan:
    def __init__(self, soldier_name: str, tracker: ASVABProgressTracker):
        self.soldier_name = soldier_name
        self.tracker = tracker

    # ------------------------------------------------------------------
    # Public
    # ------------------------------------------------------------------

    def generate(self) -> None:
        """Print a full 7-day study plan tailored to weak areas."""
        rankings = self._rank_subtests()
        plan = self._build_plan(rankings)
        self._print_plan(plan, rankings)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _rank_subtests(self) -> list:
        """
        Returns subtests ordered worst-first (most study needed first).
        Subtests with no data get a synthetic score of 0 (highest priority).
        """
        scores = {}
        for st in _ALL_SUBTESTS:
            avg = self.tracker.average_score(self.soldier_name, st)
            scores[st] = avg if avg is not None else 0.0
        return sorted(scores.keys(), key=lambda k: scores[k])

    def _build_plan(self, ranked: list) -> list:
        """
        Assign one subtest (or rest) to each of the 7 days.
        Weakest subtests get extra days; Sunday is always a full review.
        """
        # Weights: position 0 (weakest) gets 3 days, next gets 2, rest get 1
        weights = {st: 1 for st in ranked}
        weights[ranked[0]] = 3
        if len(ranked) > 1:
            weights[ranked[1]] = 2

        schedule = []
        for st in ranked:
            schedule.extend([st] * weights[st])

        # Trim to 6 days; fill any gap with the weakest subtest so the list is
        # always exactly 6 before the Sunday review is appended.
        schedule = schedule[:6]
        while len(schedule) < 6:
            schedule.append(ranked[0])
        schedule.append("REVIEW")
        return schedule

    def _print_plan(self, plan: list, ranked: list) -> None:
        scores = {}
        for st in _ALL_SUBTESTS:
            avg = self.tracker.average_score(self.soldier_name, st)
            scores[st] = avg

        print(f"\n{'═'*60}")
        print(f"  7-Day ASVAB Study Plan  –  {self.soldier_name}")
        print(f"{'═'*60}")

        # Show current readiness
        print("\n  Current Readiness:")
        for st in _ALL_SUBTESTS:
            avg = scores[st]
            bar = self._bar(avg or 0)
            label = f"{avg:.1f}%" if avg is not None else "no data"
            composite_tags = ", ".join(SUBTEST_INFO[st]["composite"])
            print(f"    {st}  {bar}  {label:>7}   [{composite_tags}]")

        print(f"\n  {'Day':<12} {'Focus':<10} {'Subtest Name':<28} {'Sessions'}")
        print(f"  {'─'*12} {'─'*10} {'─'*28} {'─'*8}")

        # Build a map of subtest -> number of days assigned (excluding REVIEW)
        subtest_day_counts = {}
        for st in plan:
            if st != "REVIEW":
                subtest_day_counts[st] = subtest_day_counts.get(st, 0) + 1

        for day, subtest in zip(_DAYS, plan):
            if subtest == "REVIEW":
                print(f"  {day:<12} {'REVIEW':<10} {'All subtests – timed drill':<28} 2")
            else:
                name = SUBTEST_INFO[subtest]["name"]
                # Use 3 sessions on days for the weakest subtest, 2 otherwise
                sessions = "3" if subtest_day_counts.get(subtest, 0) >= 3 else "2"
                print(f"  {day:<12} {subtest:<10} {name:<28} {sessions}")

        print(f"\n  Priority order (weakest → strongest): {' → '.join(ranked)}")
        print(
            "\n  TIPS:"
            "\n    • Each session = 10 practice questions in the app"
            "\n    • Review all missed questions before the next session"
            "\n    • On Review Day: do one 10-Q quiz for every subtest"
            "\n    • Track your scores in the app to see progress over time"
        )
        print(f"{'═'*60}\n")

    def _bar(self, pct: float, width: int = 15) -> str:
        filled = int(pct / 100 * width)
        return "[" + "█" * filled + "░" * (width - filled) + "]"
