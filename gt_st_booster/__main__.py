# gt_st_booster/__main__.py
# Allows the GT-ST-Booster to be run as a standalone module:
#   python -m gt_st_booster

from .quiz import run_booster_menu

if __name__ == "__main__":
    print("\n  Welcome to the GT-ST ASVAB Booster!")
    print("  Practice the subtests that drive your GT and ST composite scores.\n")
    run_booster_menu()
    print("  Thanks for practicing. Stay mission-ready!\n")
