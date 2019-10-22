package com.example.justjava;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.text.NumberFormat;

/**
 * This app displays an order form to order coffee.
 */
public class MainActivity extends AppCompatActivity {

    int numberOfCoffees = 2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    /**
     * This method is called when the order button is clicked.
     */
    public void submitOrder(View view) {

        CheckBox addWhipCream = (CheckBox) findViewById(R.id.checkbox_whipped_cream);
        CheckBox addChocolate = (CheckBox) findViewById(R.id.checkbox_chocolate);
        EditText nameOfPerson = (EditText) findViewById(R.id.enter_name_view);
        displayMessage(createOrderSummery(nameOfPerson.getText().toString(),
                numberOfCoffees,
                (numberOfCoffees * 5),
                addWhipCream.isChecked(),
                addChocolate.isChecked()));
    }

    public void increment(View view) {
        if ((numberOfCoffees + 1) >= 1 && (numberOfCoffees + 1) <= 5){
            numberOfCoffees += 1;
            displayQuantity(numberOfCoffees);
            displayPrice(numberOfCoffees * 5);
        }else{
            Toast.makeText(this, "You cannot have more than 5 coffees", Toast.LENGTH_SHORT).show();
        }

    }

    public void decrement(View view) {
        if ((numberOfCoffees - 1) >= 1 && (numberOfCoffees - 1) <= 5){
            numberOfCoffees -= 1;
            displayQuantity(numberOfCoffees);
            displayPrice(numberOfCoffees * 5);
        }else{
            Toast.makeText(this, "You cannot order less than 0 coffee", Toast.LENGTH_SHORT).show();
        }

    }

    /**
     * This method displays the given quantity value on the screen.
     */
    private void displayQuantity(int number) {
        TextView quantityTextView = (TextView) findViewById(R.id.quantity_text_view);
        quantityTextView.setText("" + number);
    }

    /**
     * This method displays the given price on the screen.
     */

    private void displayPrice(int number) {
        TextView orderSummeryTextView = (TextView) findViewById(R.id.orderSummeryTextView);
        orderSummeryTextView.setText(NumberFormat.getCurrencyInstance().format(number));
    }
    /**
     * This method displays the given text on the screen.
     */
    private void displayMessage(String message) {
        TextView orderSummeryTextView = (TextView) findViewById(R.id.orderSummeryTextView);
        orderSummeryTextView.setText(message);
    }
    /**
     * Creates the order Summery to be displayed to user.
     * @param personName String value of a person's name who is ordering
     * @param quantity number of items
     * @param priceOfOrder price of total items.
     * @param addWhipCream did user add whip cream to their order?
     * @param addChocolate did user add chocolate to their order?
     * @return string message thanking user.
     */
    private String createOrderSummery(String personName, int quantity, int priceOfOrder, boolean addWhipCream, boolean addChocolate) {
        int calculateTotalPrice = priceOfOrder;

        if (addWhipCream) {
            calculateTotalPrice = calculateTotalPrice + 1;
        }
        if (addChocolate) {
            calculateTotalPrice = calculateTotalPrice + 2;
        }



        return("Name: " + personName + "\n"
                + "Quantity: $" + quantity + "\n"
                + "Total: " + calculateTotalPrice + "\n"
                + "Add Whipped Cream? " + addWhipCream + "\n"
                + "Add Chocolate? " + addChocolate + "\n"
                + "Thank You!");
    }
}
