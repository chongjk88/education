
/**
* Week 3 - Interactive Assignment 2
* 
* Title: Queue Implementation
* Created by: Chongjun Kim
* School: The University of Arizona Global Campus
* Course: CPT307 - Data Structures & Algorithms (INE2206A)
* Professor: Michael Hayden
* Due Date: 02-17-2022
*/

import java.util.*;
import java.util.concurrent.*;

public class QueueImplementation {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedBlockingQueue<Integer>(5); // create integer queue with a limit of 5 elements

        // utilize peek() and element() to test exception
        try {
            System.out.println("Peek: " + queue.peek()); // try peek() on empty queue
        } catch (Exception e) {
            System.out.println("Exception: " + e); // does not reach exception and displays null instead
        }
        try {
            System.out.println("Element: " + queue.element()); // try element() on empty queue
        } catch (Exception e) {
            System.out.println("Exception: " + e); // throw exception due to empty queue
        }

        // add numbers using while loop
        Integer num = 0;
        while (queue.size() < 5) {
            queue.add(num);
            num++;
        }
        System.out.println("Updated queue: " + queue); // display updated queue

        // utilize poll()
        queue.poll(); // remove first element
        System.out.println("Removed first element: " + queue); // print queue

        // utilize peek() and element() on a non-empty queue
        if (queue.size() > 0) { // make sure there is at least one element
            System.out.println("Peek: " + queue.peek()); // print first element using peek()
            System.out.println("Element: " + queue.element()); // print first element using element()
        }

        // utilize offer() to test queue limit
        if (queue.offer(10)) {
            System.out.println("10 is added"); // adds a number using offer()
        } else {
            System.out.println("Unable to add more. Queue is full");
        }
        if (queue.offer(20)) {
            System.out.println("20 is added");
        } else {
            System.out.println("Unable to add more. Queue is full"); // test queue limit via offer()
        }

        // remove all numbers using while loop
        while (queue.size() > 0) {
            queue.remove(); // removes all elements
        }
        System.out.println("Emptied queue: " + queue); // display empty queue

        // utilize poll() and remove() to test exception
        try {
            System.out.println("Poll: " + queue.poll()); // try poll() on empty queue
        } catch (Exception e) {
            System.out.println("Exception: " + e); // does not reach exception and displays null instead
        }
        try {
            System.out.println("Remove: " + queue.remove()); // try remove() on empty queue
        } catch (Exception e) {
            System.out.println("Exception: " + e); // throw exception due to empty queue
        }
    }
}
