# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.



## My Unit 2 Implementation

### Design Approach

For this assignment, I created a technical support desk
simulation to demonstrate how stacks and queues work in
Python.

I used a Python list to implement the Stack class and
collections.deque to implement the Queue class.

### Stack Implementation

I implemented five methods for the Stack class:

- __init__() initialized an empty stack.
- push() added an item to the top of the stack.
- pop() removed the most recently added item.
- peek() returned the top item without removing it.
- is_empty() checked whether the stack contained any items.

I demonstrated Last In, First Out (LIFO) behavior by
recording four technician actions and undoing them in
reverse order.

### Queue Implementation

I implemented five methods for the Queue class:

- __init__() initialized an empty queue.
- enqueue() added a new item to the back of the queue.
- dequeue() removed the oldest item from the front.
- front() returned the oldest item without removing it.
- is_empty() checked whether the queue contained any items.

I demonstrated First In, First Out (FIFO) behavior by
processing four technical support tickets in the same
order they were received.

### Edge Case Testing

I tested the following situations:

- Removing an item from an empty stack.
- Viewing the top of an empty stack.
- Removing an item from an empty queue.
- Viewing the front of an empty queue.
- Removing the only item from a stack.
- Removing the only item from a queue.

I used IndexError exceptions to handle invalid removal
and viewing operations. The demonstration caught these
exceptions and displayed explanatory messages.

All demonstrated operations produced the expected output.

### Time and Space Complexity

Both implementations used O(n) memory as the number of
stored items increased.

The stack used amortized O(1) push operations and O(1)
pop and peek operations.

The queue used O(1) enqueue, dequeue, and front operations
with collections.deque.

### Program Execution

I ran the completed Python program using:

    python3 -B unit2_discussion.py

The program demonstrated both data structures, their
processing order, and the required edge cases.
