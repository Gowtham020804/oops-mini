import numpy as np

class LinearRegressionNormal:
    def __init__(self):
        self.theta = None

    def fit(self, X, y):
        # Normal Equation
        self.theta = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self, X):
        return X @ self.theta