import numpy as np

def broadcasting_examples():

    print("\n--- NumPy Broadcasting Examples ---")

    a = np.array([[1,2,3],
                  [4,5,6]])

    print("\nOriginal Matrix:\n", a)

    # Scalar broadcasting
    print("\nScalar Broadcasting (a + 10):")
    print(a + 10)

    # Row broadcasting
    b = np.array([10,20,30])

    print("\nRow Broadcasting:")
    print(a + b)

    # Column broadcasting
    c = np.array([[10],
                [20]])

    print("\nColumn Broadcasting:")
    print(a + c)

    # Different dimension broadcasting
    d = np.array([1,2,3])
    e = np.array([[10],
                [20],
                [30]])

    print("\nDifferent Dimension Broadcasting:")
    print(d + e)