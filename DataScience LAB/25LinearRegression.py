import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Load the dataset
data = load_diabetes()
print("Feature names in the diabetes dataset:\n", data.feature_names)
# Use only one feature (BMI)
x, y = load_diabetes(return_X_y=True)
x = x[:, np.newaxis, 2]  # Selecting BMI feature (column index 2)
print("Shape of feature matrix:", x.shape)
# Split into training/testing sets
x_train = x[:-20]
x_test = x[-20:]
y_train = y[:-20]
y_test = y[-20:]
# Create Linear Regression model
c_lr = LinearRegression()
c_lr.fit(x_train, y_train)
# Predict on test set
y_pred = c_lr.predict(x_test)
# Predict for user-provided BMI value
bmi = float(input("Enter a BMI value for prediction: "))
sample = np.array([[bmi]])
pred = c_lr.predict(sample)
# Output results
print("Predicted target variable for entered BMI:", pred[0])
print("\nModel Coefficient:", c_lr.coef_)
print("Model Intercept:", c_lr.intercept_)
print("\nMean Squared Error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of Determination (R²): %.2f" % r2_score(y_test, y_pred))
# Plot
plt.scatter(x_test, y_test, color='black', label='Actual')
plt.plot(x_test, y_pred, color='blue', linewidth=2, label='Predicted')
plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Linear Regression on Diabetes Dataset (BMI Feature)")
plt.legend()
plt.show()
