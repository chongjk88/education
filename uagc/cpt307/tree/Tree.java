/*
* Copyright (C) 2007-2014 by Brett Alistair Kromkamp <brett@perfectlearn.com>.
*/
package tree;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

public class Tree {
    private final static int ROOT = 0;
    private HashMap<String, Node> nodes;
    private TraversalStrategy traversalStrategy;

    // Constructors
    public Tree() {
        this(TraversalStrategy.DEPTH_FIRST);
    }

    public Tree(TraversalStrategy traversalStrategy) {
        this.nodes = new HashMap<String, Node>();
        this.traversalStrategy = traversalStrategy;
    }

    // Properties
    public HashMap<String, Node> getNodes() {
        return nodes;
    }

    public TraversalStrategy getTraversalStrategy() {
        return traversalStrategy;
    }

    public void setTraversalStrategy(TraversalStrategy traversalStrategy) {
        this.traversalStrategy = traversalStrategy;
    }

    // Public interface
    public Node addNode(String identifier) {
        return this.addNode(identifier, null);
    }

    public Node addNode(String identifier, String parent) {
        Node node = new Node(identifier);
        nodes.put(identifier, node);
        if (parent != null) {
            nodes.get(parent).addChild(identifier);
        }
        return node;
    }

    public void display(String identifier) {
        this.display(identifier, ROOT);
    }

    public void display(String identifier, int depth) {
        ArrayList<String> children = nodes.get(identifier).getChildren();
        if (depth == ROOT) {
            System.out.println(nodes.get(identifier).getIdentifier());
        } else {
            String tabs = String.format("%0" + depth + "d", 0).replace("0", " ");
            // 4 spaces
            System.out.println(tabs + nodes.get(identifier).getIdentifier());
        }
        depth++;
        for (String child : children) {
            // Recursive call
            this.display(child, depth);
        }
    }

    public Iterator<Node> iterator(String identifier) {
        return this.iterator(identifier, traversalStrategy);
    }

    public Iterator<Node> iterator(String identifier, TraversalStrategy traversalStrategy) {
        return traversalStrategy == TraversalStrategy.BREADTH_FIRST ? new BreadthFirstTreeIterator(nodes, identifier)
                : new DepthFirstTreeIterator(nodes, identifier);
    }
}