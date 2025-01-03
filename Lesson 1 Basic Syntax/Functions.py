# Basic Add function
def add(x, y):
    """Basic function to add two numbers."""
    print(f"Sum of the two numbers is {x + y}")
    return x + y

print(add(3, 5))
print(add(y=12, x=21))  # Passing arguments in a different order
print()

# Creating a function that takes a variable number of args and prints them
def variable_arg_function(*args):
    """Function that accepts a variable number of arguments and returns them as a tuple."""
    return args

print(variable_arg_function(1, 2, 3),"\n")

# Summing up all variable arguments
def variable_arg_sum_function(*args):
    """Function that sums up all variable arguments."""
    sum = 0
    for i in args:
        sum += i
    return sum

print(variable_arg_sum_function(1, 2, 3, 4, 5),"\n")

# Creating a function that takes a variable number of keyword arguments
def keyword_args(**kwargs):
    """Function that collects keyword arguments and prints them."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return kwargs

print(keyword_args(x=11, y=12, z=31),"\n")

# Combining variable args and keyword args
def all_args(*args, **kwargs):
    """Function to demonstrate combining variable and keyword arguments."""
    print(args)
    print(kwargs)

args = (1, 2, 3, 4, 5)
kwargs = {'a': 12, "b": 21, "c": 31, "d": 13}

all_args(*args)          # Unpacking standard arguments
all_args(**kwargs)        # Passing keyword arguments
all_args(*args, **kwargs) # Passing both types of arguments
print()

# Function to swap two elements and return them
def swap(x, y):
    """Function to swap two elements."""
    return y, x

x, y = swap(1, 2)
print(x, y,"\n")

# Global and Local Scope
x = 5  # Global variable

def set_x(num):
    """Set a local variable x."""
    x = num
    print(x)

def set_global_x(num):
    """Set a global variable x using the global keyword."""
    global x
    print(x)
    x = num
    print(x)

set_x(43)
set_global_x(21)
print(x, "\n")

# First-Class Functions
def create_adder(x):
    """Create a closure that returns a function to add x to a given value."""
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
print(add_10(3))  # Here we are assigning a y
print()

# Creating a first-class function to compute the average of numbers
def create_avg():
    """Closure that maintains state to compute average of numbers."""
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count
    return avg

avg = create_avg()
print(avg(3))
print(avg(5))
print(avg(12))
print(avg(21))
print(avg(1))
print()

# Lambda Functions
print("Lambda functions: ")
print((lambda x: x > 2)(3))  # Lambda to check if x > 2
print((lambda x, y: x**2 + y**2)(2, 1))  # Lambda function for sum of squares
print()
# Using lambda with map
print("Lambda functions with Map: ")
print(list(map(add_10, [1, 2, 3, 4, 5])))  # Applying add_10 using map
print(list(map(max, [1, 2, 31], [4, 6, 1])))  # Pairwise max comparison
print()

# Using lambda with filter
print("lambda functions with Filter: ")
print(list(filter(lambda x: x > 5, [5, 4, 3, 2, 6, 7, 5, 6, 4, 8])))  # Filter numbers > 5
print()

# List comprehensions using lambda
print("List comprehension: ")
print([add_10(i) for i in [1, 2, 3, 4]])  # Using lambda functions in list comprehensions
print()

#Generator Objects
print("Generator objects")
print(x for x in [3, 4, 5, 6, 7] if x > 5)  # Generator object for numbers > 5
print(list(x for x in [1, 2, 3, 4, 5, 5, 6, 7] if x > 5))  # List comprehension with filter
print()

# Set Comprehension
print("Set Comprehension")
print({x for x in "abcddeef" if x not in "abc"})  # Set comprehension excluding 'abc'
print({x: x**2 for x in range(5)})  # Dictionary comprehension for squares
