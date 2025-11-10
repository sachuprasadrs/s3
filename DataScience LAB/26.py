import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Load dataset
data = load_diabetes()
print("Feature names in the diabetes dataset:\n", data.feature_names)
# Use selected features: age (0), bmi (2), bp (3)
x, y = data.data, data.target
x = x[:, [0, 2, 3]]  # Selecting multiple columns
print("Shape of feature matrix:", x.shape)
# Split into training and testing sets
x_train = x[:-20]
x_test = x[-20:]
y_train = y[:-20]
y_test = y[-20:]
# Create Linear Regression model
c_lr = LinearRegression()
c_lr.fit(x_train, y_train)
# Predict on test set
y_pred = c_lr.predict(x_test)
# Display model parameters
print("\nModel Coefficients:\n", c_lr.coef_)
print("Model Intercept:", c_lr.intercept_)
# Evaluate model
print("\nMean Squared Error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of Determination (R²): %.2f" % r2_score(y_test, y_pred))
# Predict for user-provided input
a = float(input("Enter Age (standardized): "))
b = float(input("Enter BMI (standardized): "))
c = float(input("Enter Blood Pressure (standardized): "))
sample = np.array([[a, b, c]])
pred = c_lr.predict(sample)
print("\nPredicted diabetes progression:", pred[0])
# Optional plot (for one feature visualization, e.g., BMI vs target)
plt.scatter(x_test[:, 1], y_test, color='black', label='Actual (Test Data)')
plt.scatter(x_test[:, 1], y_pred, color='blue', label='Predicted')
plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Linear Regression on Diabetes Dataset (Multiple Features)")
plt.legend()
plt.show()
