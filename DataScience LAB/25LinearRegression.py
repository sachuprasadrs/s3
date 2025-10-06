import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Load the dataset
diabetes = load_diabetes()
print("Feature names in the diabetes dataset:\n", diabetes.feature_names)
# Use only one feature (BMI)
diabetes_X, diabetes_y = load_diabetes(return_X_y=True)
diabetes_X = diabetes_X[:, np.newaxis, 2]  # Selecting the BMI feature (column index 2)
print("Shape of feature matrix:", diabetes_X.shape)
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
# Create linear regression model
model = LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)
# Make predictions using the testing set
diabetes_y_pred = model.predict(diabetes_X_test)
# Predict for user-provided BMI value
bmi_value = float(input("Enter a BMI value for prediction: "))
bmi_array = np.array([[bmi_value]])
predicted_target = model.predict(bmi_array)
# Output results
print("Predicted target variable for entered BMI:", predicted_target[0])
print("\nModel coefficient:", model.coef_)
print("Model Intercept:", model.intercept_)
print("\nMean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("Coefficient of determination (R²): %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))
# Optional: plot the data
plt.scatter(diabetes_X_test, diabetes_y_test, color='black', label='Actual')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=2, label='Predicted')
plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Linear Regression on Diabetes Dataset (BMI Feature)")
plt.legend()
plt.show()
