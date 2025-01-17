# Recursion in Python

# Recursion is when a function calls itself to solve smaller versions of the same problem. 
# This is useful for problems that can be broken down into smaller, similar subproblems. 
# Recursion can simplify the code for complex tasks, but it also requires careful attention to avoid infinite loops.

### Key Concepts:

# 1. Base Case:  
#    The base case is the condition that stops the recursion. Without it, the recursion would continue indefinitely, 
#    leading to a stack overflow.

# 2. Recursive Case:  
#    The recursive case is the part of the function where it calls itself with modified arguments to solve a smaller problem.

# 3. Recursive Function:  
#    A function that calls itself in its own definition.

# 4. Stack:  
#    Each recursive call adds a new layer to the function call stack. When the base case is reached, 
#    the stack starts unwinding, and the function returns the result.

### How Recursion Works:

# 1. The function breaks down the problem into smaller sub-problems.
# 2. The function calls itself to solve each sub-problem.
# 3. The recursion ends when the base case is met, and the result is returned.

### Example 1: Factorial Calculation

# Factorial of a number n is the product of all positive integers from 1 to n.

# n! = n × (n-1) × (n-2) × ... × 1

#### Factorial Function (Recursive):

def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n with the result of factorial(n-1)
    else:
        result = n * factorial(n - 1)
        # Debugging: print current function call
        print(f"factorial({n}) = {n} * factorial({n - 1}) = {result}")
        return result

# Example Execution:

# The following call will trace the recursive calls
print(factorial(5))  # Output: 120

# Output for tracing:
# factorial(5) = 5 * factorial(4) = 120
# factorial(4) = 4 * factorial(3) = 24
# factorial(3) = 3 * factorial(2) = 6
# factorial(2) = 2 * factorial(1) = 2
# factorial(1) = 1


### Example 2: Fibonacci Sequence

# The Fibonacci sequence is a series where each number is the sum of the two preceding ones. 
# The sequence starts with 0 and 1.

# F(n) = F(n-1) + F(n-2)
# F(0) = 0, F(1) = 1

#### Fibonacci Function (Recursive):

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: sum of fibonacci(n-1) and fibonacci(n-2)
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        # Debugging: print current function call
        print(f"fibonacci({n}) = fibonacci({n - 1}) + fibonacci({n - 2}) = {result}")
        return result

#### Example Execution:

# The following call will trace the recursive calls
print(fibonacci(5))  # Output: 5

# Output for tracing:
# fibonacci(5) = fibonacci(4) + fibonacci(3) = 5
# fibonacci(4) = fibonacci(3) + fibonacci(2) = 3
# fibonacci(3) = fibonacci(2) + fibonacci(1) = 2
# fibonacci(2) = fibonacci(1) + fibonacci(0) = 1


### Advantages of Recursion:

# 1. **Simplifies Code:** Recursion can simplify complex problems by breaking them into smaller, more manageable sub-problems.
# 2. **Elegant Solutions:** Recursive solutions are elegant for problems like tree traversal, graph traversal, and divide-and-conquer algorithms.

### Disadvantages of Recursion:

# 1. **Memory Consumption:** Recursion uses the call stack, which can lead to a stack overflow if the recursion depth is too large.
# 2. **Efficiency:** Recursive solutions, especially for problems like Fibonacci, can be inefficient due to overlapping subproblems. Memoization can help in such cases.

### Tail Recursion:

# Tail recursion is a form of recursion where the recursive call is the last operation in the function. 
# This allows the compiler to optimize and reuse the stack frame, avoiding stack overflow.

#### Tail Recursion Example:

def factorial_tail(n, accumulator=1):
    # Base case: when n is 0 or 1, return the accumulated result
    if n == 0 or n == 1:
        return accumulator
    else:
        # Recursive case: pass the accumulated result forward
        return factorial_tail(n - 1, n * accumulator)

#### Example Execution:

print(factorial_tail(5))  # Output: 120


### When to Use Recursion:

# 1. Problems that can be naturally divided into smaller subproblems (e.g., factorial, Fibonacci).
# 2. Problems like tree or graph traversal, where recursion provides a simple solution.
# 3. Tasks that involve repeated calculations, such as searching or sorting algorithms.

### Summary:

# - **Recursion** is a powerful technique that simplifies problem-solving by breaking a problem into smaller sub-problems.
# - Every recursive function must have a **base case** to prevent infinite recursion.
# - Recursive functions are commonly used for tasks like factorial calculations, Fibonacci sequences, and tree traversals.
# - While powerful, recursion can be less efficient and consume more memory if not carefully implemented.
