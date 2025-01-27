# We have already had some rudimentary experience with the basics of Classes and Objects.
# In this segment, we shall explore these concepts in more detail.

# OOP or Object-Oriented Programming is essentially a way of structuring programs 
# by organizing data and actions into objects. These objects combine attributes (data) 
# and methods (functions) that work together, making the code easier to manage and reuse.

# OOP has 4 central 'Pillars': Encapsulation, Inheritance, Abstraction, and Polymorphism.
# Encapsulation: Bundles data and methods together in a single unit (object) while restricting direct access to the data to ensure security.
# Inheritance: Allows a class to inherit properties and behaviors from another class, promoting code reuse.
# Polymorphism: Enables using a single interface or method in different ways depending on the context.
# Abstraction: Hides complex implementation details and shows only the essential features of an object to the user.

# We will go over the meaning of each of these concepts as we delve deeper.

# Now, let us start from the basics with class creation.

# In Python, we can use the `class` keyword followed by a name and a colon. 
# Inside the class, we use the `__init__()` function to declare the attributes 
# (or variables) that each instance of the class will have.

class Employee:
    # The `__init__()` method is the constructor of the class.
    # It initializes (creates and assigns) instance variables for the object.
    def __init__(self, name, age):
        self.name = name  # Instance variable `name` is initialized.
        self.age = age    # Instance variable `age` is initialized.

# There are a few things happening here:
# - We are creating attributes `name` and `age` and assigning values to them.
# - These attributes are instance variables, which are unique to each object (instance) of the class.
# - Example: An employee's name and age will differ between objects.

# Additionally, we can also have **class attributes**.
# - Class attributes are shared among all instances of a class.
# - Example: The species of all employees.

# Class attributes are defined directly below the `class` keyword.
class Employee:
    species = 'Homo Sapiens'  # This is a class attribute.

    def __init__(self, name, age):
        # Instance variables specific to each object.
        self.name = name
        self.age = age

# Now, if we create multiple instances (objects) of the `Employee` class,
# we can see how instance and class attributes apply in real life.

Tommy = Employee('Tommy', 21)  # Create an object `Tommy` with name and age.
Fred = Employee('Fred', 25)    # Create another object `Fred`.

# Accessing instance variables:
print(Tommy.age)  # Output: 21
print(Tommy.name)  # Output: Tommy
# Accessing the class attribute:
print(Tommy.species)  # Output: Homo Sapiens

print()

print(Fred.age)  # Output: 25
print(Fred.name)  # Output: Fred
print(Fred.species)  # Output: Homo Sapiens

print()

# As we see above, the name and age of each employee are different (instance variables), 
# while the species is the same for all employees (class attribute).

# This is an advantage of the class-based approach: 
# Every instance will have attributes that you are aware of, making data organization easier.

# For example, take the following:
try:
    # This will throw an error because the `age` parameter is missing.
    Dave = Employee('Dave')
    print(Dave.age)
except TypeError:
    print("One or more Attributes Missing")

print()

# As seen above, we cannot create an instance without providing all required attributes 
# (name and age in this case). This ensures all instances of the class have consistent data.

# Instance variables can also be modified dynamically.
Fred.age = 990  # Changing Fred's age.
print(Fred.age)  # Output: 990

# Now, let's look at instance methods.
# Instance methods are functions defined inside a class and can only be called on an instance of the class.
# Like the `__init__` function, an instance method always takes `self` as its first parameter.

class Employee:
    species = "Homo Sapien"  # Class attribute shared by all instances.

    def __init__(self, name, age):
        self.age = age
        self.name = name

    # Instance method to describe the employee.
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Instance method to describe the employee's job.
    def job(self, title):
        return f"Hi, my name is {self.name}, and I work as a {title}"

# Creating instances of the Employee class:
Fred = Employee('Fred', 21)
Goerge = Employee('Goerge', 21)

# Accessing instance variables and methods:
print(Fred.name)  # Output: Fred
print(Fred.age)   # Output: 21
print(Fred.description())  # Output: Fred is 21 years old
print(Fred.job("Engineer"))  # Output: Hi, my name is Fred, and I work as an Engineer

print()

# There is still an issue with our class:
# When we try to print the object directly (e.g., `print(Fred)`), 
# it shows a cryptic message like `<__main__.Employee object at 0x...>`.

# To make objects more human-readable, we can define the `__str__()` method.

class Employee:
    species = "Homo Sapien"  # Class attribute.

    def __init__(self, name, age):
        self.age = age
        self.name = name

    # The `__str__` method returns a user-friendly string representation of the object.
    def __str__(self):
        return f"{self.name}, {self.age}"

    def description(self):
        return f"{self.name} is {self.age} years old"

    def job(self, title):
        return f"Hi, my name is {self.name}, and I work as a {title}"

# Creating instances of the Employee class:
Fred = Employee('Fred', 21)
Goerge = Employee('Goerge', 21)

# Now, printing the objects directly is more user-friendly:
print(Fred)  # Output: Fred, 21
print(Goerge)  # Output: Goerge, 21

# Methods like `__init__` and `__str__` are called **dunder methods** (short for "double underscore").
# Python provides a series of dunder methods that allow customization of how objects behave.
