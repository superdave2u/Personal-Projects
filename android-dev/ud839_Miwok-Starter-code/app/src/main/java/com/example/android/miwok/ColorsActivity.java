package com.example.android.miwok;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;

import java.util.ArrayList;

public class ColorsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.word_list);


        ArrayList<Word> wordsList = new ArrayList<Word>();
        wordsList.add(new Word("red", "weṭeṭṭi"));
        wordsList.add(new Word("green", "chokokki"));
        wordsList.add(new Word("brown", "ṭakaakki"));
        wordsList.add(new Word("gray", "ṭopoppi"));
        wordsList.add(new Word("black", "kululli"));
        wordsList.add(new Word("white", "kelelli"));
        wordsList.add(new Word("dusty yellow", "ṭopiisә"));
        wordsList.add(new Word("mustard yellow", "chiwiiṭә"));


        WordAdapter itemsAdapter = new WordAdapter(this, wordsList);
        ListView listView = (ListView) findViewById(R.id.list);
        listView.setAdapter(itemsAdapter);


    }
}
