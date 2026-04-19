import numpy as np

def display_marks(marks):
    print("Student Marks:", marks)

def sort_marks(marks):
    return np.sort(marks)

def get_pass_fail(marks, pass_mark=40):
    return np.where(marks >= pass_mark, "Pass", "Fail")