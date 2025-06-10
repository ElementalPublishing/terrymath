import argparse
import subprocess
import sys
from pathlib import Path
import os

print("sys.executable:", sys.executable)
print("cwd:", os.getcwd())
print("__file__:", __file__)

def run_pytest(test_file):
    print(f"\nRunning tests in {test_file}...\n")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-v", "-s", test_file],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed. See details above.")
    return result.returncode

def main():
    # Prompt user at the beginning
    answer = input("Do you want to run the TerryMath scientific test suite? (y/n): ").strip().lower()
    if answer == "y":
        test_file = Path(__file__).parent / "test_terrymath.py"
        run_pytest(str(test_file))
        sys.exit(0)

    parser = argparse.ArgumentParser(
        description="TerryMath CLI: Experiment with Terrence Howard's math and run scientific tests."
    )
    parser.add_argument(
        "--test", action="store_true",
        help="Run the TerryMath test suite and show detailed results."
    )
    parser.add_argument(
        "--mode", type=str, default="terry_original",
        choices=["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"],
        help="Select TerryMath mode for interactive calculation."
    )
    parser.add_argument(
        "--multiply", nargs=2, type=int, metavar=('A', 'B'),
        help="Multiply two numbers using the selected TerryMath mode."
    )
    args = parser.parse_args()

    if args.test:
        test_file = Path(__file__).parent / "test_terrymath.py"
        run_pytest(str(test_file))
        sys.exit(0)

    from terrymath import TerryMath
    tm = TerryMath(mode=args.mode)
    print(f"TerryMath CLI - Mode: {args.mode}")

    if args.multiply:
        a, b = args.multiply
        result = tm.terry_multiply(a, b)
        print(f"Result: {a} * {b} = {result} (mode: {args.mode})")
    else:
        print("No operation specified. Use --help for options.")

if __name__ == "__main__":
    main()