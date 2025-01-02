# 1. Primitive Data Types and Operators in Python

# Integer Arithmetic Operations
print(3)               # Basic integer number
print(1 + 1)           # Addition
print(8 - 1)           # Subtraction
print(10 * 2)          # Multiplication
print(35 / 5)          # Division

# Floor division (rounds towards negative infinity)
print(5 // 3)          # Integer division result: 1
print(-5 // 3)         # Integer division result: -2
print(5.0 // 3.0)      # Float division result: 1.0
print(-5.0 // 3.0)     # Float division result: -2.0

# Division returns a float even if both numbers are integers
print(10.0 / 3)        # Division result: 3.3333333333333335

# Modulo operation returns the remainder of division
print(7 % 3)           # Modulo result: 1
print(-7 % 3)          # Modulo result: 2

# Exponentiation
print(2**3)            # 2 raised to the power of 3: 8

# Parentheses to enforce precedence
print(1 + 3 * 2)       # Without parentheses: 7
print((1 + 3) * 2)     # With parentheses: 8

# Boolean values
print(True)            # True value
print(False)           # False value

# Boolean operations
print(not True)        # Not operator: False
print(not False)       # Not operator: True
print(True and False)  # AND operator: False
print(False or True)   # OR operator: True

# Boolean as integer values
print(True + True)     # 2 (True is 1, so 1 + 1 = 2)
print(True * 8)        # 8 (True is 1, so 1 * 8 = 8)
print(False - 5)       # -5 (False is 0, so 0 - 5 = -5)

# Comparison operations
print(0 == False)      # Equality check: True
print(2 > True)        # Comparison: True
print(2 == True)       # Equality check: False
print(-5 != False)     # Inequality check: True

# Boolean conversion of various data types
print(bool(0))         # False
print(bool(""))        # False
print(bool([]))        # False
print(bool({}))        # False
print(bool(4))         # True
print(bool(-6))        # True

# Using logical operators with integer values
print(bool(0))         # False
print(bool(2))         # True
print(0 and 2)         # 0
print(bool(-5))        # True
print(-5 or 0)         # -5

# Equality operator
print(1 == 1)          # True
print(2 == 1)          # False

# Inequality operator
print(1 != 1)          # False
print(2 != 1)          # True

# More comparison operations
print(1 < 10)          # True
print(1 > 10)          # False
print(2 <= 2)          # True
print(2 >= 2)          # True

# Using a range check
print(1 < 2 and 2 < 3)  # True
print(2 < 3 and 3 < 2)  # False
print(1 < 2 < 3)         # True
print(2 < 3 < 2)         # False

# Identity checks (is vs ==)
a = [1, 2, 3, 4]
b = a
print(b is a)          # True
print(b == a)          # True

b = [1, 2, 3, 4]
print(b is a)          # False
print(b == a)          # True

# String operations
print("Hello " + "world!")  # String concatenation
print("Hello " "world!")     # Concatenation without '+' using double quotes

# Accessing characters in a string
print("Hello world!"[0])   # First character: H

# Length of a string
print(len("This is a string"))  # 16

# Formatted strings (f-strings)
name = "Reiko"
print(f"She said her name is {name}.")  # "She said her name is Reiko"
print(f"{name} is {len(name)} characters long.")  # "Reiko is 5 characters long."

# None object
print(None)          # None

# Equality check with None (using 'is')
print("etc" is None)  # False
print(None is None)   # True