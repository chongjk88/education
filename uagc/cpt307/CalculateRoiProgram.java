
/**
* Week 5 - Final Project
* 
* Title: Calculate ROI Program
* Created by: Chongjun Kim
* School: The University of Arizona Global Campus
* Course: CPT307 - Data Structures & Algorithms (INE2206A)
* Professor: Michael Hayden
* Due Date: 03-07-2022
*/

import java.awt.*;
import java.awt.event.*;
import java.text.*;
import java.util.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.table.*;

public class CalculateRoiProgram extends JPanel implements ListSelectionListener {

    // default components
    private static JFrame frame;
    private JLabel title;
    private JTable table;
    private DefaultTableModel tableModel;
    private JScrollPane listScrollPane;
    private JPanel topPane;
    private JPanel centerPane;
    private JPanel endPane;
    private JButton addButton;
    private JButton removeButton;
    private JButton deselectButton;
    private JButton printButton;

    public CalculateRoiProgram() {
        super(new BorderLayout());
        title = new JLabel("Return on Investment List");
        title.setFont(new Font("Arial", Font.PLAIN, 24));
        title.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        title.setHorizontalAlignment(JLabel.CENTER);

        Object rowData[][] = {};
        Object columnNames[] = { "Equipment", "Gain", "Cost", "ROI" };
        tableModel = new DefaultTableModel(rowData, columnNames);
        table = new JTable(tableModel);
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION); // allow one selection at a time
        table.getSelectionModel().addListSelectionListener(this); // initiate listener when selecting a row
        table.setAutoCreateRowSorter(true); // allow integrated sorting

        TableRowSorter<?> trs = (TableRowSorter<?>) table.getRowSorter();
        trs.setSortsOnUpdates(true); // allow newly added rows to follow sort order of the selected column

        listScrollPane = new JScrollPane(table); // added scroll for larger list size
        listScrollPane.setBorder(BorderFactory.createEmptyBorder(5, 0, 0, 0));

        addButton = new JButton("Add");
        addButton.setActionCommand("Add");
        addButton.addActionListener(new OpenPrompt());

        removeButton = new JButton("Remove");
        removeButton.setActionCommand("Remove");
        removeButton.addActionListener(new RemoveListener());
        removeButton.setEnabled(false);

        deselectButton = new JButton("Deselect");
        deselectButton.setActionCommand("Deselect");
        deselectButton.addActionListener(new DeselectListener());
        deselectButton.setEnabled(false);

        printButton = new JButton("Print Best to Least ROI");
        printButton.setActionCommand("Print");
        printButton.addActionListener(new PrintListener(table));
        printButton.setEnabled(false);

        topPane = new JPanel();
        topPane.setLayout(new BoxLayout(topPane, BoxLayout.LINE_AXIS)); // utilize BoxLayout
        topPane.add(title);
        topPane.add(addButton);

        endPane = new JPanel();
        endPane.setLayout(new BoxLayout(endPane, BoxLayout.LINE_AXIS));
        endPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        endPane.add(deselectButton);
        endPane.add(Box.createHorizontalStrut(10)); // spacer
        endPane.add(removeButton);
        endPane.add(Box.createHorizontalGlue()); // pushes buttons to each side
        endPane.add(printButton);

        centerPane = new JPanel();
        centerPane.setLayout(new BoxLayout(centerPane, BoxLayout.Y_AXIS));
        centerPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 0, 5));
        centerPane.add(topPane);
        centerPane.add(listScrollPane);

        add(title, BorderLayout.PAGE_START);
        add(centerPane, BorderLayout.CENTER);
        add(endPane, BorderLayout.PAGE_END);
    }

    // print button action listener
    class PrintListener implements ActionListener {
        JTable table;

        public PrintListener(JTable table) {
            this.table = table;
        }

        public void actionPerformed(ActionEvent e) {
            Vector<?> data = ((DefaultTableModel) table.getModel()).getDataVector();
            LinkedList<String[]> list = new LinkedList<String[]>();
            for (Object d : data) {
                String a = String.valueOf(d).replaceAll("[\\[\\]]", ""); // converting Vector Object to String
                String[] myArray = a.split(", "); // generating list via String
                list.push(myArray);
            }

            // sorting best to least ROI using the Collections framework
            Collections.sort(list, (o1, o2) -> (((Double) Double.parseDouble(o2[3].replaceAll("%", "")))
                    .compareTo((Double) Double.parseDouble(o1[3].replaceAll("%", "")))));

            System.out.println("\nOrdered by best to least ROI:");
            for (String[] l : list) {
                System.out.println(Arrays.toString(l)); // printing one by one in sorted order
            }
        }
    }

    // double value validator
    public Boolean validateDoubleInput(Double input) {
        return input != 0;
    }

    // add button action listener
    class OpenPrompt implements ActionListener {
        private Double gain;
        private Double cost;
        private Double roi;

        public void actionPerformed(ActionEvent e) {
            JTextField brand = new JTextField(20);
            JTextField gainField = new JTextField(10);
            JTextField costField = new JTextField(10);
            JPanel myPanel = new JPanel();

            DecimalFormat dollarFormatter = new DecimalFormat("$#,###.##"); // formatting to dollar
            dollarFormatter.setMinimumFractionDigits(2);
            dollarFormatter.setMaximumFractionDigits(2);

            DecimalFormat percentFormatter = new DecimalFormat("#.##%"); // formatting to percentage
            percentFormatter.setMinimumFractionDigits(2);
            percentFormatter.setMaximumFractionDigits(2);

            myPanel.add(new JLabel("Brand:"));
            myPanel.add(brand);
            myPanel.add(Box.createHorizontalStrut(10)); // spacer
            myPanel.add(new JLabel("Gain:"));
            myPanel.add(gainField);
            myPanel.add(Box.createHorizontalStrut(10)); // spacer
            myPanel.add(new JLabel("Cost:"));
            myPanel.add(costField);
            brand.requestFocusInWindow();

            // opening modal to add equipment information
            Integer prompt = JOptionPane.showConfirmDialog(null, myPanel, "Enter Equipment Information",
                    JOptionPane.OK_CANCEL_OPTION, JOptionPane.PLAIN_MESSAGE);


            if (prompt == JOptionPane.OK_OPTION) {
                try {
                    Double.parseDouble(gainField.getText());
                    gain = Double.parseDouble(gainField.getText());
                } catch (Exception x) {
                    gain = 0.0;
                }

                try {
                    Double.parseDouble(costField.getText());
                    cost = Double.parseDouble(costField.getText());
                } catch (Exception x) {
                    cost = 0.0;
                }

                if (!brand.getText().equals("") && !gainField.getText().equals("") && !costField.getText().equals("")) {
                    if (validateDoubleInput(gain) && validateDoubleInput(cost)) {
                        roi = ((gain - cost) / cost); // calculate roi
                        tableModel.addRow(new Object[] { // adding new row
                                brand.getText(),
                                dollarFormatter.format(gain),
                                dollarFormatter.format(cost),
                                percentFormatter.format(roi)
                        });

                        int lastRow = table.convertRowIndexToView(tableModel.getRowCount() - 1);
                        table.getSelectionModel().setSelectionInterval(lastRow, lastRow);
                        table.scrollRectToVisible(table.getCellRect(lastRow, lastRow, true));
                        // table.getRowSorter().convertRowIndexToModel(lastRow);
                    } else {
                        JOptionPane.showMessageDialog(null,
                                "The gain and cost fields must be numeric. Please try again!");
                        actionPerformed(e); // applying recursion to reopen prompt
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Missing information. Please try again!");
                    actionPerformed(e); // applying recursion to reopen prompt
                }
            }
        }
    }

    // remove button action listener
    class RemoveListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            Integer indexModel = table.convertRowIndexToModel(table.getSelectionModel().getAnchorSelectionIndex()); // get original index
            tableModel.removeRow(indexModel); // remove based on index not sorted

            Integer size = table.getRowCount();

            if (size == 0) {
                removeButton.setEnabled(false); // list size and disable button if empty
            }
        }
    }

    // deselect button action listener
    class DeselectListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            table.getSelectionModel().clearSelection(); // clears selection
        }
    }

    // action listener when there is a change in the table's rows
    public void valueChanged(ListSelectionEvent e) { // added as part of the requirement for ListSelectionListener
        if (e.getValueIsAdjusting() == false) {
            if (table.getSelectedRow() == -1) {
                removeButton.setEnabled(false); // disable button if there's no selection
                deselectButton.setEnabled(false);
            } else {
                removeButton.setEnabled(true); // enable buttons when a row is selected
                deselectButton.setEnabled(true);
            }

            if (table.getRowCount() == 0) {
                printButton.setEnabled(false); // disable buttons when there is no row
            } else {
                printButton.setEnabled(true); // enable button when there is at least one row
            }
        }
    }

    // app's main frame ui setup
    private static void CalculateRoiProgramFrame() {
        JComponent newContentPane = new CalculateRoiProgram();
        newContentPane.setOpaque(true); // content panes must be opaque

        frame = new JFrame("Calculate ROI Program");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(300, 200, 400, 300); // window position & size
        frame.setResizable(false);
        frame.setContentPane(newContentPane);
        frame.setVisible(true); // set to show JFrame window
    }

    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                CalculateRoiProgramFrame();
            }
        });
    }
}
