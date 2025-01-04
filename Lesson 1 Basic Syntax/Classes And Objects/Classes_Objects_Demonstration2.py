# This file demonstrates multiple inheritance, where the 'Batman' class inherits from both 
# the 'Superhero' class and the 'Bat' class, combining their attributes and methods.

# Importing the 'Superhero' class from the 'DemonstrationClass2' module 
# and the 'Bat' class from the 'DemonstrationClass3' module.
from DemonstrationClass2 import Superhero
from DemonstrationClass3 import Bat

# The Batman class inherits from both Superhero and Bat.
# This demonstrates the concept of multiple inheritance in Python.
class Batman(Superhero, Bat):
    # The __init__ method initializes the Batman object, calling the __init__ methods of both parent classes.
    def __init__(self, *args, **kwargs):
        # Initializing the Superhero class with specific attributes for Batman.
        Superhero.__init__(self, "anonymous", movie=True, superpowers=['Wealthy'], *args, **kwargs)
        # Initializing the Bat class with specific attributes for Batman.
        Bat.__init__(self, *args, can_fly=False, **kwargs)

        # Customizing the name for the Batman object.
        self.name = "John Doe"

    # Overriding the 'sing' method from the Superhero class to make it specific to Batman.
    def sing(self):
        """Method that returns Batman's theme song."""
        return "Dun dun dun Batman!"

# Main execution block, runs only when this file is executed directly (not imported as a module).
if __name__ == '__main__':
    # Creating an instance of the Batman class
    sup = Batman()

    # Printing the Method Resolution Order (MRO) to show the inheritance hierarchy
    print(Batman.__mro__)

    # Accessing the species of the Batman object, which is inherited from Superhero.
    print(sup.get_species())  # Should print "SuperHuman"

    # Calling the overridden 'sing' method for Batman.
    print(sup.sing())  # Should print "Dun dun dun Batman!"

    # Calling the 'say' method from the Superhero class.
    sup.say("I Agree")  # Should print "I Agree" (overridden in Superhero)

    # Calling the 'sonar' method from the Bat class to simulate echolocation.
    print(sup.sonar())  # Should print "***__***"

    # Setting and printing the 'age' attribute inherited from the Human class.
    sup.age = 100  # Setting the age to 100
    print(sup.age)  # Should print 100

    # Printing the 'fly' attribute, which is set to False in the Bat class.
    print("Can I Fly: " + str(sup.fly))  # Should print "Can I Fly: False"
