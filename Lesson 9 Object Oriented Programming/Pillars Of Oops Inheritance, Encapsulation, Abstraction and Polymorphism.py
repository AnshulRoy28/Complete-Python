# Python code demonstrating the four pillars of OOP:
# Encapsulation, Inheritance, Abstraction, and Polymorphism.

# =============================================
# 1. Encapsulation
# =============================================
# Encapsulation bundles data (attributes) and methods (functions) into a single unit (class).
# It also restricts direct access to data by making attributes private or protected.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute (encapsulated)

    # Public method to access private attribute
    def get_balance(self):
        return self.__balance

    # Public method to modify private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Insufficient funds or invalid amount."

# Example usage of Encapsulation
account = BankAccount("Alice", 1000)
print(account.account_holder)  # Output: Alice
print(account.get_balance())   # Output: 1000
print(account.deposit(500))    # Output: Deposited $500. New balance: $1500
print(account.withdraw(200))   # Output: Withdrew $200. New balance: $1300

# Attempting to access private attribute directly will raise an error
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# =============================================
# 2. Inheritance
# =============================================
# Inheritance allows a class to inherit attributes and methods from another class.
# This promotes code reuse and hierarchical organization.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Cat class inherits from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Example usage of Inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.

# =============================================
# 3. Abstraction
# =============================================
# Abstraction hides complex implementation details and exposes only essential features.
# In Python, abstraction is achieved using abstract base classes (ABC).

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method (no implementation)

    @abstractmethod
    def perimeter(self):
        pass  # Abstract method (no implementation)

# Concrete class implementing Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class implementing Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage of Abstraction
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")  # Output: Circle Area: 78.5, Perimeter: 31.4
print(f"Rectangle Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")  # Output: Rectangle Area: 24, Perimeter: 20

# =============================================
# 4. Polymorphism
# =============================================
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# It enables using a single interface for different data types.

# Function demonstrating Polymorphism
def animal_sound(animal):
    print(animal.speak())

# Example usage of Polymorphism
animals = [Dog("Rex"), Cat("Mittens")]
for animal in animals:
    animal_sound(animal)
# Output:
# Rex barks.
# Mittens meows.

# Polymorphism with abstract classes
shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
# Output:
# Area: 28.26, Perimeter: 18.84
# Area: 20, Perimeter: 18

# =============================================
# Summary
# =============================================
# - Encapsulation: Bundling data and methods, restricting direct access.
# - Inheritance: Reusing code by inheriting from a parent class.
# - Abstraction: Hiding complex details and exposing only essential features.
# - Polymorphism: Using a single interface for different data types.
