# gt_st_booster/score_calculator.py
# Estimates GT and ST ASVAB composite scores based on practice quiz results.
#
# Real ASVAB composites are scaled scores; this module provides a straightforward
# percentage-based estimate useful for identifying weak areas and tracking improvement.

from .questions import GT_SUBTESTS, ST_SUBTESTS, SUBTEST_NAMES


def estimate_composite(scores: dict, subtests: list) -> int:
    """Return a 0-100 percentage score for the given composite's subtests."""
    total_correct = sum(scores.get(s, {}).get("correct", 0) for s in subtests)
    total_questions = sum(scores.get(s, {}).get("total", 0) for s in subtests)
    if total_questions == 0:
        return 0
    return round((total_correct / total_questions) * 100)


def print_score_report(scores: dict) -> None:
    """Print a formatted GT/ST score report from a scores dict."""
    print("\n" + "=" * 50)
    print("       GT-ST BOOSTER — SCORE REPORT")
    print("=" * 50)

    # Per-subtest breakdown
    print("\n  Subtest Breakdown:")
    for code, name in SUBTEST_NAMES.items():
        entry = scores.get(code)
        if entry:
            pct = round((entry["correct"] / entry["total"]) * 100) if entry["total"] else 0
            bar = "#" * (pct // 5) + "-" * (20 - pct // 5)
            print(f"    {code} ({name:<30}) {entry['correct']:>2}/{entry['total']} [{bar}] {pct:>3}%")

    # GT composite
    gt_score = estimate_composite(scores, GT_SUBTESTS)
    st_score = estimate_composite(scores, ST_SUBTESTS)

    print()
    print(f"  GT (General Technical)  = AR + VE (WK + PC)  →  Estimated: {gt_score}%")
    print(f"  ST (Skilled Technical)  = MC+GS+AS+EI  →  Estimated: {st_score}%")

    print()
    if gt_score >= 80:
        print("  GT Status: ✓ STRONG  — Competitive for most MOS.")
    elif gt_score >= 60:
        print("  GT Status: ~ MODERATE — Keep practicing AR and vocabulary.")
    else:
        print("  GT Status: ✗ NEEDS WORK — Focus heavily on AR and WK/PC.")

    if st_score >= 80:
        print("  ST Status: ✓ STRONG  — Competitive for technical MOS.")
    elif st_score >= 60:
        print("  ST Status: ~ MODERATE — Review MC and EI concepts.")
    else:
        print("  ST Status: ✗ NEEDS WORK — Study electronics, mechanics, and science.")

    print("=" * 50)
