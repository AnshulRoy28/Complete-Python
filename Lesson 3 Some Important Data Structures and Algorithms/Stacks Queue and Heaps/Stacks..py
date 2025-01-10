# Stack Implementation in Python

# What is a Stack?
# ----------------
# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
# Think of it like a stack of plates: the last plate added is the first one removed.

# Key Operations of a Stack:
# 1. Push: Add an element to the top of the stack.
# 2. Pop: Remove and return the top element of the stack.
# 3. Peek/Top: Return the top element without removing it.
# 4. isEmpty: Check if the stack is empty.
# 5. Size: Return the number of elements in the stack.

# In python we can easily implement a stack using a list
class Stack:
    def __init__(self):
        self.stack = []  #Creating a list to store the elements

    # Push operation:- Adding an element to the end of the stack
    def push(self, item):
        self.stack.append(item)#We can simply use the in built append function in python to achive this

    # Pop operation:- Remove the last element of the stack 
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack") #If stack is empty raise an error 
        return self.stack.pop() #utillise the in built python function for pop 

    # Peek operation:- #Reading the last element of the stack 
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack") #IF stack is empty raise an error stating that the stack is empty 
        return self.stack[-1] #Show the last element of the stack 

    # isEmpty operation:- Checking if the stack is empty 
    def is_empty(self):
        return len(self.stack) == 0 #If length of the stack is zero then it is empty else it is not 

    # Size operation:- The total number of elements in the stack 
    def size(self): 
        return len(self.stack) #Return the length of the stack

# Demonstration of Stack functionality
my_stack = Stack() #Creating a sample stack object 

# Push elements onto the stack
print("Pushing elements onto the stack:") 
for elem in [1, 2, 3, 4, 5]: 
    my_stack.push(elem) #Calling the push function from our class to add elements to the stack
    print(f"Pushed: {elem}")

print("\nCurrent Stack Size:", my_stack.size()) #Check the size of the stack after pushing 
print("Top element:", my_stack.peek()) #Peek to see the last element of the stack

# Pop elements from the stack
print("\nPopping elements from the stack:")
while not my_stack.is_empty():#As we want to empty the stack we continue till the stack is empty
    print(f"Popped: {my_stack.pop()}") #Pop out the elements of the stack starting from the last element 

print("\nIs the stack empty?", my_stack.is_empty()) #Check if the stack is empty 
