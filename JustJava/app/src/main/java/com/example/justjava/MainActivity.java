package com.example.justjava;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.TextView;
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
        displayMessage(createOrderSummery(numberOfCoffees, (numberOfCoffees * 5)));
    }

    public void increment(View view) {
        numberOfCoffees = numberOfCoffees + 1;
        displayQuantity(numberOfCoffees);
        displayPrice(numberOfCoffees * 5);
    }

    public void decrement(View view) {
        numberOfCoffees = numberOfCoffees - 1;
        displayQuantity(numberOfCoffees);
        displayPrice(numberOfCoffees * 5);
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
        TextView priceTextView = (TextView) findViewById(R.id.price_text_view);
        priceTextView.setText(NumberFormat.getCurrencyInstance().format(number));
    }
    /**
     * This method displays the given text on the screen.
     */
    private void displayMessage(String message) {
        TextView priceTextView = (TextView) findViewById(R.id.price_text_view);
        priceTextView.setText(message);
    }

    /**
     * Creates the order Summery to be displayed to user.
     * @param quantity number of items
     * @param priceOfOrder price of total items.
     * @return string message thanking user.
     */
    private String createOrderSummery(int quantity, int priceOfOrder) {
        return("Name: Kaptain Kunal\n"
                + "Quantity: " + quantity + "\n"
                + "Total: " + priceOfOrder + "\n"
                + "Thank You!");
    }
}
