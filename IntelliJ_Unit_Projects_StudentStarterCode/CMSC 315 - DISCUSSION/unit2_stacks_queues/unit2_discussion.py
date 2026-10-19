"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        # Create an empty list to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # Add the new item to the end (top) of the stack.
        # LIFO means the last item added will be removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # Check whether the stack is empty before removing an item.
        if not self.items:
            raise IndexError("Cannot pop from an empty stack.")

        # LIFO: Remove and return the most recently added item.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Check whether the stack is empty.
        if not self.items:
            raise IndexError("Cannot peek at an empty stack.")

        # Return the top item without removing it.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        # Return True if the stack contains no items.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # Create an empty deque to store queue items.
        # A deque allows efficient adding and removing from both ends.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # Add new tickets to the back of the queue.
        # FIFO ensures older tickets are processed before newer tickets.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Check if the queue is empty before removing an item.
        if not self.items:
            raise IndexError("Cannot dequeue from an empty queue.")

        # FIFO: Remove and return the oldest item from the front.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Check whether the queue is empty.
        if not self.items:
            raise IndexError("Cannot view the front of an empty queue.")

        # Return the oldest item without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        # Check whether the queue contains zero items.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO: TECHNICIAN ACTION HISTORY ===")

    # Create a stack for recording technician actions.
    action_stack = Stack()

    # Add four actions to demonstrate LIFO behavior.
    action_stack.push("Opened support ticket")
    action_stack.push("Assigned technician")
    action_stack.push("Updated ticket status")
    action_stack.push("Closed support ticket")

    print("Four technician actions were recorded.")
    print("Action history:", action_stack.items)

    # View the newest action without removing it.
    print("\nMost recent action:", action_stack.peek())

    # Undo actions in reverse order.
    print("\nUndoing actions in LIFO order:")

    while not action_stack.is_empty():
        print("Undo:", action_stack.pop())

    print("\nStack empty:", action_stack.is_empty())

    # Test popping from an empty stack.
    print("\nTesting pop() on an empty stack:")

    try:
        action_stack.pop()
    except IndexError as error:
        print("Handled empty stack:", error)

    # Test peeking at an empty stack.
    print("\nTesting peek() on an empty stack:")

    try:
        action_stack.peek()
    except IndexError as error:
        print("Handled empty stack:", error)

    # Test a stack containing only one item.
    print("\nTesting a single-item stack:")

    single_stack = Stack()
    single_stack.push("Restarted router")

    print("Added:", single_stack.peek())
    print("Removed:", single_stack.pop())
    print("Stack empty after removal:", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: SUPPORT TICKET PROCESSING ===")

    # Create a queue for incoming support tickets.
    ticket_queue = Queue()

    # Add four tickets in the order they were received.
    ticket_queue.enqueue("Ticket-001: Network outage")
    ticket_queue.enqueue("Ticket-002: Printer problem")
    ticket_queue.enqueue("Ticket-003: Password reset")
    ticket_queue.enqueue("Ticket-004: Server maintenance")

    print("Four support tickets were received.")
    print("Current ticket queue:", list(ticket_queue.items))

    # View the oldest ticket without removing it.
    print("\nNext ticket to process:", ticket_queue.front())

    # Demonstrate First In, First Out behavior.
    print("\nProcessing tickets in FIFO order:")

    while not ticket_queue.is_empty():
        print("Processing:", ticket_queue.dequeue())

    print("\nQueue empty:", ticket_queue.is_empty())

    # Test removing an item from an empty queue.
    print("\nTesting dequeue() on an empty queue:")

    try:
        ticket_queue.dequeue()
    except IndexError as error:
        print("Handled empty queue:", error)

    # Test viewing the front of an empty queue.
    print("\nTesting front() on an empty queue:")

    try:
        ticket_queue.front()
    except IndexError as error:
        print("Handled empty queue:", error)

    # Test a queue containing only one item.
    print("\nTesting a single-item queue:")

    single_queue = Queue()
    single_queue.enqueue("Ticket-005: Router restart")

    print("Added:", single_queue.front())
    print("Processed:", single_queue.dequeue())
    print("Queue empty after removal:", single_queue.is_empty())


if __name__ == "__main__":
    main()
