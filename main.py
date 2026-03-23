"""
Army PT & ASVAB Study Tracker
==============================
Unified entry point tying the ACFT score tracker and the ASVAB study
program to a single soldier profile.
"""

from src.soldier import Soldier
from src.acft_event import ACFTEvent
from src.acft_record import ACFTRecord
from src.score_tracker import ScoreTracker
from src.asvab.progress_tracker import ASVABProgressTracker
from src.asvab.study_session import StudySession
from src.asvab.study_plan import StudyPlan
from src.asvab.question_bank import SUBTEST_INFO


# ---------------------------------------------------------------------------
# Soldier setup
# ---------------------------------------------------------------------------

def create_soldier() -> Soldier:
    print("\n" + "═" * 60)
    print("  Army PT & ASVAB Tracker  –  Soldier Setup")
    print("═" * 60)
    name = input("  Last name          : ").strip() or "Medrano"
    rank = input("  Rank (e.g. SPC)    : ").strip() or "SPC"
    unit = input("  Unit               : ").strip() or "1-10 CAV"
    try:
        age = int(input("  Age                : ").strip())
    except ValueError:
        age = 25
    gender = input("  Gender (M/F)       : ").strip().upper() or "M"
    return Soldier(name, rank, unit, age, gender)


# ---------------------------------------------------------------------------
# ACFT menu
# ---------------------------------------------------------------------------

def acft_menu(soldier: Soldier, acft_tracker: ScoreTracker) -> None:
    print("\n" + "─" * 50)
    print(f"  ACFT Tracker  –  {soldier.rank} {soldier.name}")
    print("─" * 50)

    events = []
    event_names = [
        "3 Rep Max Deadlift",
        "Standing Power Throw",
        "Hand Release Push-Up",
        "Sprint Drag Carry",
        "Plank",
        "2 Mile Run",
    ]

    for name in event_names:
        try:
            raw = float(input(f"  {name} – raw score : "))
            pts = int(input(f"  {name} – points    : "))
        except ValueError:
            print("  Invalid input – skipping event.")
            continue
        events.append(ACFTEvent(name, raw, pts))

    if not events:
        print("  No events entered.")
        return

    record = ACFTRecord(soldier)
    for event in events:
        record.add_event(event)

    print("\n=== ACFT RESULTS ===")
    print(record)
    print("\nEvent Breakdown:")
    for event in record.events:
        print(f"  {event}")

    acft_tracker.save_record(
        soldier.name, record.total_score(), record.passed(), record.date
    )
    print("\n  ✔ Record saved.")


def acft_history(soldier: Soldier, acft_tracker: ScoreTracker) -> None:
    print(f"\n=== ACFT HISTORY – {soldier.rank} {soldier.name} ===")
    acft_tracker.show_history(soldier.name)


# ---------------------------------------------------------------------------
# ASVAB menu
# ---------------------------------------------------------------------------

def asvab_menu(soldier: Soldier, asvab_tracker: ASVABProgressTracker) -> None:
    session = StudySession(soldier.name, asvab_tracker)
    plan = StudyPlan(soldier.name, asvab_tracker)

    while True:
        print(f"\n{'─'*50}")
        print(f"  ASVAB Study Program  –  {soldier.rank} {soldier.name}")
        print(f"{'─'*50}")
        print("  Subtests that boost your GT and ST scores:")
        for code, info in SUBTEST_INFO.items():
            composites = ", ".join(info["composite"])
            print(f"    {code}  –  {info['name']:<28}  [{composites}]")
        print()
        print("  [1] Practice a subtest quiz")
        print("  [2] View my ASVAB score history")
        print("  [3] See composite score readiness (GT / ST)")
        print("  [4] Generate my 7-day study plan")
        print("  [5] Back to main menu")

        choice = input("\n  Choose (1-5): ").strip()

        if choice == "1":
            code = input(
                "  Which subtest? (WK / PC / AR / MC / AO): "
            ).strip().upper()
            if code not in SUBTEST_INFO:
                print("  Unknown subtest.")
                continue
            try:
                num_q = int(input("  How many questions? (1-25, default 10): ").strip() or "10")
                num_q = max(1, min(num_q, 25))
            except ValueError:
                num_q = 10
            session.run(code, num_questions=num_q)

        elif choice == "2":
            asvab_tracker.show_history(soldier.name)

        elif choice == "3":
            asvab_tracker.show_composite_estimate(soldier.name)

        elif choice == "4":
            plan.generate()

        elif choice == "5":
            break

        else:
            print("  Please enter 1-5.")


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def main() -> None:
    soldier = create_soldier()
    acft_tracker = ScoreTracker()
    asvab_tracker = ASVABProgressTracker()

    while True:
        print(f"\n{'═'*60}")
        print(f"  Army Tracker  –  {soldier.rank} {soldier.name}  |  {soldier.unit}")
        print(f"{'═'*60}")
        print("  [1] Log ACFT scores")
        print("  [2] View ACFT score history")
        print("  [3] ASVAB Study Program  (GT / ST boost)")
        print("  [4] Exit")

        choice = input("\n  Choose (1-4): ").strip()

        if choice == "1":
            acft_menu(soldier, acft_tracker)
        elif choice == "2":
            acft_history(soldier, acft_tracker)
        elif choice == "3":
            asvab_menu(soldier, asvab_tracker)
        elif choice == "4":
            print(f"\n  Stay Army Strong, {soldier.rank} {soldier.name}. Hooah! 🎖\n")
            break
        else:
            print("  Please enter 1-4.")


if __name__ == "__main__":
    main()