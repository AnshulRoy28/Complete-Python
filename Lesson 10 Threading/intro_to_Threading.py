# Threading in Python allows you to run multiple tasks concurrently, enabling better performance
# for I/O-bound operations. Using the threading module, you can create and manage lightweight 
# threads to improve responsiveness in applications like web scraping and network requests.

# In order to utilize threads in Python, we need to import the threading library

import threading 
import time 

# Function to print numbers from 1 to 5
def print_numbers():
    for i in range(1, 6):
        print(f"numbers:{i}")  # Print numbers
        time.sleep(1)  # Sleep for 1 second to simulate a time-consuming task
    
# Function to print letters A to E
def print_letters():
    for letter in 'ABCDE':
        print(f"letter:{letter}")  # Print letters
        time.sleep(1)  # Sleep for 1 second to simulate a time-consuming task

# Create threads to run the two functions
thread1 = threading.Thread(target=print_numbers)  # Thread to print numbers
thread2 = threading.Thread(target=print_letters)  # Thread to print letters

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete before proceeding
thread1.join()  # Wait for thread1 to finish
thread2.join()  # Wait for thread2 to finish

# Print a message indicating both threads have finished execution
print("Both threads finished")

# As we can see, both processes (printing numbers and letters) are running in parallel.

# Now we can pass arguments into these threads to customize their behavior.

import threading
import time 

# Function to greet a person by name
def greet(name):
    for _ in range(3):
        print(f"Hello, {name}!")  # Print greeting
        time.sleep(0.1)  # Sleep for 0.1 second to simulate a small delay

# Create threads with different names as arguments
thread1 = threading.Thread(target=greet, args=('Alice',))  # Thread for Alice
thread2 = threading.Thread(target=greet, args=('Bob',))  # Thread for Bob

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete before proceeding
thread1.join()  # Wait for thread1 to finish
thread2.join()  # Wait for thread2 to finish

# Print a message indicating both threads have finished execution
print("Both Threads Finished execution!")

# If we run this a few times, we would notice that the outputs 
# do not alternate. This is because threads in Python are independent 
# of each other. For instance, thread 1 could run several times before 
# thread 2 runs. This is because the scheduling of threads is done 
# by the operating system, and it may not alternate between each print statement.

# In order to make the threads alternate, one method is to use the threading.Condition function.

import threading
import time

# Lock object to ensure thread-safe operation
lock = threading.Lock()

# Condition object to control the execution order between threads
condition = threading.Condition()

# Function to alternate greetings between threads
def greet(name, other_name):
    global turn  # Use global turn to control the alternating between threads
    for _ in range(3):
        with condition:  # Acquire the condition lock to synchronize threads
            while turn != name:  # Wait until it's this thread's turn
                condition.wait()  # Wait for the other thread to notify
            print(f"Hello, {name}")  # Print greeting
            time.sleep(0.1)  # Sleep for 0.1 second to simulate delay
            turn = other_name  # Switch turn to the other thread
            condition.notify_all()  # Notify the other thread to run

# Main function to start the alternating greeting threads
def greet_alternating():
    global turn
    turn = "Alice"  # Set the initial turn to Alice

    # Create threads for Alice and Bob
    thread1 = threading.Thread(target=greet, args=("Alice", "Bob"))
    thread2 = threading.Thread(target=greet, args=("Bob", "Alice"))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()  # Wait for thread1 to finish
    thread2.join()  # Wait for thread2 to finish

    # Print a message indicating both threads have finished execution
    print("Both threads finished")  # Message when both threads finish

# Call the greet_alternating function to start the alternating greeting threads
greet_alternating()
