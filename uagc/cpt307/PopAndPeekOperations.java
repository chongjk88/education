
/**
* Week 3 - Interactive Assignment 1
* 
* Title: Pop and Peek Operations
* Created by: Chongjun Kim
* School: The University of Arizona Global Campus
* Course: CPT307 - Data Structures & Algorithms (INE2206A)
* Professor: Michael Hayden
* Due Date: 02-17-2022
*/

import java.util.*;

public class PopAndPeekOperations
{
    public static void main(String[] args)
    {
        Stack<Integer> initialStack = new Stack<Integer>(); // Creating a new Stack
        Stack<Integer> sortedStack = new Stack<Integer>(); // Another new Stack for sorting

        initialStack.push(30); // adding elements to the new Stack
        initialStack.push(10);
        initialStack.push(40);
        initialStack.push(20);

        System.out.println("Unsorted list: " + initialStack); // print initial Stack prior to sorting

        while (!initialStack.isEmpty())
        {
            Integer temp = initialStack.pop(); // pop the top element into a variable

            while (!sortedStack.isEmpty() && // check if the sorted Stack is not empty
                    sortedStack.peek() > temp) // AND if the top element is greater
            {
                initialStack.push(sortedStack.pop()); // push the top element from sorted Stack to the initial Stack
            }
            sortedStack.push(temp); // push temp into sorted Stack
        }

        System.out.println("Sorted list: " + sortedStack); // print newly sorted Stack
    }
}
