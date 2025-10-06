import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X, y = load_diabetes(return_X_y=True)
X = X[:, [2]] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

try:
    bmi_input = float(input("Enter a BMI value (e.g., 0.05): "))
    if not -0.2 < bmi_input < 0.2:
        print("Warning: BMI input is outside typical scaled range (-0.2 to 0.2).")
except ValueError:
    print("Invalid input. Using default value 0.05.")
    bmi_input = 0.05
user_pred = model.predict([[bmi_input]])
print(f"\nPredicted target for BMI {bmi_input:.2f}: {user_pred[0]:.2f}")
print(f"Model Coefficient: {model.coef_[0]:.2f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")
plt.scatter(X_test, y_test, color='black', label='Test Data')
plt.plot(X_test, y_pred, color='blue', label='Model')
plt.scatter([[bmi_input]], user_pred, color='red', s=100, marker='x', label='User BMI Prediction')
plt.title('BMI vs Disease Progression')
plt.xlabel('BMI (scaled)')
plt.ylabel('Disease Progression')
plt.legend()
plt.grid(True)
plt.show()
