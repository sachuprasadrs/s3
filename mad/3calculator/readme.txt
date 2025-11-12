Program 3: Simple Calculator App (Android Java)
Aim
To design an Android app that allows the user to enter two numbers and perform basic arithmetic operations (add, subtract, multiply, divide), displaying the result.

Algorithm (Refurbished & Stepwise)
Start a new Android project ("CalculatorApp") with an Empty Activity.

In activity_main.xml:

Place two EditText fields for number input (with inputType="numberDecimal").

Add four Button views for addition, subtraction, multiplication, and division (arranged horizontally).

Add a TextView to display the result.

In MainActivity.java:

Link XML widgets (EditText, Button, TextView) to Java variables using findViewById().

Add OnClickListener to each button.

On button press:

Read numbers from the EditTexts as double.

Perform the selected operation.

Display the result in the TextView.

Handle invalid input (e.g., division by zero, empty fields) by showing a Toast.

Test the app with valid and invalid inputs, checking all operations and displaying user-friendly error messages as needed.

Files to Alter
res/layout/activity_main.xml (UI design)

java/com.example.calculatorapp/MainActivity.java (logic for calculator)

No changes are needed to the manifest or Gradle files for a simple app like this.

Complete Code (Concise & Commented)
1. activity_main.xml
xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="24dp">

    <EditText
        android:id="@+id/number1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter first number"
        android:inputType="numberDecimal"
        android:layout_marginBottom="12dp" />

    <EditText
        android:id="@+id/number2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter second number"
        android:inputType="numberDecimal"
        android:layout_marginBottom="16dp" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="center">

        <Button
            android:id="@+id/addButton"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="+" />
        <Button
            android:id="@+id/subtractButton"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="-" />
        <Button
            android:id="@+id/multiplyButton"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="×" />
        <Button
            android:id="@+id/divideButton"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="÷" />
    </LinearLayout>

    <TextView
        android:id="@+id/resultText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Result will appear here"
        android:textSize="20sp"
        android:layout_marginTop="18dp"
        android:gravity="center" />

</LinearLayout>
2. MainActivity.java
java
package com.example.calculatorapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    EditText number1, number2;
    Button addButton, subtractButton, multiplyButton, divideButton;
    TextView resultText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Connect UI to code
        number1 = findViewById(R.id.number1);
        number2 = findViewById(R.id.number2);
        addButton = findViewById(R.id.addButton);
        subtractButton = findViewById(R.id.subtractButton);
        multiplyButton = findViewById(R.id.multiplyButton);
        divideButton = findViewById(R.id.divideButton);
        resultText = findViewById(R.id.resultText);

        addButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                calculate("add");
            }
        });
        subtractButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                calculate("sub");
            }
        });
        multiplyButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                calculate("mul");
            }
        });
        divideButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                calculate("div");
            }
        });
    }

    // Perform calculation with error handling
    private void calculate(String op) {
        String s1 = number1.getText().toString().trim();
        String s2 = number2.getText().toString().trim();
        if (s1.isEmpty() || s2.isEmpty()) {
            Toast.makeText(this, "Enter both numbers", Toast.LENGTH_SHORT).show();
            return;
        }
        try {
            double n1 = Double.parseDouble(s1);
            double n2 = Double.parseDouble(s2);
            double res = 0;
            switch (op) {
                case "add": res = n1 + n2; break;
                case "sub": res = n1 - n2; break;
                case "mul": res = n1 * n2; break;
                case "div":
                    if (n2 == 0) {
                        Toast.makeText(this, "Cannot divide by zero", Toast.LENGTH_SHORT).show();
                        return;
                    }
                    res = n1 / n2;
                    break;
            }
            resultText.setText("Result: " + res);
        } catch (NumberFormatException e) {
            Toast.makeText(this, "Invalid input", Toast.LENGTH_SHORT).show();
        }
    }
}
Explanation of Key Lines (with context)
EditText & Button Linking:

number1 = findViewById(R.id.number1); connects XML input to your Java variable.

Reading Input:

number1.getText().toString() fetches user input as String.

Event Listeners:

Each button's setOnClickListener triggers calculate() with the right operation.

Calculation & Validation:

Check for empty fields, parse numbers, prevent division by zero, catch input errors.

Display Result:

resultText.setText(...) updates the result display.

Error Handling:

Toast.makeText() shows messages for invalid entries.

Possible Viva Questions (Non-Repetitive)
Q1. How do you connect an EditText from XML to Java code?

Use findViewById(R.id.editTextId); to get a reference to the input field in Java.

Q2. How do you ensure only numbers are entered?

In XML, set android:inputType="numberDecimal" for EditText fields.

Q3. How can you handle a division-by-zero error?

Check if the denominator is zero before performing division and show an error message if it is.

Q4. What is NumberFormatException and why is it handled?

NumberFormatException occurs when input cannot be parsed to a number; handling it prevents app crashes due to bad input.

Q5. Why do we use setOnClickListener for the buttons?

To define the specific operation that should run when the user taps an arithmetic button.

Q6. How do you show concise feedback for invalid input?

Use a Toast: Toast.makeText(this, "Invalid input", Toast.LENGTH_SHORT).show();
