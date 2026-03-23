from src.soldier import Soldier
from src.acft_event import ACFTEvent
from src.acft_record import ACFTRecord
from src.score_tracker import ScoreTracker
from gt_st_booster import run_booster_menu


def run_acft():
    """Run the ACFT score tracker demo."""
    # Create a soldier
    soldier = Soldier("Medrano", "SPC", "1-10 CAV", 25, "M")

    # Create ACFT events
    events = [
        ACFTEvent("3 Rep Max Deadlift", 200, 70),
        ACFTEvent("Standing Power Throw", 8.5, 65),
        ACFTEvent("Hand Release Push-Up", 35, 70),
        ACFTEvent("Sprint Drag Carry", 120, 65),
        ACFTEvent("Leg Tuck", 10, 65),
        ACFTEvent("2 Mile Run", 1560, 70)
    ]

    # Build record
    record = ACFTRecord(soldier)
    for event in events:
        record.add_event(event)
    print("\n=== ACFT RESULTS ===")
    print(record)
    print("\nEvent Breakdown:")
    for event in record.events:
        print(f"  {event}")

    # Save to file
    tracker = ScoreTracker()
    tracker.save_record(soldier.name, record.total_score(), record.passed(), record.date)
    print("\nRecord saved.")

    # Show history
    print("\n=== SCORE HISTORY ===")
    tracker.show_history("Medrano")


def main():
    while True:
        print("\n" + "=" * 50)
        print("       ARMY TRACKER — MAIN MENU")
        print("=" * 50)
        print("  1. ACFT Score Tracker")
        print("  2. GT-ST Booster (ASVAB Practice)")
        print("  3. Exit")
        print("=" * 50)
        choice = input("  Select an option (1-3): ").strip()

        if choice == "1":
            run_acft()
        elif choice == "2":
            run_booster_menu()
        elif choice == "3":
            print("\n  Goodbye, Soldier. Stay sharp!\n")
            break
        else:
            print("  Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()