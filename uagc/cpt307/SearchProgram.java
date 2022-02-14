
/**
* Week 2 - Assignment
* 
* Title: Search Program
* Created by: Chongjun Kim
* School: The University of Arizona Global Campus
* Course: CPT307 - Data Structures & Algorithms (INE2206A)
* Professor: Michael Hayden
* Due Date: 02-14-2022
*/

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class SearchProgramFrame extends JFrame implements ActionListener {

    // default components
    private Container c;
    private JLabel title;
    private JLabel searchKey;
    private JTextField searchKeyField;
    private JButton submit;
    private JButton reset;
    private JLabel resultText;

    // constructor initializing the components
    public SearchProgramFrame() {
        setTitle("Search Program"); // window title
        setBounds(300, 200, 400, 350); // window position & size
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setResizable(false);

        c = getContentPane();
        c.setLayout(null);

        // form title
        title = new JLabel("Binary Search");
        title.setFont(new Font("Arial", Font.PLAIN, 30));
        title.setSize(300, 30);
        title.setLocation(100, 30);
        c.add(title);

        // labels
        searchKey = new JLabel("Search");
        searchKey.setFont(new Font("Arial", Font.PLAIN, 20));
        searchKey.setSize(150, 30);
        searchKey.setLocation(50, 100);
        c.add(searchKey);

        // fields
        searchKeyField = new JTextField();
        searchKeyField.setFont(new Font("Arial", Font.PLAIN, 20));
        searchKeyField.setSize(190, 30);
        searchKeyField.setLocation(130, 100);
        searchKeyField.addActionListener(this); // enable 'enter' keypress
        c.add(searchKeyField);

        // submit button
        submit = new JButton("Submit");
        submit.setFont(new Font("Arial", Font.PLAIN, 15));
        submit.setSize(100, 20);
        submit.setLocation(80, 170);
        submit.addActionListener(this);
        c.add(submit);

        // reset button
        reset = new JButton("Reset");
        reset.setFont(new Font("Arial", Font.PLAIN, 15));
        reset.setSize(100, 20);
        reset.setLocation(200, 170);
        reset.addActionListener(this);
        c.add(reset);

        // result text
        resultText = new JLabel("");
        resultText.setFont(new Font("Arial", Font.PLAIN, 20));
        resultText.setSize(400, 25);
        resultText.setLocation(0, 230);
        resultText.setHorizontalAlignment(JTextField.CENTER);
        c.add(resultText);

        setVisible(true);
    }

    // validator
    public Boolean validateIntegerInput(Integer input) {
        return input != 0;
    }

    public Integer binarySearch(Integer numbers[], Integer l, Integer r, Integer v) {
        if (r >= l) {
            Integer mid = l + (r - l) / 2;

            if (numbers[mid] == v) // check middle number
                return mid;

            // search left if the value is lower than the middle number
            if (numbers[mid] > v)
                return binarySearch(numbers, l, mid - 1, v);

            // otherwise search the right of the middle number
            return binarySearch(numbers, mid + 1, r, v);
        }

        // return false when there is no matching value
        return -1;
    }

    public void actionPerformed(ActionEvent e) {
        Integer searchKey = 0;
        Integer numbers[] = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70 };
        Integer size = numbers.length;

        try {
            Integer.parseInt(searchKeyField.getText());
            searchKey = Integer.parseInt(searchKeyField.getText());
        } catch (Exception x) {
            searchKey = 0;
        }

        if (e.getSource() == submit || e.getSource() == searchKeyField) {
            if (validateIntegerInput(searchKey)) {

                Integer result = binarySearch(numbers, 0, size - 1, searchKey);
                if (result == -1)
                    resultText.setText(searchKey + " was not found.");
                else
                    resultText.setText(searchKey + " was found.");

            } else {
                resultText.setText("Please fill in a number.");
            }
        }
        // reset button action
        else if (e.getSource() == reset) {
            String emtpy = "";
            searchKeyField.setText(emtpy);
            resultText.setText(emtpy);
        }
    }
}

public class SearchProgram {
    public static void main(String[] args) throws Exception {
        SearchProgramFrame f = new SearchProgramFrame();

        // debugging purposes & avoid warning of variable not being used
        System.out.println(f != null ? "success" : "failed");
    }
}
