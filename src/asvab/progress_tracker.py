"""
ASVAB Progress Tracker
----------------------
Persists per-soldier ASVAB quiz results in asvab_scores.json,
mirroring the pattern used by ScoreTracker for ACFT records.
"""

import json
import os
from datetime import date


class ASVABProgressTracker:
    def __init__(self, filepath="asvab_scores.json"):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump({}, f)

    # ------------------------------------------------------------------
    # Writing
    # ------------------------------------------------------------------

    def save_result(self, soldier_name: str, subtest: str, correct: int, total: int) -> None:
        """Append a quiz result for a soldier."""
        data = self._load()
        if soldier_name not in data:
            data[soldier_name] = {}
        if subtest not in data[soldier_name]:
            data[soldier_name][subtest] = []
        data[soldier_name][subtest].append(
            {
                "date": str(date.today()),
                "correct": correct,
                "total": total,
                "pct": round(correct / total * 100, 1) if total else 0.0,
            }
        )
        self._save(data)

    # ------------------------------------------------------------------
    # Reading
    # ------------------------------------------------------------------

    def get_history(self, soldier_name: str) -> dict:
        """Return all recorded results for a soldier, keyed by subtest."""
        data = self._load()
        return data.get(soldier_name, {})

    def get_subtest_history(self, soldier_name: str, subtest: str) -> list:
        return self.get_history(soldier_name).get(subtest, [])

    def latest_score(self, soldier_name: str, subtest: str) -> dict | None:
        history = self.get_subtest_history(soldier_name, subtest)
        return history[-1] if history else None

    def average_score(self, soldier_name: str, subtest: str) -> float | None:
        history = self.get_subtest_history(soldier_name, subtest)
        if not history:
            return None
        return round(sum(r["pct"] for r in history) / len(history), 1)

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def show_history(self, soldier_name: str) -> None:
        history = self.get_history(soldier_name)
        if not history:
            print(f"  No ASVAB records found for {soldier_name}.")
            return

        print(f"\n{'═'*60}")
        print(f"  ASVAB Study History – {soldier_name}")
        print(f"{'═'*60}")
        for subtest, records in sorted(history.items()):
            avg = self.average_score(soldier_name, subtest)
            print(f"\n  [{subtest}]  Avg: {avg:.1f}%  ({len(records)} attempt(s))")
            for r in records[-5:]:          # show last 5 attempts
                bar = self._bar(r["pct"])
                status = "PASS" if r["pct"] >= 70 else "FAIL"
                print(f"    {r['date']}  {r['correct']:>2}/{r['total']:<2}  {r['pct']:>5.1f}%  {status}  {bar}")
        print(f"{'═'*60}\n")

    def show_composite_estimate(self, soldier_name: str) -> None:
        """Show estimated GT / ST improvement based on average quiz scores."""
        history = self.get_history(soldier_name)
        if not history:
            print("  No data yet. Complete some quizzes first.")
            return

        def avg(subtest):
            return self.average_score(soldier_name, subtest)

        wk = avg("WK") or 0
        pc = avg("PC") or 0
        ar = avg("AR") or 0
        mc = avg("MC") or 0
        ao = avg("AO") or 0

        ve = (wk + pc) / 2 if (wk or pc) else 0
        gt_est = (ve + ar) / 2 if (ve or ar) else 0
        st_est = (mc + ao + ve) / 3 if (mc or ao or ve) else 0

        print(f"\n{'─'*50}")
        print("  Composite Score Readiness Estimate")
        print(f"{'─'*50}")
        print(f"  VE  (Word Knowledge + Para Comp avg) : {ve:.1f}%")
        print(f"  AR  (Arithmetic Reasoning avg)       : {ar:.1f}%")
        print(f"  MC  (Mechanical Comprehension avg)   : {mc:.1f}%")
        print(f"  AO  (Assembling Objects avg)         : {ao:.1f}%")
        print(f"{'─'*50}")
        print(f"  GT  (VE + AR) Readiness              : {gt_est:.1f}%")
        print(f"  ST  (MC + AO + VE) Readiness         : {st_est:.1f}%")
        print(f"{'─'*50}")
        if gt_est < 70:
            weak = []
            if ve < 70:
                weak.append("WK and PC (Verbal)")
            if ar < 70:
                weak.append("AR (Arithmetic)")
            print(f"  ► Focus areas for GT: {', '.join(weak) if weak else 'Keep practicing!'}")
        if st_est < 70:
            weak = []
            if mc < 70:
                weak.append("MC (Mechanical)")
            if ao < 70:
                weak.append("AO (Assembling Objects)")
            if ve < 70:
                weak.append("WK/PC (Verbal)")
            print(f"  ► Focus areas for ST: {', '.join(weak) if weak else 'Keep practicing!'}")
        print()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _bar(self, pct: float, width: int = 20) -> str:
        filled = int(pct / 100 * width)
        return "[" + "█" * filled + "░" * (width - filled) + "]"

    def _load(self) -> dict:
        with open(self.filepath, "r") as f:
            return json.load(f)

    def _save(self, data: dict) -> None:
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)
