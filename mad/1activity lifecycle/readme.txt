
Program 1: Activity Lifecycle
Let's start with Program 1: Activity Lifecycle - a comprehensive deep-dive into theory, refined algorithm, complete code, files altered, and all viva questions covered.​

Aim
To demonstrate the Android Activity Lifecycle by displaying Toast messages at each lifecycle stage (onCreate, onStart, onResume, onPause, onStop, onDestroy, onRestart).​

Theory & Concepts
What is Activity Lifecycle?
The Activity Lifecycle represents the sequence of states an activity goes through from creation to destruction. Android provides callback methods at each stage to manage resources efficiently.​

Lifecycle Methods:

Method	When Called	Purpose
onCreate()	Activity is first created	Initialize UI, set layout, declare variables ​
onStart()	Activity becomes visible	Prepare resources needed when visible ​
onResume()	Activity is interactive	Start animations, resume operations ​
onPause()	Another activity comes to foreground	Pause operations, save data ​
onStop()	Activity no longer visible	Release heavy resources ​
onDestroy()	Activity is destroyed	Final cleanup before termination ​
onRestart()	Activity restarts after being stopped	Re-initialize stopped resources ​
Refined Algorithm
text
1. Open Android Studio → Create New Project → Empty Activity
2. Set project name as "ActivityLifecycleDemo"
3. In MainActivity.java:
   a. Override all 7 lifecycle methods
   b. Inside each method:
      - Call super method first
      - Display Toast with method name
      - Log message to Logcat
4. In activity_main.xml:
   a. Add TextView showing "Activity Lifecycle Demo"
   b. Add instructional text for user actions
5. Run the app and observe:
   - App launch → onCreate → onStart → onResume
   - Press Home → onPause → onStop
   - Return to app → onRestart → onStart → onResume
   - Press Back → onPause → onStop → onDestroy
6. Verify Toast messages and Logcat output at each stage
Files to Alter
Project Structure:

text
app/
├── manifests/
│   └── AndroidManifest.xml (auto-configured)
├── java/com.example.activitylifecycle/
│   └── MainActivity.java (PRIMARY FILE - add lifecycle methods)
├── res/
│   └── layout/
│       └── activity_main.xml (SECONDARY FILE - simple UI)
Complete Code
File 1: activity_main.xml
xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="20dp">

    <TextView
        android:id="@+id/titleText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Activity Lifecycle Demo"
        android:textSize="24sp"
        android:textStyle="bold"
        android:textColor="#000000"/>

    <TextView
        android:id="@+id/instructionText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Press Home, Back, or switch apps to see lifecycle methods"
        android:textSize="16sp"
        android:textAlignment="center"
        android:layout_marginTop="20dp"/>

</LinearLayout>
Purpose: Simple UI showing title and instructions. The real action happens in Java code.​

File 2: MainActivity.java
java
package com.example.activitylifecycle;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    // Tag for Logcat filtering
    private static final String TAG = "ActivityLifecycle";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // Show Toast and log
        Toast.makeText(this, "onCreate() called", Toast.LENGTH_SHORT).show();
        Log.d(TAG, "onCreate() - Activity is being created");
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast.makeText(this, "onStart() called", Toast.LENGTH_SHORT).show();
        Log.d(TAG, "onStart() - Activity is now visible");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Toast.makeText(this, "onResume() called", Toast.LENGTH_SHORT).show();
        Log.d(TAG, "onResume() - Activity is interactive");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast.makeText(this, "onPause() called", Toast.LENGTH_SHORT).show();
        Log.d(TAG, "onPause() - Activity is partially hidden");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Toast.makeText(this, "onStop() called", Toast.LENGTH_SHORT).show();
        Log.d(TAG, "onStop() - Activity is no longer visible");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast.makeText(this, "onRestart() called", Toast.LENGTH_SHORT).show();
        Log.d(TAG, "onRestart() - Activity is restarting");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Toast.makeText(this, "onDestroy() called", Toast.LENGTH_SHORT).show();
        Log.d(TAG, "onDestroy() - Activity is being destroyed");
    }
}
Line-by-Line Explanation
Line	Code	Explanation
1-6	Package & imports	Declares package and imports AppCompatActivity, Bundle, Toast, Log ​
8	public class MainActivity	Main activity class extending AppCompatActivity ​
10-11	private static final String TAG	Constant for filtering Logcat messages ​
13-19	onCreate()	First method called; sets layout and initializes UI ​
15	setContentView(R.layout.activity_main)	Links XML layout to Java activity ​
17	Toast.makeText()	Displays temporary popup message ​
18	Log.d(TAG, ...)	Writes debug message to Logcat console ​
21-26	onStart()	Called when activity becomes visible to user ​
28-33	onResume()	Called when activity is ready for user interaction ​
35-40	onPause()	Called when another activity partially covers this one ​
42-47	onStop()	Called when activity is completely hidden ​
49-54	onRestart()	Called when activity restarts after being stopped ​
56-61	onDestroy()	Called before activity is destroyed; final cleanup ​
Viva Questions & Answers
Q1: What is the Activity Lifecycle in Android?
A: The Activity Lifecycle is the sequence of states an activity goes through from creation to destruction, including onCreate, onStart, onResume, onPause, onStop, onDestroy, and onRestart.​

Q2: What is the use of each lifecycle callback?
A:

onCreate(): Initialize components, set layout​

onStart(): Activity becomes visible​

onResume(): Activity is interactive​

onPause(): Another activity comes to foreground; pause tasks​

onStop(): Activity no longer visible; release resources​

onDestroy(): Final cleanup before termination​

onRestart(): Restarts after being stopped​

Q3: When is onCreate() called?
A: onCreate() is called when the activity is first created. It's used to initialize UI elements and data.​

Q4: What's the difference between onPause() and onStop()?
A: onPause() is called when the activity is partially visible (e.g., dialog appears), while onStop() is called when the activity is completely invisible.​

Q5: Why should we call super methods in lifecycle callbacks?
A: Calling super methods ensures the parent class (AppCompatActivity) performs its necessary operations before your custom code executes.​

Q6: What is Toast in Android?
A: Toast is used to display brief information messages that appear temporarily and disappear automatically without blocking user interaction.​

Q7: What is Logcat?
A: Logcat is a command-line tool and window in Android Studio used to view log messages generated by the system and apps, useful for debugging.​

Q8: What happens when user presses the Back button?
A: The activity goes through onPause() → onStop() → onDestroy(), completely terminating the activity.​

Q9: What happens when user presses the Home button?
A: The activity goes through onPause() → onStop(), but remains in memory.​

Q10: What is the R class?
A: The R class is an auto-generated class that stores resource IDs for all resources in the project, allowing access via syntax like R.layout.activity_main.​

Testing Steps
Run the app → Observe onCreate → onStart → onResume Toast messages

Press Home button → Observe onPause → onStop

Return to app → Observe onRestart → onStart → onResume

Press Back button → Observe onPause → onStop → onDestroy

Check Logcat for detailed logs with TAG "ActivityLifecycle"
