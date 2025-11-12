Program 1: Login Form (Validation Only)
This program demonstrates a simple login form with field validation and Toast feedback, building on what you've learned and focusing on robust user input handling.

Aim
Create an Android app with username and password fields. Validate entries: show inline errors for empty fields and display Toast feedback for successful and failed logins.

Refurbished Algorithm
Design a login UI (activity_main.xml):

Two EditText fields (username, password)

One Button for login action

In MainActivity.java:

Connect EditText and Button with findViewById

On button click:

Read edit text values

If fields are empty, set inline error on EditText

If both fields are filled:

Check if username/password match preset values (e.g., "admin"/"1234")

Show Toast for success or failure

Test all validation flows

Files to Alter
res/layout/activity_main.xml (UI design)

java/com.example.loginform/MainActivity.java (logic for validation)

Complete Code
1. activity_main.xml
xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="24dp">

    <EditText
        android:id="@+id/usernameInput"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Username"
        android:inputType="textPersonName"
        android:layout_marginBottom="14dp" />

    <EditText
        android:id="@+id/passwordInput"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Password"
        android:inputType="textPassword"
        android:layout_marginBottom="14dp" />

    <Button
        android:id="@+id/loginBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Login" />

</LinearLayout>
2. MainActivity.java
java
package com.example.loginform;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Button;
import android.widget.Toast;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    EditText usernameInput, passwordInput;
    Button loginBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Connect XML views to code
        usernameInput = findViewById(R.id.usernameInput);
        passwordInput = findViewById(R.id.passwordInput);
        loginBtn = findViewById(R.id.loginBtn);

        loginBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String username = usernameInput.getText().toString().trim();
                String password = passwordInput.getText().toString().trim();
                boolean valid = true;
                if (username.isEmpty()) {
                    usernameInput.setError("Username required");
                    valid = false;
                }
                if (password.isEmpty()) {
                    passwordInput.setError("Password required");
                    valid = false;
                }
                if (valid) {
                    if (username.equals("admin") && password.equals("1234")) {
                        Toast.makeText(MainActivity.this, "Login Successful", Toast.LENGTH_SHORT).show();
                    } else {
                        Toast.makeText(MainActivity.this, "Invalid Credentials", Toast.LENGTH_SHORT).show();
                    }
                }
            }
        });
    }
}
Explanation & Key Logic
setError(): Shows inline error in the EditText if fields are blank.

Toast feedback: Brief popups show the result of login.

Validation logic: Ensures both fields are filled before checking credentials.

Fresh Viva Questions
Q1. How do you show an inline error message below an EditText field in Android?
Use editText.setError("Message") which displays an error directly within the textbox until corrected.

Q2. Why do we use .trim() when reading EditText values?
It removes leading/trailing spaces the user might accidentally add, improving reliability of input checks.

Q3. How can you provide instant feedback for empty fields before form submission?
Call setError() on the EditText if it’s empty during validation, so the user sees the problem immediately.
