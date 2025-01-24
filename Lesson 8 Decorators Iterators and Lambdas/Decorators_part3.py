# Defining a decorator maker that accepts arguments
# The decorator maker itself takes three arguments: decorator_arg1, decorator_arg2, decorator_arg3.
# It then defines the decorator and a wrapper inside it.
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    # The decorator is defined here, which will wrap the original function.
    def decorator(func):
        # The wrapper function is defined inside the decorator.
        def wrapper(function_arg1, function_arg2, function_arg3):
            "This is the wrapper function"
            # The wrapper function can access arguments from both the decorator maker and the original function.
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2, decorator_arg3,
                          function_arg1, function_arg2, function_arg3))
            # Calls the original function with its arguments.
            return func(function_arg1, function_arg2, function_arg3)

        return wrapper

    return decorator

# Example of using the decorator maker:
pandas = "Pandas"

# The decorator maker is called with arguments, which returns a decorator.
@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    # This is the original function, which will be wrapped by the decorator.
    print("This is the decorated function and it only knows about its arguments: {0} {1} {2}"
          .format(function_arg1, function_arg2, function_arg3))

# Calling the decorated function with its arguments.
decorated_function_with_arguments(pandas, "Science", "Tools")

# The following illustrates an issue with decorators:
# After wrapping, the function name and docstring are replaced by those of the wrapper function.
print(decorated_function_with_arguments.__name__)  # Prints "wrapper"
print(decorated_function_with_arguments.__doc__)   # Prints "This is the wrapper function"

# To fix this, we use the `functools.wraps` function:
# It ensures the metadata of the original function is preserved in the decorated function.
import functools

def uppercase_decorator(func):
    @functools.wraps(func)  # Copies the name, docstring, and other metadata from `func` to the wrapper.
    def wrapper():
        # The wrapper modifies the original function's output to uppercase.
        return func().upper()
    return wrapper

# Example usage of the uppercase decorator:
@uppercase_decorator
def say_hi():
    "This will say hi"  # Original docstring.
    return 'hello there'

print(say_hi())  # Prints "HELLO THERE"
print(say_hi.__name__)  # Prints "say_hi" (metadata preserved)
print(say_hi.__doc__)   # Prints "This will say hi" (docstring preserved)

# Python also allows creating class-based decorators:
class UppercaseDecorator:
    def __init__(self, function):
        # Stores the original function.
        self.function = function

    def __call__(self, *args, **kwargs):
        # Calls the original function and modifies its result.
        result = self.function(*args, **kwargs)
        return result.upper()

# Example usage of the class-based decorator:
@UppercaseDecorator
def greet():
    return "Hello There"

print(greet())  # Prints "HELLO THERE"

# Another example of a class-based decorator:
class CallCounter:
    def __init__(self, function):
        # Stores the original function and initializes a counter.
        self.function = function
        self.count = 0

    def __call__(self, *args, **kwargs):
        # Increments the call count and logs it.
        self.count += 1
        print(f"Function {self.function.__name__} has been called {self.count} times.")
        # Calls the original function.
        return self.function(*args, **kwargs)

# Example usage of the CallCounter decorator:
@CallCounter
def say_hello():
    print("Hello!")

say_hello()  # Prints "Function say_hello has been called 1 times." and "Hello!"
say_hello()  # Prints "Function say_hello has been called 2 times." and "Hello!"

# One of the practical uses of decorators is caching, which stores the result of expensive function calls:
from functools import lru_cache

@lru_cache(maxsize=128)  # Caches the results of the function for up to 128 unique inputs.
def fibonacci(n):
    # Calculates the nth Fibonacci number recursively.
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Using the cached Fibonacci function:
print(fibonacci(999))  # The first call may take some time, but subsequent calls are faster.

# Decorators have many other uses:
# - Logging
# - Authentication
# - Execution timing
# - Retry mechanisms
# - Input validation
