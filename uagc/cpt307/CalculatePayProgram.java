
/**
* Week 1 - Assignment
* 
* Title: Calculate Pay Program
* Created by: Chongjun Kim
* School: The University of Arizona Global Campus
* Course: CPT307 - Data Structures & Algorithms (INE2206A)
* Professor: Michael Hayden
* Due Date: 02-07-2022
*/

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.text.*;

class CalculatePayProgramFrame extends JFrame implements ActionListener {

    // default components
    private Container c;
    private JLabel title;
    private JLabel name;
    private JLabel rop;
    private JLabel hrs;
    private JTextField nameField;
    private JFormattedTextField ropField;
    private JTextField hrsField;
    private JButton sub;
    private JButton reset;
    private JTextArea tout;
    private JLabel res;

    // constructor initializing the components
    public CalculatePayProgramFrame() {
        setTitle("Calculate Pay Program"); // window title
        setBounds(300, 200, 780, 500); // window position & size
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setResizable(false);

        c = getContentPane();
        c.setLayout(null);

        // form title
        title = new JLabel("Calculate Weekly Pay");
        title.setFont(new Font("Arial", Font.PLAIN, 30));
        title.setSize(300, 30);
        title.setLocation(240, 30);
        c.add(title);

        // labels
        name = new JLabel("Full Name");
        name.setFont(new Font("Arial", Font.PLAIN, 20));
        name.setSize(150, 30);
        name.setLocation(50, 100);
        c.add(name);

        rop = new JLabel("Rate of pay  $");
        rop.setFont(new Font("Arial", Font.PLAIN, 20));
        rop.setSize(150, 30);
        rop.setLocation(50, 150);
        c.add(rop);

        hrs = new JLabel("Hours worked");
        hrs.setFont(new Font("Arial", Font.PLAIN, 20));
        hrs.setSize(150, 30);
        hrs.setLocation(50, 200);
        c.add(hrs);

        // dollar formatter
        DecimalFormat dollarFormatter = new DecimalFormat("#,###.##");
        dollarFormatter.setMinimumFractionDigits(2);
        dollarFormatter.setMaximumFractionDigits(2);

        // fields
        nameField = new JTextField();
        nameField.setFont(new Font("Arial", Font.PLAIN, 20));
        nameField.setSize(190, 30);
        nameField.setLocation(180, 100);
        c.add(nameField);

        ropField = new JFormattedTextField(dollarFormatter);
        ropField.setFont(new Font("Arial", Font.PLAIN, 20));
        ropField.setSize(190, 30);
        ropField.setLocation(180, 150);
        c.add(ropField);

        hrsField = new JTextField();
        hrsField.setFont(new Font("Arial", Font.PLAIN, 20));
        hrsField.setSize(190, 30);
        hrsField.setLocation(180, 200);
        c.add(hrsField);

        // submit button
        sub = new JButton("Submit");
        sub.setFont(new Font("Arial", Font.PLAIN, 15));
        sub.setSize(100, 20);
        sub.setLocation(100, 300);
        sub.addActionListener(this);
        c.add(sub);

        // reset button
        reset = new JButton("Reset");
        reset.setFont(new Font("Arial", Font.PLAIN, 15));
        reset.setSize(100, 20);
        reset.setLocation(220, 300);
        reset.addActionListener(this);
        c.add(reset);

        // result panel
        tout = new JTextArea();
        tout.setFont(new Font("Arial", Font.PLAIN, 15));
        tout.setSize(300, 310);
        tout.setLocation(400, 100);
        tout.setLineWrap(true);
        tout.setEditable(false);
        c.add(tout);

        res = new JLabel("");
        res.setFont(new Font("Arial", Font.PLAIN, 20));
        res.setSize(500, 25);
        res.setLocation(50, 380);
        c.add(res);

        setVisible(true);
    }

    // validators
    public Boolean validateInput(String input) {
        return !input.isBlank();
    }

    public Boolean validateDoubleInput(Double input) {
        return input != 0;
    }

    public Boolean validateIntegerInput(Integer input) {
        return input != 0;
    }

    public void actionPerformed(ActionEvent e) {
        String name = nameField.getText();
        Double rop = 0.0;
        Integer hrs = 0;
        Double gross;
        Double fed;
        Double state;
        Double medi;
        Double social;
        Double unemp;
        Double deduct;
        Double net;

        // try catch for validating field entry
        try {
            Double.parseDouble(ropField.getText());
            rop = Double.parseDouble(ropField.getText());
        } catch (Exception x) {
            rop = 0.0;
        }

        try {
            Integer.parseInt(hrsField.getText());
            hrs = Integer.parseInt(hrsField.getText());
        } catch (Exception x) {
            hrs = 0;
        }

        // condition for greater than, less than 40 hours
        if (hrs > 40) {
            gross = (Double) (((hrs - 40) * (rop * 1.5)) + (40 * rop));
        } else {
            gross = (Double) (rop * hrs);
        }

        // deductables calcuation
        fed = (Double) (.15 * gross);
        state = (Double) (.0307 * gross);
        medi = (Double) (.0145 * gross);
        social = (Double) (.062 * gross);
        unemp = (Double) (.007 * gross);
        deduct = (Double) (fed + state + medi + social + unemp);

        // net income
        net = (Double) (gross - deduct);

        if (e.getSource() == sub) {
            if (validateInput(name) && validateDoubleInput(rop) && validateIntegerInput(hrs)) {
                DecimalFormat dollarFormatter = new DecimalFormat("$#,###.##");
                dollarFormatter.setMinimumFractionDigits(2);
                dollarFormatter.setMaximumFractionDigits(2);

                String data = " ----------------------------------------------------------" + "\n"
                        + " Employee Name : "
                        + name + "\n"
                        + " Rate of pay : "
                        + dollarFormatter.format(rop) + "\n"
                        + " Hours worked : "
                        + hrs + "\n"
                        + " ----------------------------------------------------------" + "\n"
                        + " Gross Pay : "
                        + dollarFormatter.format(gross) + "\n"
                        + " ----------------------------------------------------------" + "\n"
                        + " Federal Tax : "
                        + dollarFormatter.format(fed) + "\n"
                        + " State Tax : "
                        + dollarFormatter.format(state) + "\n"
                        + " Medicare : "
                        + dollarFormatter.format(medi) + "\n"
                        + " Social Security : "
                        + dollarFormatter.format(social) + "\n"
                        + " Unemployment Insurance : "
                        + dollarFormatter.format(unemp) + "\n"
                        + " ----------------------------------------------------------" + "\n"
                        + " Total Deductions : "
                        + dollarFormatter.format(deduct) + "\n"
                        + " ================================" + "\n"
                        + " Net Pay : "
                        + dollarFormatter.format(net) + "\n"
                        + " ================================" + "\n";
                tout.setText(data);
                tout.setEditable(false);
                res.setText("Success!!");
            } else {
                tout.setText("");
                res.setText("Please fill in all the fields.");
            }
        }
        // reset button action
        else if (e.getSource() == reset) {
            String emtpy = "";
            nameField.setText(emtpy);
            ropField.setValue(null);
            hrsField.setText(emtpy);
            res.setText(emtpy);
            tout.setText(emtpy);
        }
    }
}

public class CalculatePayProgram {
    public static void main(String[] args) throws Exception {
        CalculatePayProgramFrame f = new CalculatePayProgramFrame();
        System.out.println(f != null ? "success" : "failed"); // added println for debugging purposes & avoid warning of
                                                              // variable not being used
    }
}
