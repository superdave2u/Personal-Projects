package com.example.android.miwok;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;

import java.util.ArrayList;

public class PhrasesActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.word_list);


        ArrayList<Word> wordsList = new ArrayList<Word>();
        wordsList.add(new Word("Where are you going?", "minto wuksus"));
        wordsList.add(new Word("What is your name?", "tinnә oyaase'nә"));
        wordsList.add(new Word("My name is...", "oyaaset..."));
        wordsList.add(new Word("How are you feeling?", "michәksәs?"));
        wordsList.add(new Word("I'm feeling good.", "kuchi achit"));
        wordsList.add(new Word("Are you coming?", "әәnәs'aa?"));
        wordsList.add(new Word("Yes, I am coming.", "hәә’ әәnәm"));
        wordsList.add(new Word("I'm coming", "әәnәm"));
        wordsList.add(new Word("Let's go.", "yoowutis"));
        wordsList.add(new Word("Come here.", "әnni'nem"));


        WordAdapter itemsAdapter = new WordAdapter(this, wordsList);
        ListView listView = (ListView) findViewById(R.id.list);
        listView.setAdapter(itemsAdapter);


    }

}
