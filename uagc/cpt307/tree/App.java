/*
* Copyright (C) 2007-2014 by Brett Alistair Kromkamp <brett@perfectlearn.com>.
*/
package tree;

import java.util.Iterator;

public class App {
    public static void main(String[] args) {
        Tree tree = new Tree();
        /*
         * The second parameter for the addNode method is the identifier
         * for the node's parent. In the case of the root node, either
         * null is provided or no second parameter is provided.
         */

        // 2022-02-27 - chongjun.kim@student.uagc.edu
        // Generated a list of major car corporations that sell in the U.S. 
        // and the brands they currently offer here.
        tree.addNode("Car makes sold in the U.S.");

        tree.addNode("BMW Group", "Car makes sold in the U.S.");
        tree.addNode("BMW", "BMW Group");
        tree.addNode("Mini", "BMW Group");
        tree.addNode("Rolls-Royce", "BMW Group");

        tree.addNode("Daimler AG", "Car makes sold in the U.S.");
        tree.addNode("Mercedes-Benz", "Daimler AG");
        tree.addNode("Smart", "Daimler AG");

        tree.addNode("Ford Motor Co.", "Car makes sold in the U.S.");
        tree.addNode("Ford", "Ford Motor Co.");
        tree.addNode("Lincoln", "Ford Motor Co.");

        tree.addNode("General Motors", "Car makes sold in the U.S.");
        tree.addNode("Buick", "General Motors");
        tree.addNode("Cadillac", "General Motors");
        tree.addNode("Chevrolet", "General Motors");
        tree.addNode("GMC", "General Motors");

        tree.addNode("Honda Motor Co.", "Car makes sold in the U.S.");
        tree.addNode("Acura", "Honda Motor Co.");
        tree.addNode("Honda", "Honda Motor Co.");

        tree.addNode("Mazda Motor Corp.", "Car makes sold in the U.S.");
        tree.addNode("Mazda", "Mazda Motor Corp.");

        tree.addNode("Renault-Nissan-Mitsubishi Alliance", "Car makes sold in the U.S.");
        tree.addNode("Infiniti", "Renault-Nissan-Mitsubishi Alliance");
        tree.addNode("Mitsubishi", "Renault-Nissan-Mitsubishi Alliance");
        tree.addNode("Nissan", "Renault-Nissan-Mitsubishi Alliance");

        tree.addNode("Stellantis", "Car makes sold in the U.S.");
        tree.addNode("Alfa Romeo", "Stellantis");
        tree.addNode("Chrysler", "Stellantis");
        tree.addNode("Dodge", "Stellantis");
        tree.addNode("Fiat", "Stellantis");
        tree.addNode("Jeep", "Stellantis");
        tree.addNode("Maserati", "Stellantis");
        tree.addNode("Ram", "Stellantis");

        tree.addNode("Subaru Corp.", "Car makes sold in the U.S.");
        tree.addNode("Subaru", "Subaru Corp.");

        tree.addNode("Tata Motors", "Car makes sold in the U.S.");
        tree.addNode("Jaguar", "Tata Motors");
        tree.addNode("Land Rover", "Tata Motors");

        tree.addNode("Tesla, Inc.", "Car makes sold in the U.S.");
        tree.addNode("Tesla", "Tesla, Inc.");

        tree.addNode("Toyota Motor Corp.", "Car makes sold in the U.S.");
        tree.addNode("Lexus", "Toyota Motor Corp.");
        tree.addNode("Toyota", "Toyota Motor Corp.");

        tree.addNode("Volkswagen AG", "Car makes sold in the U.S.");
        tree.addNode("Audi", "Volkswagen AG");
        tree.addNode("Bentley", "Volkswagen AG");
        tree.addNode("Bugatti", "Volkswagen AG");
        tree.addNode("Lamborghini", "Volkswagen AG");
        tree.addNode("Porsche", "Volkswagen AG");
        tree.addNode("Volkswagen", "Volkswagen AG");

        tree.addNode("Zhejiang Geely Holding Group (ZGH)", "Car makes sold in the U.S.");
        tree.addNode("Lotus", "Zhejiang Geely Holding Group (ZGH)");
        tree.addNode("Polestar", "Zhejiang Geely Holding Group (ZGH)");
        tree.addNode("Volvo", "Zhejiang Geely Holding Group (ZGH)");

        tree.display("Car makes sold in the U.S.");

        Integer total = 0;
        System.out.println("\n***** DEPTH-FIRST ITERATION *****"); // 2022-02-27 - added backslash before 'n' for newline
        Iterator<Node> depthIterator = tree.iterator("Car makes sold in the U.S."); // Default traversal strategy is 'depth-first'
        while (depthIterator.hasNext()) {
            Node node = depthIterator.next();
            System.out.println(node.getIdentifier());
            total ++;
        }

        System.out.println("\n***** BREADTH-FIRST ITERATION *****"); // 2022-02-27 - added backslash before 'n' for newline
        Iterator<Node> breadthIterator = tree.iterator("Car makes sold in the U.S.", TraversalStrategy.BREADTH_FIRST);
        while (breadthIterator.hasNext()) {
            Node node = breadthIterator.next();
            System.out.println(node.getIdentifier());
        }

        System.out.println("\nTotal number of Nodes: " + total); // 2022-02-27 - added total number of nodes
    }
}