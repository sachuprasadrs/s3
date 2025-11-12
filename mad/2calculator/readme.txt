Program 2: Simple Calculator App (Custom Keypad)
Aim
To design an Android app that presents a calculator interface using only button input (number keys, basic operators, clear, backspace). Tap buttons to build an arithmetic expression, use clear/backspace for corrections, and display the evaluated result.

Refurbished Algorithm (Stepwise)
Start a new Android project (CalculatorApp) with an Empty Activity.

In activity_main.xml:

Use a vertical layout centered (android:gravity="center").

Place a TextView at the top for display.

Use a GridLayout for a keypad:

Four rows: numbers (7–9, 4–6, 1–3, C/0/⌫/+/-/*//)

Operators and action keys (division, multiplication, subtraction, addition, equals, clear, backspace).

Swap the positions of clear and 0, placing "0" at bottom-left.

Center align all buttons and display.

In MainActivity.java:

Link TextView and all button views using findViewById.

Maintain a string for current expression.

On button tap, append digits/operators appropriately.

Backspace = delete last character. Clear = reset input.

On "=": evaluate the arithmetic expression and display result.

Handle invalid expressions/divide by zero by showing "Error".

Test all possible input sequences including erase/correction.

Files to Alter
res/layout/activity_main.xml (UI keypad, display, button arrangement)

java/com.example.calculatorapp/MainActivity.java (logic for input/build/evaluate)

Complete Code
1. activity_main.xml
xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="14dp">

    <TextView
        android:id="@+id/display"
        android:layout_width="match_parent"
        android:layout_height="90dp"
        android:text="0"
        android:textSize="32sp"
        android:gravity="center"
        android:background="#222"
        android:textColor="#fff"
        android:padding="16dp"
        android:layout_marginBottom="8dp" />

    <GridLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:columnCount="4"
        android:rowCount="5"
        android:gravity="center">
        <!-- Row 1 -->
        <Button android:id="@+id/btn7" android:text="7" />
        <Button android:id="@+id/btn8" android:text="8" />
        <Button android:id="@+id/btn9" android:text="9" />
        <Button android:id="@+id/btnDiv" android:text="/" />
        <!-- Row 2 -->
        <Button android:id="@+id/btn4" android:text="4" />
        <Button android:id="@+id/btn5" android:text="5" />
        <Button android:id="@+id/btn6" android:text="6" />
        <Button android:id="@+id/btnMul" android:text="*" />
        <!-- Row 3 -->
        <Button android:id="@+id/btn1" android:text="1" />
        <Button android:id="@+id/btn2" android:text="2" />
        <Button android:id="@+id/btn3" android:text="3" />
        <Button android:id="@+id/btnSub" android:text="-" />
        <!-- Row 4: Swapped 'C' and '0' -->
        <Button android:id="@+id/btn0" android:text="0" />
        <Button android:id="@+id/btnClear" android:text="C" />
        <Button android:id="@+id/btnBack" android:text="⌫" />
        <Button android:id="@+id/btnAdd" android:text="+" />
        <!-- Row 5: Equals button, rest empty for symmetry -->
        <View android:layout_width="0dp" android:layout_height="0dp" />
        <View android:layout_width="0dp" android:layout_height="0dp" />
        <View android:layout_width="0dp" android:layout_height="0dp" />
        <Button android:id="@+id/btnEq" android:text="=" />
    </GridLayout>

</LinearLayout>
2. MainActivity.java
java
package com.example.calculatorapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    TextView display;
    String currentInput = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        display = findViewById(R.id.display);

        int[] numIds = {R.id.btn0,R.id.btn1,R.id.btn2,R.id.btn3,R.id.btn4,R.id.btn5,R.id.btn6,R.id.btn7,R.id.btn8,R.id.btn9};
        int[] opIds = {R.id.btnAdd, R.id.btnSub, R.id.btnMul, R.id.btnDiv};
        Button btnEq = findViewById(R.id.btnEq);
        Button btnClear = findViewById(R.id.btnClear);
        Button btnBack = findViewById(R.id.btnBack);

        for(int i=0; i<=9; i++) {
            Button b = findViewById(numIds[i]);
            final int fi = i;
            b.setOnClickListener(v -> {
                currentInput += String.valueOf(fi);
                updateDisplay();
            });
        }
        for(int id : opIds) {
            Button opBtn = findViewById(id);
            opBtn.setOnClickListener(v -> {
                String op = ((Button)v).getText().toString();
                if (currentInput.isEmpty()) return;
                char last = currentInput.charAt(currentInput.length() - 1);
                if (last=='+'||last=='-'||last=='*'||last=='/') return;
                currentInput += op;
                updateDisplay();
            });
        }
        btnEq.setOnClickListener(v -> {
            if (currentInput.isEmpty()) return;
            try {
                double result = eval(currentInput);
                display.setText(String.valueOf(result));
                currentInput = "";
            } catch (Exception e) {
                display.setText("Error");
                currentInput = "";
            }
        });
        btnClear.setOnClickListener(v -> {
            currentInput = "";
            updateDisplay();
        });
        btnBack.setOnClickListener(v -> {
            if (!currentInput.isEmpty()) {
                currentInput = currentInput.substring(0, currentInput.length() - 1);
                updateDisplay();
            }
        });
    }
    private void updateDisplay() {
        display.setText(currentInput.isEmpty() ? "0" : currentInput);
    }
    private double eval(String expr) {
        double result = 0;
        char lastOp = '+';
        int i=0, n=expr.length();
        String num = "";
        while(i<n){
            char c = expr.charAt(i);
            if(Character.isDigit(c)) num+=c;
            else if(c=='+'||c=='-'||c=='*'||c=='/'){
                if(num.isEmpty()) throw new RuntimeException();
                double val = Double.parseDouble(num);
                result = applyOp(result, val, lastOp);
                lastOp = c;
                num = "";
            }
            i++;
        }
        if(!num.isEmpty()) result = applyOp(result, Double.parseDouble(num), lastOp);
        return result;
    }
    private double applyOp(double a, double b, char op){
        switch(op){
            case '+': return a+b;
            case '-': return a-b;
            case '*': return a*b;
            case '/': if(b==0) throw new ArithmeticException(); return a/b;
        }
        return b;
    }
}
Explanation of Key Lines
UI Alignment: Outer LinearLayout and GridLayout centered; TextView content is centered via android:gravity="center".

Button Swapping: The "0" button is now bottom-left, "C" next to it.

Input Logic: Button clicks build a string, backspace erases last, clear resets.

Evaluation: Simple left-to-right; errors handled as "Error".

Viva Questions (Non-Repetitive)
Q1. How would you center all the calculator's display and buttons in the layout?

Set android:gravity="center" for parent LinearLayout, GridLayout, and the TextView.

Q2. How do you swap the positions of two buttons in a GridLayout?

Change their order in the XML: put the desired button as the first/last child in its row.

Q3. What is the role of the backspace and clear buttons?

Backspace deletes the last character of input, clear resets the expression to empty.

Q4. How does the calculator app prevent two operators from being entered consecutively?

In code, check the last character before appending a new operator; if it's already an operator, ignore the input.

Q5. If result is 'Error', what could have happened?

User tried an invalid calculation, e.g., dividing by zero or entering an invalid expression.

Q6. What file would you update to change button arrangement?

The XML layout file: activity_main.xml.

