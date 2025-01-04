# A class is essentially a blueprint that defines the properties (attributes) and behaviors (methods) 
# of an object. It is a way to represent real-world entities and actions in code.

# To create a class, we use the 'class' statement.

class Human:
    # Class Attribute: 'species' is a property that is shared by all instances of the class
    species = "Homo.Sapiens"

    # The __init__ method is called when a new object (instance) of the class is created.
    # It initializes the object's attributes. 'self' refers to the current instance.
    def __init__(self, name):
        self.name = name  # Assigns a unique name to the object
        self._age = 0  # Initializes 'age' privately. The leading underscore indicates it's meant for internal use.

    # Instance Method: A method that is called on an instance of the class.
    # It requires 'self' as the first argument to refer to the current instance.
    def say(self, msg):
        """Method that allows the human object to say a message."""
        print(f"{self.name}: {msg}")

    # Another instance method
    def sing(self):
        """Method that returns a string when the human sings."""
        return "Hi hi, How are you liking Python so far?"

    # Class Method: A method that is bound to the class, not the instance.
    # It is used to operate on class-level attributes or perform class-related actions.
    # The first argument is 'cls', referring to the class itself.
    @classmethod
    def get_species(cls):
        """Class method that returns the species of the class."""
        return cls.species

    # Static Method: A method that doesn't require a reference to the instance or class.
    # It's a function that belongs to the class but doesn't interact with class or instance attributes.
    @staticmethod
    def grunt():
        """Static method that returns a grunt sound."""
        return "*grunt*"

    # Property Decorator: This allows the 'age' method to behave like an attribute.
    # The method is accessed as a property, but it is a method in the class.
    @property
    def age(self):
        """Getter method for 'age'. It returns the private '_age' attribute."""
        return self._age

    # Setter method for the 'age' property. This allows us to set 'age' directly.
    @age.setter
    def age(self, age):
        """Setter method for 'age' to set a value."""
        self._age = age

    # Deleter method for the 'age' property. This allows us to delete 'age'.
    @age.deleter
    def age(self):
        """Deleter method for 'age' to delete the '_age' attribute."""
        del self._age


# Main execution block, runs only when this file is executed directly (not imported as a module).
if __name__ == "__main__":
    # Creating two instances of the Human class
    i = Human(name="Ian")
    i.say("hi")  # Ian says hi

    j = Human("Joel")
    j.say("hello")  # Joel says hello

    # Showing how to access the class attribute 'species' using an instance or class itself
    i.say(i.get_species())  # Ian says the species
    Human.species = "H.neandrathal"  # Changing the species at the class level
    i.say(i.get_species())  # Ian says the new species
    j.say(j.get_species())  # Joel says the new species

    # Calling the static method 'grunt' using both class and instance
    print(Human.grunt())  # Prints *grunt*
    print(i.grunt())  # Prints *grunt*

    # Setting and getting the 'age' property for both instances
    i.age = 42  # Setting age for Ian
    i.say(i.age)  # Ian says his age
    j.say(j.age)  # Joel says his age (0, as age is not set yet)

    # Deleting the 'age' attribute from Ian
    del i.age  # Deletes the 'age' property from Ian
