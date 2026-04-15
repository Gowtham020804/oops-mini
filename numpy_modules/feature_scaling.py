import numpy as np

def feature_scaling():

    print("\n--- Feature Scaling Example ---")

    # dataset
    x = np.array(([1,200],
                [2,300]))

    mean = x.mean(axis=0)
    std = x.std(axis=0)

    scaled = (x - mean) / std

    print("Original Data:\n", x)
    print("Mean:", mean)
    print("Standard Deviation:", std)
    print("Scaled Data:\n", scaled)