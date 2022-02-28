/*
* Copyright (C) 2007-2014 by Brett Alistair Kromkamp <brett@perfectlearn.com>.
*/
package tree;

import java.util.ArrayList;

public class Node {
    private String identifier;
    private ArrayList<String> children;

    // Constructor
    public Node(String identifier) {
        this.identifier = identifier;
        children = new ArrayList<String>();
    }

    // Properties
    public String getIdentifier() {
        return identifier;
    }

    public ArrayList<String> getChildren() {
        return children;
    }

    // Public interface
    public void addChild(String identifier) {
        children.add(identifier);
    }
}
