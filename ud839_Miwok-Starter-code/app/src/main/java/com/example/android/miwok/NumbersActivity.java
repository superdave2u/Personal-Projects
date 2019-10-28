package com.example.android.miwok;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class NumbersActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_numbers);

        // Adding English words
        String words [] = new String [] {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"};
        ArrayList<String> wordsList = new ArrayList<>(Arrays.asList("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"));
    }
}
