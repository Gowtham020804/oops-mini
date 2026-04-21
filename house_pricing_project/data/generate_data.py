import random
import numpy as np

def generate_housing_data(n=200):
    sizes = [random.uniform(500, 3000) for _ in range(n)]        # sq.ft
    bedrooms = [random.randint(1, 5) for _ in range(n)]
    ages = [random.uniform(0, 30) for _ in range(n)]

    prices = [
        3000*sizes[i] + 50000*bedrooms[i] - 1000*ages[i] + random.uniform(-20000, 20000)
        for i in range(n)
    ]

    return (
        np.array(sizes),
        np.array(bedrooms),
        np.array(ages),
        np.array(prices)
    )