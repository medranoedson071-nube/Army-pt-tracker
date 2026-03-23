"""
ASVAB Study Program
====================
Standalone entry point for the ASVAB study program.
Run with:  python asvab_study.py

Covers the five subtests that boost Army GT and ST composite scores:
  GT  (General Technical)  = VE + AR   (WK, PC, AR)
  ST  (Skilled Technical)  = MC + AO + VE   (WK, PC, MC, AO)
"""

from src.asvab.progress_tracker import ASVABProgressTracker
from src.asvab.study_session import StudySession
from src.asvab.study_plan import StudyPlan
from src.asvab.question_bank import SUBTEST_INFO


def get_soldier_name() -> str:
    print("\n" + "═" * 60)
    print("  ASVAB Study Program  –  GT & ST Score Booster")
    print("═" * 60)
    name = input("  Enter your last name: ").strip()
    return name if name else "Soldier"


def asvab_menu(soldier_name: str, tracker: ASVABProgressTracker) -> None:
    session = StudySession(soldier_name, tracker)
    plan = StudyPlan(soldier_name, tracker)

    while True:
        print(f"\n{'─'*50}")
        print(f"  ASVAB Study Program  –  {soldier_name}")
        print(f"{'─'*50}")
        print("  Subtests covered (GT & ST composites):")
        for code, info in SUBTEST_INFO.items():
            composites = ", ".join(info["composite"])
            print(f"    {code}  –  {info['name']:<28}  [{composites}]")
        print()
        print("  [1] Practice a subtest quiz")
        print("  [2] View my score history")
        print("  [3] See GT / ST composite readiness estimate")
        print("  [4] Generate my 7-day study plan")
        print("  [5] Exit")

        choice = input("\n  Choose (1-5): ").strip()

        if choice == "1":
            code = input(
                "  Which subtest? (WK / PC / AR / MC / AO): "
            ).strip().upper()
            if code not in SUBTEST_INFO:
                print("  Unknown subtest. Please enter WK, PC, AR, MC, or AO.")
                continue
            try:
                num_q = int(input("  How many questions? (1-25, default 10): ").strip() or "10")
                num_q = max(1, min(num_q, 25))
            except ValueError:
                num_q = 10
            session.run(code, num_questions=num_q)

        elif choice == "2":
            tracker.show_history(soldier_name)

        elif choice == "3":
            tracker.show_composite_estimate(soldier_name)

        elif choice == "4":
            plan.generate()

        elif choice == "5":
            print(f"\n  Good luck on the ASVAB, {soldier_name}. Hooah! 🎖\n")
            break

        else:
            print("  Please enter 1-5.")


def main() -> None:
    soldier_name = get_soldier_name()
    tracker = ASVABProgressTracker()
    asvab_menu(soldier_name, tracker)


if __name__ == "__main__":
    main()
