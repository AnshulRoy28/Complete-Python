#Decorators in Python. 
#A decorator in python is essentially a tool that allows us to add some extra 
#Features to a function without moddifying its code. Think of it like adding 
#Some extra attachments to it, The original base of the function remains unchanged

#Now how this works:- Functions in pythons behave as ''First class Citizens
# As in they can be passed over as a argument to anouther function, returned 
# or even assigned to a varaible. This means that we can treat them like any 
# Other Object in python making it extremely flexible. 

# Before we dive into this lets first look at some examples of the above operations

#Assigining functions to variables 
def plus_10(number):
    return number+10

add_10=plus_10
print(add_10(15))

#Unlike java or c++ we can directly define a function in anouther function
#This will be important later
def plus_one(number):
    def add_one(number):
        return number+1
    result=add_one(number)
    return result
print(plus_one(10))

#Functions can also return other functions as shown below 
def hello():
    def hello_world():
        return 'Hello World'
    return hello_world
hi=hello()
print(hi())

#In python if a function is nested it is still allowed to access the scope of the enclosing function.
# This is called Closure and is critical for decoratos to function appropriately 

#Here is an exmaple of a closure 

def outer(sample):
    # `inner` is a nested function that uses the variable `sample` from the enclosing `outer` function.
    def inner():
        print(f"Message from closure: {sample}")
    return inner  # `inner` is returned as a function object, capturing `sample` in its closure.

# When `outer` is called, it returns the `inner` function, with `sample` captured in its closure.
closure = outer("Hello, how do you do")

# At this point, `closure` holds the `inner` function, and it retains access to the `sample` variable
# even though the `outer` function has finished executing.

# Calling `closure()` invokes the `inner` function, which prints the captured value of `sample`.
print(closure())

#How is this useful for decorators:- To put it simply, when we create a decorator
#We also create a wrapper function, this wrapper function is a closure retaining access
#to the function being decorated and any additial state or arguments defined in the decorater 
#Function. 

# The simple_decorator function takes a function `func` as input
def simple_decorator(func):
    # The wrapper function is defined inside the decorator
    # It will add extra functionality around the original function `func`
    def wrapper():
        # This code runs before calling the original function
        print("Before func call")  
        
        # The original function `func` is called here
        # `func` will be the `greet` function in this case
        func()                   
        
        # This code runs after calling the original function
        print("After function call")
    
    # The wrapper function (which includes the new functionality) is returned
    return wrapper  

# The @simple_decorator is a decorator that wraps the greet function
# It is equivalent to: greet = simple_decorator(greet)
@simple_decorator
def greet():
    # This is the original function that will be decorated
    print("Hi, how do you do")

# When greet() is called, the `wrapper` function is executed instead of the original `greet` function
# This is because greet has been replaced by the `wrapper` function via the decorator
greet()


#With this basic Know How we can go ahead on creating our own Decorators in ernest 

def uppercase(function):
    def wrapper():
        func=function()
        uppercase=func.upper()
        return uppercase
    return wrapper

def say_hi():
    return 'Hello There'

decorate=uppercase(say_hi)
print(decorate())
