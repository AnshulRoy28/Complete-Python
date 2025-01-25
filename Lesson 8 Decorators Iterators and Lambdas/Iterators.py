#Iterators in python can be defined as objects that allow us to traverse through a collection
#of items one element at a time without having to use indexing. 

#In Python, iterator objects must have two components: __iter__() and __next__().

#Lists and tuples in Python already have these components built into their definition.
#Hence, we can create an iterator directly from these objects.

my_list = [4, 7, 0]  # Example list

#Creating an iterator object from the list
sample_iterator = iter(my_list) 
print(sample_iterator)  # This will print a reference to the iterator object.

#Using the next() function to access elements in the iterator
try:
    print(next(sample_iterator))  # Prints the first element of the list
    print(next(sample_iterator))  # Prints the second element of the list
    print(next(sample_iterator))  # Prints the third element of the list
    print(next(sample_iterator))  # This will raise a StopIteration error
except StopIteration:
    print("End of the Iterable has been reached")

print()
#When we exceed the number of elements in the iterator, a StopIteration error is raised.

#The more elegant way to iterate over elements is by using a for loop. 
#For example:

my_list = [1, 7, 9]  # Example list

#The for loop automatically handles iteration and StopIteration errors internally.
for i in my_list:
    print(i)  # Prints each element in the list

print()
#We can also directly pass an iterator object into a for loop, achieving the same result.

my_list = [4, 0, 7, 0]  # Another example list
iterator = iter(my_list)  # Creating an iterator from the list

for i in iterator:
    print(i)  # Prints each element until the iterator is exhausted

#The for loop assigns the value of the next element to the loop variable ("i" in this case)
#and executes the indented code block. This process continues until the iterator is exhausted,
#at which point the loop terminates.

#Let us now look at how we can create our own custom iterators in Python.
#Custom iterators require two primary components: the __iter__() method and the __next__() method.

class PowThree:
    #A sample Python class to implement an iterator for powers of three

    def __init__(self, max=0):
        self.max = max  # The maximum power of 3 to compute

    def __iter__(self):
        self.n = 0  # Initialize the current power to 0
        return self  # Return the iterator object itself

    def __next__(self):
        if self.n <= self.max:  # Check if the current power is within the limit
            result = 3 ** self.n  # Compute 3 raised to the power of "n"
            self.n += 1  # Increment the power
            return result  # Return the computed result
        else:
            raise StopIteration  # Raise StopIteration when the limit is reached

#Creating an instance of the PowThree iterator with a maximum power of 3
numbers = PowThree(3)

i = iter(numbers)  # Creating an iterator object from the PowThree instance
print(next(i))  # Prints 3^0 = 1
print(next(i))  # Prints 3^1 = 3
print(next(i))  # Prints 3^2 = 9
print(next(i))  # Prints 3^3 = 27

print()
#Using a for loop to iterate over the custom iterator
for i in PowThree(5):
    print(i)  # Prints powers of 3 from 3^0 to 3^5

print()
#Infinite iterators are iterators that never stop producing elements.
#We can create an infinite iterator using the "count" function from the itertools library.

from itertools import count

#Creating an infinite iterator starting from 1
infinite_iterator = count(1)

#Using a for loop to extract 500 elements from the infinite iterator
for i in range(500):
    print(next(infinite_iterator))  # Prints numbers starting from 1 incrementing by 1

#Now let us attempt to create our own infinite iterator that mimics the behavior of the above.

class InfiniteCounter:
    #A custom infinite iterator class

    def __init__(self, start=0, step=1):
        self.current = start  # Initialize the starting value
        self.step = step  # Initialize the step size

    def __iter__(self):
        return self  # Return the iterator object itself

    def __next__(self):
        value = self.current  # Store the current value
        self.current += self.step  # Increment the current value by the step size
        return value  # Return the current value

#Creating an instance of the InfiniteCounter iterator
counter = InfiniteCounter()

#Using a for loop to extract elements from the infinite iterator
for num in counter:
    print(num)  # Prints numbers starting from 0 incrementing by 1
    if num > 500:  # Break the loop after printing 500 elements
        break

#Now let us compare the performance of the two infinite iterators

import time

#Timing the built-in "count" function
start_iterator_time = time.time()  # Record the start time
for i in range(50000):
    pass  # Iterates 50000 times without doing anything
end_iterator_time = time.time()  # Record the end time

#Timing the custom InfiniteCounter class
counter = InfiniteCounter()  # Create a new instance of the InfiniteCounter class
start_counter_time = time.time()  # Record the start time
for num in counter:
    if num > 50000:  # Break the loop after iterating 50000 times
        break
end_counter_time = time.time()  # Record the end time

#Print the time taken by each iterator
print(end_iterator_time - start_iterator_time)  # Time taken by the built-in "count"
print(end_counter_time - start_counter_time)  # Time taken by the custom InfiniteCounter

#The custom iterator takes longer to execute compared to the built-in "count" function.
#This is because the built-in "count" is implemented in C, making it more efficient.
#In contrast, the custom iterator is written in Python, introducing overhead due to its interpreted nature.

#We will explore deeper performance comparisons and optimization techniques at a later time.
