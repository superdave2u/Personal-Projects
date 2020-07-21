package com.example.android.miwok;

public class Word {

    /** Define a variable to store the default translation word **/
    private String mDefaultTranslation;

    /** Defines a variable with the translated word **/
    private String mMiwakTranslation;

    public Word (String DefaultTranslation, String MiwakTranslation) {

        mDefaultTranslation = DefaultTranslation;
        mMiwakTranslation = MiwakTranslation;

    }

    // Fetch the default translated word
    public String getDefaultTranslation(){
        return mDefaultTranslation;
    }

    // Fetch the corresponding translated word
    public String getMiwakTranslation() {
        return mMiwakTranslation;
    }
}
