Program 3: Login + Welcome Screen (Android Java)
Let's build a classic Login form app where successful login takes the user to a new Welcome screen. We’ll cover the refined algorithm, proper file separation, clean Java/XML code, and only fresh viva content you haven't learned yet.

Aim
Create a Login page that validates static credentials; on success, navigate to a Welcome screen (activity) using Intent, passing the username.

Refined Algorithm
Design Login UI (activity_main.xml):

Add EditText for Username and Password

Add Button for Login

Validate credentials in MainActivity.java:

On Login button click, get both inputs

Check for empty fields and show error if needed

Compare user input to preset credentials

If success: use Intent to switch to WelcomeActivity, passing username as extra

If failed: show error Toast

Create Welcome screen (activity_welcome.xml + WelcomeActivity.java):

Get passed username from intent

Display personalized greeting with username

Update AndroidManifest.xml:

Register WelcomeActivity

Test with valid/invalid input & navigation

Files To Alter
res/layout/activity_main.xml (Login UI)

java/com.example.loginapp/MainActivity.java (Login logic)

res/layout/activity_welcome.xml (Welcome UI)

java/com.example.loginapp/WelcomeActivity.java (Display welcome)

AndroidManifest.xml (add WelcomeActivity)

Complete Code
1. activity_main.xml (Login Screen)
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
2. MainActivity.java (Login Logic)
java
package com.example.loginapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Button;
import android.widget.Toast;
import android.view.View;
import android.content.Intent;

public class MainActivity extends AppCompatActivity {
    EditText usernameInput, passwordInput;
    Button loginBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Link UI
        usernameInput = findViewById(R.id.usernameInput);
        passwordInput = findViewById(R.id.passwordInput);
        loginBtn = findViewById(R.id.loginBtn);

        loginBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String username = usernameInput.getText().toString().trim();
                String password = passwordInput.getText().toString().trim();
                if (username.isEmpty() || password.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Please enter both fields", Toast.LENGTH_SHORT).show();
                } else if (username.equals("admin") && password.equals("admin")) {
                    // Move to welcome screen
                    Intent intent = new Intent(MainActivity.this, WelcomeActivity.class);
                    intent.putExtra("USERNAME_KEY", username);
                    startActivity(intent);
                    finish(); // Optional: prevent returning to login
                } else {
                    Toast.makeText(MainActivity.this, "Invalid credentials", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
3. activity_welcome.xml (Welcome Screen UI)
xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="24dp">

    <TextView
        android:id="@+id/welcomeText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="22sp"
        android:textStyle="bold"
        android:text="Welcome!" />

</LinearLayout>
4. WelcomeActivity.java
java
package com.example.loginapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class WelcomeActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_welcome);
        TextView welcomeText = findViewById(R.id.welcomeText);
        String username = getIntent().getStringExtra("USERNAME_KEY");
        if (username != null && !username.isEmpty()) {
            welcomeText.setText("Welcome, " + username + "!");
        } else {
            welcomeText.setText("Welcome!");
        }
    }
}
5. AndroidManifest.xml (Only add one line)
Add below inside your <application> tag:

xml
<activity android:name=".WelcomeActivity" />
Summary of Files Changed
activity_main.xml (Login UI)

MainActivity.java (Login logic)

activity_welcome.xml (Welcome UI)

WelcomeActivity.java (show greeting)

AndroidManifest.xml (register new screen)

Fresh Viva Questions (Skip repeats)
Q1. How do you move from one Activity (screen) to another in Android?

Use an Intent: Intent i = new Intent(CurrentActivity.this, TargetActivity.class); startActivity(i);

Q2. How can you send data (like username) with an Intent?

Attach data using putExtra: i.putExtra("key", value);

Q3. How do you retrieve the sent data in the new Activity?

Use getIntent().getStringExtra("key"); inside onCreate().

Q4. Why do we use finish() after starting WelcomeActivity?

It removes Login Activity from the back stack, so "Back" won’t return to login page.

Q5. Where do you register a new Activity?

In AndroidManifest.xml within <application> using <activity android:name=".WelcomeActivity"/>

Q6. Explain the benefit of using two separate Activities instead of one.

Keeps code modular, improves navigation, and each screen can have distinct design and logic.

