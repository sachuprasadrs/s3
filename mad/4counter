Program 4: Counter App (Android Java)
A classic Counter App lets the user increment, decrement, and reset a displayed number. This exercise is great for learning UI interaction, variable update, and basic validation logic in Android.

Aim
Create an Android app where the user taps buttons to increment, decrement, or reset a counter, displaying the value live on the screen.

Refined Algorithm
Create UI (activity_main.xml):

Add a TextView for the counter value

Add three Buttons: Increment (+), Decrement (-), Reset

MainActivity.java Logic:

Connect all views using findViewById

Declare an int variable (counter) and initialize to zero

Set click listeners for all buttons:

Increment: increases counter by one

Decrement: decreases counter by one (minimum value can be zero)

Reset: sets counter to zero

Update the TextView whenever the value changes

Optionally show a Toast when counter cannot be decremented below zero

Test app on emulator or device, verify all button actions, and screen updates.

Files to Alter
res/layout/activity_main.xml (UI)

java/com.example.counterapp/MainActivity.java (logic)

Complete Code
1. activity_main.xml
xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="24dp">

    <TextView
        android:id="@+id/counterText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="0"
        android:textSize="48sp"
        android:textStyle="bold"
        android:layout_marginBottom="32dp" />

    <LinearLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="center">

        <Button
            android:id="@+id/incrementBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="+" />
        <Button
            android:id="@+id/decrementBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginLeft="18dp"
            android:text="-" />
        <Button
            android:id="@+id/resetBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginLeft="18dp"
            android:text="Reset" />
    </LinearLayout>

</LinearLayout>
2. MainActivity.java
java
package com.example.counterapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Button;
import android.widget.Toast;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    int counter = 0;
    TextView counterText;
    Button incrementBtn, decrementBtn, resetBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        counterText = findViewById(R.id.counterText);
        incrementBtn = findViewById(R.id.incrementBtn);
        decrementBtn = findViewById(R.id.decrementBtn);
        resetBtn = findViewById(R.id.resetBtn);

        incrementBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                counter++;
                counterText.setText(String.valueOf(counter));
            }
        });
        decrementBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if (counter > 0) {
                    counter--;
                    counterText.setText(String.valueOf(counter));
                } else {
                    Toast.makeText(MainActivity.this, "Counter cannot be less than zero", Toast.LENGTH_SHORT).show();
                }
            }
        });
        resetBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                counter = 0;
                counterText.setText(String.valueOf(counter));
            }
        });
    }
}
Explanation & Key Logic
counterText: Displays current count.

incrementBtn/decrementBtn/resetBtn: Buttons to change value.

Use setText(String.valueOf(counter)) to update display each time.

Error prevention: Do not allow count to go negative. Show a Toast as feedback.

All UI wiring uses findViewById for XML/Java connection.

Non-Repetitive Viva Questions
Q1. What is the role of findViewById in Android apps?

It links XML views/components (like buttons and textviews) to Java variables so you can control them programmatically.

Q2. Why use LinearLayout for arranging buttons horizontally and vertically?

It allows you to stack views vertically in the root layout and horizontally for the button group, giving fine-grained control over arrangement.

Q3. How do you prevent a variable (counter) from going negative?

Use an if condition to check the value before decrementing, and block the operation (or show a warning) if it’s zero.

Q4. When would you show a Toast versus updating the UI?

Toast is best for temporary error/info not shown on screen; UI updates are for persistent data the user tracks visually.

