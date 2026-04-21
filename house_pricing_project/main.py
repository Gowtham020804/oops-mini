import numpy as np
from data.generate_data import generate_housing_data
from models.liner_regression import LinearRegressionNormal
from utils.metrics import mean_squared_error, r2_score

# Generate dataset
sizes, bedrooms, ages, prices = generate_housing_data(200)

# Feature matrix
X = np.column_stack((
    np.ones(len(sizes)),  # bias
    sizes,
    bedrooms,
    ages
))

y = prices

# Train model
model = LinearRegressionNormal()
model.fit(X, y)

# Predict
predictions = model.predict(X)

# Evaluation
mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)

print("Model Performance")
print("MSE:", mse)
print("R2 Score:", r2)

print("\nLearned Parameters:")
print("Bias, Size, Bedrooms, Age =", model.theta)