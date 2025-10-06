import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
print("--- Data Loading & Features ---")
print(f"Feature names (Step 5): {diabetes.feature_names}")
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = diabetes_X[:, np.newaxis, 2]
print(f"Shape of the feature matrix (Step 11): {diabetes_X.shape}")
print(f"First 5 feature values (Step 12): \n{diabetes_X[:5]}")

diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(
    diabetes_X, diabetes_y, test_size=0.2, random_state=42
)
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_X_test)
print("\n--- User Prediction ---")
while True:
    try:
        user_bmi_input = float(input("Prompt the user to enter a BMI value (e.g., 0.05): "))
        if -0.2 < user_bmi_input < 0.2:
            break
        else:
            print("Warning: BMI input is outside the typical scaled range (-0.2 to 0.2) for this dataset.")
            break
    except ValueError:
        print("Invalid input. Please enter a numerical value for BMI.")
user_bmi_array = np.array([[user_bmi_input]])
user_prediction = regr.predict(user_bmi_array)

print(f"Prediction for user-entered BMI ({user_bmi_input}):")
print(f"Predicted target variable (s6) is: {user_prediction[0]:.2f}")

print("\n--- Model Evaluation ---")
print(f"Coefficient (Step 27, 28): {regr.coef_[0]:.2f}")
print(f"Mean squared error: {mean_squared_error(diabetes_y_test, diabetes_y_pred):.2f}")
print(f"Coefficient of determination (R-squared, Step 29, 30): {r2_score(diabetes_y_test, diabetes_y_pred):.2f}")

plt.figure(figsize=(8, 6))
plt.scatter(diabetes_X_test, diabetes_y_test, color='black', label='Test Data')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3, label='Linear Regression Fit')
plt.scatter(user_bmi_array, user_prediction, color='red', marker='x', s=100, label=f'User BMI Prediction')
plt.title('Linear Regression on Diabetes (BMI vs Target)')
plt.xlabel('BMI (Scaled Feature)')
plt.ylabel('Target (Disease Progression)')
plt.legend()
plt.grid(True)
plt.show()

