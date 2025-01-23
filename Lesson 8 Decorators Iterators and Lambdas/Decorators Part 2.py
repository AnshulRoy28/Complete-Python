# This decorator converts the output of a function to uppercase
def uppercase(function):
    def wrapper():
        func = function()  # Call the original function
        uppercase = func.upper()  # Convert the result to uppercase
        return uppercase  # Return the uppercase result
    return wrapper  # Return the wrapper function, effectively "decorating" the original function

# Function that returns a simple greeting string
def say_hi():
    return 'Hello There'

# Applying the 'uppercase' decorator manually to the say_hi function
decorate = uppercase(say_hi)
print(decorate())  # Call the decorated function and print the result

# Using Python's @ symbol to apply the 'uppercase' decorator directly
@uppercase
def say_hi():
    return 'Howdy Do'

print(say_hi())  # Call the decorated function and print the result

# Explanation on using multiple decorators on a function. 
# The decorators are applied in order (bottom-up).
# We also use 'functools.wraps' to preserve the original function's metadata like name, docstring, etc.

import functools

# This decorator splits the string returned by the decorated function into a list of words
def split_string(function):
    @functools.wraps(function)  # Preserve the metadata of the original function
    def wrapper():
        func = function()  # Call the decorated function
        splitted_string = func.split()  # Split the returned string into a list of words
        return splitted_string  # Return the list of words
    return wrapper  # Return the wrapped function

# Apply both the 'uppercase' and 'split_string' decorators. Order matters here!
@split_string
@uppercase
def say_hiiii():
    return 'Hiiiii how do you do'

print(say_hiiii())  # The result is split into words and printed as a list

# Explanation of why reversing the order of decorators would cause an error:
# If we apply 'uppercase' before 'split_string', the list returned by split_string won't have the 'upper' method.
try:
    @uppercase
    @split_string
    def say_hiiii():
        return "Hello how are you"
    print(say_hiiii())  # This will raise an error as lists don't have 'upper' method
except AttributeError:
    print("As you can see an error was thrown due to an issue with the attributes")

# A decorator that accepts arguments. We pass the arguments to the wrapper function 
# and then to the decorated function when it is called.

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f"The arguments I accepted are {arg1}, {arg2}")
        function(arg1, arg2)  # Call the original function with the passed arguments
    return wrapper_accepting_arguments  # Return the wrapper function

# Using the 'decorator_with_arguments' decorator on the 'cities' function
@decorator_with_arguments
def cities(city_one, city_two):
    print(f"I love {city_one} and {city_two}")  # Print the cities passed as arguments

cities('Tokyo', 'India')  # Pass two city names as arguments to the decorated function

# Note: The number of arguments in the decorator's wrapper function must match those of the decorated function.

# General-purpose decorator: Can be used on any function by accepting any number of arguments using *args and **kwargs.

def general_purpose_decorator(function_to_decorate):
    def general_purpose_wrapper(*args, **kwargs):  # Accept any number of positional and keyword arguments
        print('Positional arguments are', args)  # Print the positional arguments
        print('Keyword arguments are', kwargs)  # Print the keyword arguments
        return function_to_decorate(*args, **kwargs)  # Call the decorated function with the passed arguments
    return general_purpose_wrapper  # Return the wrapper function

# Applying the general-purpose decorator to a function with no arguments
@general_purpose_decorator
def function_with_no_args():
    print("No arguments passed here")

function_with_no_args()  # Call the function without passing any arguments

# Applying the general-purpose decorator to a function with positional arguments
@general_purpose_decorator
def function_with_args(one, two, three):
    print(one, two, three)

function_with_args(1, 2, 3)  # Pass positional arguments

# Using the general-purpose decorator with keyword arguments (no need to define parameters explicitly)
@general_purpose_decorator
def function_with_keyword_args(*args, **kwargs):
    print(f"This has keyword args: {kwargs}")  # Print the keyword arguments

function_with_keyword_args(fname="Anshul", lname="Roy")  # Pass keyword arguments

# Using the general-purpose decorator with both positional and keyword arguments combined
@general_purpose_decorator
def function_with_both_position_and_keyword_args(*args, **kwargs):
    print(f"Positional arguments: {args}")  # Print positional arguments
    print(f"Keyword arguments: {kwargs}")  # Print keyword arguments

function_with_both_position_and_keyword_args(1, 2, 3, 4, name="Anshul Roy", age="19")  # Pass both positional and keyword arguments
