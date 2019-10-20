package com.example.courtcounter;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;
import android.widget.TextView;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {


    int teamATotalScore = 0;
    int teamBTotalScore = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        displayForTeamA(teamATotalScore);
        displayForTeamB(teamBTotalScore);
    }
    /**
     * Displays the given score for Team A.
     */
    public void displayForTeamA(int score) {
        TextView scoreView = (TextView) findViewById(R.id.team_a_score);
        scoreView.setText(String.valueOf(score));
    }
    public void teamAPlus3(View view) {
        teamATotalScore = teamATotalScore + 3;
        displayForTeamA(teamATotalScore);
    }
    public void teamAPlus2(View view) {
        teamATotalScore = teamATotalScore + 2;
        displayForTeamA(teamATotalScore);
    }
    public void teamAFreeThrow(View view) {
        teamATotalScore = teamATotalScore + 1;
        displayForTeamA(teamATotalScore);
    }

    /**
     * Displays the given score for Team B.
     */
    public void displayForTeamB(int score) {
        TextView scoreView = (TextView) findViewById(R.id.team_b_score);
        scoreView.setText(String.valueOf(score));
    }
    public void teamBPlus3(View view) {
        teamBTotalScore = teamBTotalScore + 3;
        displayForTeamB(teamBTotalScore);
    }
    public void teamBPlus2(View view) {
        teamBTotalScore = teamBTotalScore + 2;
        displayForTeamB(teamBTotalScore);
    }
    public void teamBFreeThrow(View view) {
        teamBTotalScore = teamBTotalScore + 1;
        displayForTeamB(teamBTotalScore);
    }

    public void resetButton(View view) {
        teamATotalScore = 0;
        displayForTeamA(teamATotalScore);
        teamBTotalScore = 0;
        displayForTeamB(teamBTotalScore);
    }

}
