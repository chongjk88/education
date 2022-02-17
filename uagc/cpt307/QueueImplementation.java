
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

public class QueueImplementation
{
    public static void main(String[] args)
    {
        Queue<Integer> queue = new LinkedList<Integer>(); // create object of Queue
  
        queue.add(1); // Add numbers to end of Queue
        queue.add(12);
  
        System.out.println("Queue: " + queue); // print queue
        System.out.println("Queue's head: " + queue.poll()); // print head and deletes the head
        System.out.println("Queue's head: " + queue.poll()); // print head and deleted the head
        System.out.println("Queue: " + queue); // print queue
        System.out.println("Queue's head: " + queue.poll()); // print null as Queue is empty now
    }
}
