
/**
* Week 1 - Assignment
* 
* Title: Calculate Pay Program
* Created by: Chongjun Kim
* School: The University of Arizona Global Campus
* Course: CPT307 - Data Structures & Algorithms (INE2206A)
* Instructor: Michael Hayden
* Due Date: 02-07-2022
*/

import javax.swing.*;
import javax.xml.validation.Validator;

import java.awt.*;
import java.awt.event.*;

class MyFrame extends JFrame implements ActionListener {

    // Components of the Form
    private Container c;
    private JLabel title;
    private JLabel name;
    private JTextField tname;
    private JLabel rop;
    private JTextField trop;
    private JLabel hrs;
    private JTextField thrs;
    private JCheckBox term;
    private JButton sub;
    private JButton reset;
    private JTextArea tout;
    private JLabel res;
    private JTextArea resadd;

    // constructor, to initialize the components
    // with default values.
    public MyFrame() {
        setTitle("Calculate Pay Program");
        setBounds(300, 200, 900, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setResizable(false);

        c = getContentPane();
        c.setLayout(null);

        title = new JLabel("Calculate Pay");
        title.setFont(new Font("Arial", Font.PLAIN, 30));
        title.setSize(300, 30);
        title.setLocation(300, 30);
        c.add(title);



        name = new JLabel("Name");
        name.setFont(new Font("Arial", Font.PLAIN, 20));
        name.setSize(150, 30);
        name.setLocation(50, 100);
        c.add(name);

        tname = new JTextField();
        tname.setFont(new Font("Arial", Font.PLAIN, 20));
        tname.setSize(190, 30);
        tname.setLocation(180, 100);
        c.add(tname);

        rop = new JLabel("Rate of pay");
        rop.setFont(new Font("Arial", Font.PLAIN, 20));
        rop.setSize(150, 30);
        rop.setLocation(50, 150);
        c.add(rop);

        trop = new JTextField();
        trop.setFont(new Font("Arial", Font.PLAIN, 20));
        trop.setSize(190, 30);
        trop.setLocation(180, 150);
        c.add(trop);

        hrs = new JLabel("Hours worked");
        hrs.setFont(new Font("Arial", Font.PLAIN, 20));
        hrs.setSize(150, 30);
        hrs.setLocation(50, 200);
        c.add(hrs);

        thrs = new JTextField();
        thrs.setFont(new Font("Arial", Font.PLAIN, 20));
        thrs.setSize(190, 30);
        thrs.setLocation(180, 200);
        c.add(thrs);



        term = new JCheckBox("Accept Terms And Conditions.");
        term.setFont(new Font("Arial", Font.PLAIN, 15));
        term.setSize(250, 20);
        term.setLocation(150, 400);
        c.add(term);

        sub = new JButton("Submit");
        sub.setFont(new Font("Arial", Font.PLAIN, 15));
        sub.setSize(100, 20);
        sub.setLocation(150, 450);
        sub.addActionListener(this);
        c.add(sub);

        reset = new JButton("Reset");
        reset.setFont(new Font("Arial", Font.PLAIN, 15));
        reset.setSize(100, 20);
        reset.setLocation(270, 450);
        reset.addActionListener(this);
        c.add(reset);

        tout = new JTextArea();
        tout.setFont(new Font("Arial", Font.PLAIN, 15));
        tout.setSize(300, 400);
        tout.setLocation(500, 100);
        tout.setLineWrap(true);
        tout.setEditable(false);
        c.add(tout);

        res = new JLabel("");
        res.setFont(new Font("Arial", Font.PLAIN, 20));
        res.setSize(500, 25);
        res.setLocation(100, 500);
        c.add(res);

        resadd = new JTextArea();
        resadd.setFont(new Font("Arial", Font.PLAIN, 15));
        resadd.setSize(200, 75);
        resadd.setLocation(580, 175);
        resadd.setLineWrap(true);
        c.add(resadd);

        setVisible(true);
    }

    public Boolean validateInput (String input) {
        return !input.isBlank();
    }

    // method actionPerformed()
    // to get the action performed
    // by the user and act accordingly
    public void actionPerformed(ActionEvent e) {
        String name = tname.getText();
        String rop = trop.getText();
        String hrs = thrs.getText();

        if (e.getSource() == sub) {
            if (validateInput(name) || validateInput(rop) || validateInput(hrs)) {
                String data = "Employee Name : "
                        + name + "\n"
                        + "Rate of pay : "
                        + rop + "\n"
                        + "Hours worked : "
                        + hrs + "\n";
                tout.setText(data);
                tout.setEditable(false);
                res.setText("Success!!");
            } else {
                tout.setText("");
                resadd.setText("");
                res.setText("Please fill in all the fields.");
            }
        }

        else if (e.getSource() == reset) {
            String def = "";
            tname.setText(def);
            trop.setText(def);
            thrs.setText(def);
            res.setText(def);
            tout.setText(def);
            term.setSelected(false);
            resadd.setText(def);
        }
    }
}

public class CalculatePayProgram {
    public static void main(String[] args) throws Exception {
        MyFrame f = new MyFrame();
    }
}
