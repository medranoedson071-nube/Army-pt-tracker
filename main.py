from src.soldier import Soldier
from src.acft_event import ACFTEvent
from src.acft_record import ACFTRecord
from src.score_tracker import ScoreTracker

def main():
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

if __name__ == "__main__":
    main()