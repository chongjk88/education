
/**
* Week 3 - Assignment
* 
* Title: Sorted List Program
* Created by: Chongjun Kim
* School: The University of Arizona Global Campus
* Course: CPT307 - Data Structures & Algorithms (INE2206A)
* Professor: Michael Hayden
* Due Date: 02-21-2022
*/

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.event.*;

public class SortedListProgram extends JPanel implements ListSelectionListener {

    // default components
    private JLabel title;
    private JList<String> list;
    private DefaultListModel<String> listModel;
    private JScrollPane listScrollPane;
    private JPanel topPane;
    private JPanel centerPane;
    private JPanel endPane;
    private JTextField freeForm;
    private JButton addButton;
    private JCheckBox firstPlace;
    private JButton removeButton;
    private JButton deselectButton;
    private AddListener addListener;

    public SortedListProgram() {
        super(new BorderLayout());
        title = new JLabel("List Management Tool");
        title.setFont(new Font("Arial", Font.PLAIN, 24));
        title.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        title.setHorizontalAlignment(JLabel.CENTER);

        listModel = new DefaultListModel<>();
        String[] week = { "Monday", "Tuesday", "Wednesday" };
        // "Thursday", "Friday", "Saturday", "Sunday" left out to allow user to add
        Integer v = 0;
        while (v < week.length) {
            listModel.addElement(week[v]);
            v++;
        }

        list = new JList<>(listModel);
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION); // allow one selection at a time
        list.addListSelectionListener(this);
        list.setFont(new Font("Arial", Font.PLAIN, 18));
        list.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

        listScrollPane = new JScrollPane(list); // added scroll for larger list size
        listScrollPane.setBorder(BorderFactory.createEmptyBorder(5, 0, 0, 0));

        firstPlace = new JCheckBox("Add to top"); // checkbox for top placement when adding

        addButton = new JButton("Add");
        addListener = new AddListener(addButton);
        addButton.setActionCommand("Add");
        addButton.addActionListener(addListener);
        addButton.setEnabled(false);

        removeButton = new JButton("Remove");
        removeButton.setActionCommand("Remove");
        removeButton.addActionListener(new RemoveListener());
        removeButton.setEnabled(false);

        deselectButton = new JButton("Deselect");
        deselectButton.setActionCommand("Deselect");
        deselectButton.addActionListener(new DeselectListener());
        deselectButton.setEnabled(false);

        freeForm = new JTextField(10);
        freeForm.addActionListener(addListener);
        freeForm.getDocument().addDocumentListener(addListener);

        topPane = new JPanel();
        topPane.setLayout(new BoxLayout(topPane, BoxLayout.LINE_AXIS)); // utilize BoxLayout
        topPane.add(title);
        topPane.add(freeForm);
        topPane.add(firstPlace);
        topPane.add(addButton);

        endPane = new JPanel();
        endPane.setLayout(new BoxLayout(endPane, BoxLayout.LINE_AXIS)); // utilize BoxLayout
        endPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        endPane.add(deselectButton);
        endPane.add(Box.createHorizontalGlue()); // pushes buttons to each side
        endPane.add(removeButton);

        centerPane = new JPanel();
        centerPane.setLayout(new BoxLayout(centerPane, BoxLayout.Y_AXIS)); // utilize BoxLayout
        centerPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 0, 5));
        centerPane.add(topPane);
        centerPane.add(listScrollPane);

        add(title, BorderLayout.PAGE_START);
        add(centerPane, BorderLayout.CENTER);
        add(endPane, BorderLayout.PAGE_END);
    }

    class AddListener implements ActionListener, DocumentListener {
        private boolean isEnabled = false;
        private JButton button;

        public AddListener(JButton button) {
            this.button = button;
        }

        public void actionPerformed(ActionEvent e) {
            String value = freeForm.getText();

            if (value.isBlank() || alreadyInList(value)) { // validation alert
                Toolkit.getDefaultToolkit().beep(); // sound alert
                if (value.isBlank()) {
                    JOptionPane.showMessageDialog(null, "Please enter a valid entry.");
                } else {
                    JOptionPane.showMessageDialog(null, "Value already exist. Please enter something different.");
                }
                freeForm.requestFocusInWindow(); // refocus on freeForm text input
                freeForm.selectAll(); // select all text for easy overwriting
                return;
            }

            System.out.println("Original list: " + listModel); // print out the contents of the original list

            Integer index = list.getSelectedIndex(); // get selected index
            if (index == -1 || firstPlace.isSelected()) { // no selection OR firstPlace is checked
                index = 0;
            } else {
                index++; // add after the selected item
            }

            if (index > 0 || firstPlace.isSelected()) {
                listModel.insertElementAt(freeForm.getText(), index); // insert element in specific index
                list.setSelectedIndex(index); // auto select newly added element
            } else {
                listModel.addElement(freeForm.getText()); // insert element at the bottom
            }
            freeForm.requestFocusInWindow(); // reset the input field
            freeForm.setText("");
            list.ensureIndexIsVisible(index);

            System.out.println("Updated list: " + listModel); // print out the updated contents of the list
        }

        protected boolean alreadyInList(String value) { // validate if value already exist
            return listModel.contains(value);
        }

        public void insertUpdate(DocumentEvent e) { // required by DocumentListener
            enableButton();
        }

        public void removeUpdate(DocumentEvent e) { // required by DocumentListener
            handleEmptyTextField(e);
        }

        public void changedUpdate(DocumentEvent e) { // required by DocumentListener
            if (!handleEmptyTextField(e)) {
                enableButton();
            }
        }

        private void enableButton() {
            if (!isEnabled) {
                button.setEnabled(true);
            }
        }

        private boolean handleEmptyTextField(DocumentEvent e) {
            if (e.getDocument().getLength() <= 0) {
                button.setEnabled(false);
                isEnabled = false;
                return true;
            }
            return false;
        }
    }

    class RemoveListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println("Original list: " + listModel); // print out the contents of the original list

            Integer index = list.getSelectedIndex(); // get selected index
            listModel.remove(index); // remove selected index

            Integer size = listModel.getSize();

            if (size == 0) {
                removeButton.setEnabled(false); // list size and disable button if empty
            } else {
                if (index == listModel.getSize()) {
                    index--; // last position element removal
                }
                list.setSelectedIndex(index);
                list.ensureIndexIsVisible(index);
            }

            System.out.println("Updated list: " + listModel); // print out the updated contents of the list
        }
    }

    class DeselectListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            list.clearSelection(); // clears selection
        }
    }

    public void valueChanged(ListSelectionEvent e) { // added as part of the requirement for ListSelectionListener
        if (e.getValueIsAdjusting() == false) {
            if (list.getSelectedIndex() == -1) {
                removeButton.setEnabled(false); // disable button if there's no selection
                deselectButton.setEnabled(false);
            } else {
                removeButton.setEnabled(true); // Selection, enable the fire button.
                deselectButton.setEnabled(true);
            }
        }
    }

    private static void SortedListProgramFrame() { // frame ui setup
        JFrame frame = new JFrame("Sorted List Program");
        JComponent newContentPane = new SortedListProgram();
        newContentPane.setOpaque(true); // content panes must be opaque

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(300, 200, 300, 300); // window position & size
        frame.setResizable(false);
        frame.setContentPane(newContentPane);
        frame.setVisible(true); // set to show JFrame window
    }

    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                SortedListProgramFrame();
            }
        });
    }
}
