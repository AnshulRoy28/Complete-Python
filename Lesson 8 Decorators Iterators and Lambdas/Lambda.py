# What is a Lambda Function?
# - A lambda function is a small, anonymous function in Python.
# - It is defined using the keyword `lambda`.
# - Syntax:
#     lambda arguments: expression
#   The function can have any number of arguments but only a single expression, which is evaluated and returned.

# Key Features of Lambda Functions:
# 1. Anonymous: Lambda functions don’t have a name (unless assigned to a variable).
# 2. Single Expression: They are limited to a single line or expression.
# 3. Inline Use: Typically used for short, simple functions that are temporary.

# Syntax Breakdown:
# lambda x, y: x + y
# - `lambda`: Indicates the start of a lambda function.
# - `x, y`: Arguments passed to the function.
# - `x + y`: The expression to be evaluated and returned.

# Examples:

# 1. Basic Example:
add = lambda x, y: x + y  # Define a lambda function to add two numbers
print(add(5, 10))  # Output: 15

# 2. Using with Built-in Functions:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))  # Square each number using map and lambda
print(squared)  # Output: [1, 4, 9, 16, 25]

# 3. Filtering with `filter`:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filter even numbers using lambda
print(even_numbers)  # Output: [2, 4, 6]

# 4. Sorting with `sorted`:
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))  # Sort words by their length using lambda
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']

# 5. Lambda Function with Multiple Arguments:
multiply = lambda x, y, z: x * y * z  # Define a lambda function to multiply three numbers
print(multiply(2, 3, 4))  # Output: 24

# 6. Lambda Function with Default Arguments:
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"  # Default greeting is "Hello"
print(greet("John"))  # Output: Hello, John!
print(greet("Alice", "Good Morning"))  # Output: Good Morning, Alice!

# 7. Nested Lambda Functions:
power = lambda x: (lambda y: y ** x)  # A function that returns another lambda to compute power
square = power(2)  # Create a function to square a number
cube = power(3)  # Create a function to cube a number
print(square(4))  # Output: 16
print(cube(2))  # Output: 8

# 8. Using `reduce` with Lambda (from functools module):
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)  # Calculate the product of all numbers in the list
print(product)  # Output: 120

# 9. Lambda with Conditional Expressions:
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"  # Check if a number is even or odd
print(check_even(10))  # Output: Even
print(check_even(7))   # Output: Odd

# 10. Using Lambda with List Comprehension:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [lambda x: x ** 2 for x in numbers]  # List of lambda functions for squaring each number
print([func(x) for func, x in zip(squared_numbers, numbers)])  # Output: [1, 4, 9, 16, 25]


# Use Cases:
# 1. Temporary Use: Avoid defining a named function when it’s only used once.
# 2. Functional Programming: Useful with `map()`, `filter()`, and `reduce()` for concise operations.
# 3. Custom Sorting: Define dynamic sorting rules using the `key` parameter.

# Lambda Functions vs. `def` Functions

# - Syntax:  
#   Lambda functions are concise and written in a single line, while `def` functions are more detailed and span multiple lines.
# - Function Name:  
#   Lambda functions are anonymous, meaning they don’t have a name unless explicitly assigned to a variable. In contrast, functions created with `def` always have a defined name.
# - Scope:  
#   A lambda function is usually limited to the local scope in which it is defined, while functions created using `def` can be global or local, depending on where they are declared.
# - Complexity:  
#   Lambda functions are limited to simple, single expressions. On the other hand, `def` functions allow for more complex logic, spanning multiple lines of code.

# Limitations:
# 1. Single Expression: Cannot contain statements or multiple expressions.
# 2. Readability: Overuse can make code harder to read.
# 3. Debugging: Anonymous nature makes debugging more difficult.

# Best Practices:
# 1. Use lambda functions for simple, one-off tasks.
# 2. Avoid using lambda for complex logic.
# 3. Prefer named functions (`def`) for reusable or longer code.
