package com.example.android.miwok;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ListView;

import java.util.ArrayList;

public class NumbersActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.word_list);


        ArrayList<Word> wordsList = new ArrayList<Word>();
        wordsList.add(new Word("one", "lutti"));
        wordsList.add(new Word("two", "otiiko"));
        wordsList.add(new Word("three", "tolookosu"));
        wordsList.add(new Word("four", "oyyisa"));
        wordsList.add(new Word("five", "massokka"));
        wordsList.add(new Word("six", "temmokka"));
        wordsList.add(new Word("seven", "kenekaku"));
        wordsList.add(new Word("eight", "kawinta"));
        wordsList.add(new Word("nine", "wo’e"));
        wordsList.add(new Word("ten", "na’aacha"));


        WordAdapter itemsAdapter = new WordAdapter(this, wordsList);
        ListView listView = (ListView) findViewById(R.id.list);
        listView.setAdapter(itemsAdapter);


    }

}
