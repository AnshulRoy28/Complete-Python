# Queue Implementation in Python

# What is a Queue?
# ----------------
# A queue is a linear data structure that follows the First In, First Out (FIFO) principle.
# Think of it like a line of people waiting for a service: the first person in line is the first to be served.

# Implementation of a Queue Using Python List
class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue

    # Enqueue operation: Add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)  # Use the append method to add an item to the queue

    # Dequeue operation: Remove the front element from the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")  # If queue is empty, raise an error
        return self.queue.pop(0)  # Remove the first element using pop(0)

    # Peek operation: View the front element without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")  # If queue is empty, raise an error
        return self.queue[0]  # Return the first element

    # isEmpty operation: Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0  # Return True if the queue has no elements

    # Size operation: Return the total number of elements in the queue
    def size(self):
        return len(self.queue)  # Return the length of the queue

# Demonstration of Queue Functionality
# Create a sample queue
my_queue = Queue()

# Enqueue elements into the queue
print("Enqueueing elements into the queue:")
for elem in [10, 20, 30, 40, 50]:
    my_queue.enqueue(elem)
    print(f"Enqueued: {elem}")

print("\nCurrent Queue Size:", my_queue.size())  # Check the size of the queue
print("Front element:", my_queue.peek())  # Peek to see the front element

# Dequeue elements from the queue
print("\nDequeuing elements from the queue:")
while not my_queue.is_empty():
    print(f"Dequeued: {my_queue.dequeue()}")  # Dequeue elements one by one

print("\nIs the queue empty?", my_queue.is_empty())  # Check if the queue is empty
