"""
Python Testing Tutorial for Beginners
=====================================

Testing is a crucial part of writing reliable software. In Python, we have built-in tools that make testing easier and more efficient. 
This tutorial walks you through different testing techniques using `doctest`, `unittest`, and `pytest`. We'll also explore two fundamental 
software testing methodologies: Black-box and White-box testing.
"""

# ====================================
# 1. Doctest (Lightweight Testing)
# ====================================

# Define a function to add two numbers
def add(a, b):
    """
    Adds two numbers and returns the sum.
    """
    return a + b

# Define a function to subtract two numbers
def subtract(a, b):
    """
    Subtracts the second number from the first and returns the result.
    """
    return a - b

# Define a function to multiply two numbers
def multiply(a, b):
    """
    Multiplies two numbers and returns the product.
    """
    return a * b

# Define a function to divide two numbers
def divide(a, b):
    """
    Divides the first number by the second and returns the quotient.
    Raises a ValueError if attempting to divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")  # Prevents division by zero
    return a / b

# If this script is run directly, perform doctest-based testing
if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Runs doctests to validate function correctness

# ====================================
# 2. Unittest (Built-in Unit Testing)
# ====================================

import unittest  # Import Python's built-in unit testing framework

# Define a test case class that inherits from unittest.TestCase
class TestMathOperations(unittest.TestCase):

    # Test cases for the add() function
    def test_add(self):
        self.assertEqual(add(2, 3), 5)   # 2 + 3 should return 5
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 should return 0
        self.assertEqual(add(0, 0), 0)   # 0 + 0 should return 0

    # Test cases for the subtract() function
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)  # 5 - 3 should return 2
        self.assertEqual(subtract(10, 10), 0)  # 10 - 10 should return 0

    # Test cases for the multiply() function
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)  # 3 * 4 should return 12
        self.assertEqual(multiply(-2, 5), -10)  # -2 * 5 should return -10

    # Test cases for the divide() function
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)  # 10 / 2 should return 5.0
        self.assertEqual(divide(9, 3), 3.0)   # 9 / 3 should return 3.0
        with self.assertRaises(ValueError):   # Ensure ValueError is raised for divide by zero
            divide(10, 0)

# Run the unit tests when the script is executed
if __name__ == "__main__":
    unittest.main(exit=False)

# ====================================
# 3. Mocking (Using unittest.mock)
# ====================================
from unittest.mock import MagicMock  # Import MagicMock for dependency mocking

# Function that fetches user data from a database
def get_user_data(database, user_id):
    """Fetches user data from a database."""
    return database.fetch(user_id)  # Calls the database fetch method

# Function to test the get_user_data function using a mock object
def test_mocking():
    mock_db = MagicMock()  # Create a mock database object
    mock_db.fetch.return_value = {"id": 1, "name": "Alice"}  # Define mock return value
    assert get_user_data(mock_db, 1) == {"id": 1, "name": "Alice"}  # Validate behavior

test_mocking()  # Run the mock test

# ====================================
# 4. Testing Methodologies
# ====================================

# Black-box Testing (Input/Output Based)

# Function to check if a number is even
def is_even(n):
    return n % 2 == 0  # Returns True if even, False otherwise

# Test function for black-box testing
def test_black_box():
    assert is_even(2) is True  # 2 is even
    assert is_even(3) is False  # 3 is odd
    assert is_even(0) is True  # 0 is even

test_black_box()  # Run black-box test cases

# White-box Testing (Logic/Branch Coverage)

# Function to compute absolute value of a number
def absolute_value(n):
    if n < 0:
        return -n  # Convert negative number to positive
    return n  # Return positive numbers as-is

# Test function for white-box testing
def test_white_box():
    assert absolute_value(-5) == 5  # Absolute of -5 should be 5
    assert absolute_value(0) == 0  # Absolute of 0 should be 0
    assert absolute_value(10) == 10  # Absolute of 10 should be 10

test_white_box()  # Run white-box test cases

# Function to compute the factorial of a number
def factorial(n):
    """Computes the factorial of a number."""
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    return n * factorial(n - 1)  # Recursive case: n * (n-1)!

# Test function for factorial
def test_factorial():
    assert factorial(0) == 1  # 0! = 1
    assert factorial(1) == 1  # 1! = 1
    assert factorial(5) == 120  # 5! = 120

test_factorial()  # Run factorial test cases

# Function to compute the nth Fibonacci number
def fibonacci(n):
    """Computes the nth Fibonacci number."""
    if n == 0:
        return 0  # Base case: 0th Fibonacci number is 0
    elif n == 1:
        return 1  # Base case: 1st Fibonacci number is 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case: F(n) = F(n-1) + F(n-2)

# Test function for Fibonacci series
def test_fibonacci():
    assert fibonacci(0) == 0  # Fibonacci(0) = 0
    assert fibonacci(1) == 1  # Fibonacci(1) = 1
    assert fibonacci(5) == 5  # Fibonacci(5) = 5

test_fibonacci()  # Run Fibonacci test cases

# Final message to indicate all tests have passed
print("All tests executed successfully!")
