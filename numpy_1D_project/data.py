import numpy as np

def generate_marks(num_students=20):
    np.random.seed(42)
    marks = np.random.randint(0, 101, size=num_students)
    return marks
