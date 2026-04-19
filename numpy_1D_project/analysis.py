import numpy as np

def calculate_average(marks):
    return np.mean(marks)

def find_topper(marks):
    return np.max(marks)

def find_lowest(marks):
    return np.min(marks)

def calculate_std(marks):
    return np.std(marks)

def count_pass_fail(marks, pass_mark=40):
    passed = np.sum(marks >= pass_mark)
    failed = np.sum(marks < pass_mark)
    return passed, failed