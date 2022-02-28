/*
* Copyright (C) 2007-2014 by Brett Alistair Kromkamp <brett@perfectlearn.com>.
*/
package tree;

import java.util.*;

/*
* See URL: http://en.wikipedia.org/wiki/Breadth-first_search
*/
public class BreadthFirstTreeIterator implements Iterator<Node> {
    private static final int ROOT = 0;
    private LinkedList<Node> list;
    private HashMap<Integer, ArrayList<String>> levels;

    public BreadthFirstTreeIterator(HashMap<String, Node> tree, String identifier) {
        list = new LinkedList<Node>();
        levels = new HashMap<Integer, ArrayList<String>>();
        if (tree.containsKey(identifier)) {
            this.buildList(tree, identifier, ROOT);
            for (Map.Entry<Integer, ArrayList<String>> entry : levels.entrySet()) {
                for (String child : entry.getValue()) {
                    list.add(tree.get(child));
                }
            }
        }
    }

    private void buildList(HashMap<String, Node> tree, String identifier, int level) {
        if (level == ROOT) {
            list.add(tree.get(identifier));
        }
        ArrayList<String> children = tree.get(identifier).getChildren();
        if (!levels.containsKey(level)) {
            levels.put(level, new ArrayList<String>());
        }
        for (String child : children) {
            levels.get(level).add(child);
            // Recursive call
            this.buildList(tree, child, level + 1);
        }
    }

    @Override
    public boolean hasNext() {
        return !list.isEmpty();
    }

    @Override
    public Node next() {
        return list.poll();
    }

    @Override
    public void remove() {
        throw new UnsupportedOperationException();
    }
}
