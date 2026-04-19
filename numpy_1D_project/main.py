from data import generate_marks
from utils import display_marks, sort_marks, get_pass_fail
from analysis import *

def main():
    marks = generate_marks()

    display_marks(marks)

    print("\nSorted Marks:", sort_marks(marks))

    print("\nAverage Marks:", calculate_average(marks))
    print("Topper Marks:", find_topper(marks))
    print("Lowest Marks:", find_lowest(marks))
    print("Standard Deviation:", calculate_std(marks))

    passed, failed = count_pass_fail(marks)
    print(f"\nPassed: {passed}, Failed: {failed}")

    print("\nPass/Fail Status:", get_pass_fail(marks))

if __name__ == "__main__":
    main()