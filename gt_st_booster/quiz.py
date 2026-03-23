# gt_st_booster/quiz.py
# Interactive quiz runner for the GT-ST-Booster module.

from .questions import ALL_SUBTESTS, SUBTEST_NAMES, GT_SUBTESTS, ST_SUBTESTS
from .score_calculator import print_score_report


def run_subtest_quiz(code: str) -> dict:
    """Run through all questions for a single subtest. Returns {correct, total}."""
    questions = ALL_SUBTESTS[code]
    name = SUBTEST_NAMES[code]
    correct = 0

    print(f"\n{'=' * 50}")
    print(f"  {code} — {name}")
    print(f"  {len(questions)} questions  |  Type A, B, C, or D to answer")
    print("=" * 50)

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for choice in q["choices"]:
            print(f"  {choice}")

        while True:
            answer = input("  Your answer (A/B/C/D): ").strip().upper()
            if answer in ("A", "B", "C", "D"):
                break
            print("  Invalid input. Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("  ✓ Correct!")
            correct += 1
        else:
            print(f"  ✗ Incorrect. Correct answer: {q['answer']}")
        print(f"  Explanation: {q['explanation']}")

    pct = round((correct / len(questions)) * 100)
    print(f"\n  {code} Result: {correct}/{len(questions)} ({pct}%)")
    return {"correct": correct, "total": len(questions)}


def _print_booster_menu():
    print("\n" + "=" * 50)
    print("       GT-ST BOOSTER — ASVAB PRACTICE")
    print("=" * 50)
    print("  GT Composite subtests (VE + AR):")
    print("    1. AR — Arithmetic Reasoning")
    print("    2. WK — Word Knowledge (VE)")
    print("    3. PC — Paragraph Comprehension (VE)")
    print()
    print("  ST Composite subtests (MC + GS + AS + EI):")
    print("    4. MC — Mechanical Comprehension")
    print("    5. GS — General Science")
    print("    6. AS — Assembling Objects")
    print("    7. EI — Electronics Information")
    print()
    print("    8. Run ALL subtests (full GT-ST practice)")
    print("    9. Back to main menu")
    print("=" * 50)


_MENU_MAP = {
    "1": "AR",
    "2": "WK",
    "3": "PC",
    "4": "MC",
    "5": "GS",
    "6": "AS",
    "7": "EI",
}


def run_booster_menu():
    """Entry point for the GT-ST-Booster interactive menu."""
    session_scores = {}

    while True:
        _print_booster_menu()
        choice = input("  Select an option (1-9): ").strip()

        if choice in _MENU_MAP:
            code = _MENU_MAP[choice]
            result = run_subtest_quiz(code)
            session_scores[code] = result

            # Offer score report after each subtest
            show = input("\n  View score report so far? (y/n): ").strip().lower()
            if show == "y":
                print_score_report(session_scores)

        elif choice == "8":
            print("\n  Starting full GT-ST practice — all 7 subtests.\n")
            all_codes = list(ALL_SUBTESTS.keys())
            for code in all_codes:
                result = run_subtest_quiz(code)
                session_scores[code] = result
            print_score_report(session_scores)

        elif choice == "9":
            if session_scores:
                print_score_report(session_scores)
            print("\n  Returning to main menu.\n")
            break

        else:
            print("  Invalid choice. Please enter a number from 1 to 9.")
