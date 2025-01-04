# Importing the 'Human' class from another module to demonstrate inheritance.
# The 'Human' class is assumed to be from the file 'DemonstrationClass1.py'
from DemonstrationClass1 import Human

# The Superhero class inherits from the Human class, meaning it has all properties
# and behaviors of the Human class, and can add or modify its own.
class Superhero(Human):
    # Overriding the 'species' attribute from the Human class for Superhero.
    species = "SuperHuman"

    # The __init__ method initializes the object with additional attributes like 'movie' and 'superpowers'.
    # 'super().__init__(name)' calls the __init__ method of the parent (Human) class.
    def __init__(self, name, movie=False, superpowers=['MindControl', "Transformation"]):
        self.functional = True  # New attribute specific to Superhero
        self.movie = movie  # Boolean flag indicating if the superhero is part of a movie
        self.superpowers = superpowers  # List of powers the superhero has
        
        # Call the parent class (Human) initializer to initialize the 'name' and 'age' attributes
        super().__init__(name)

    # Overriding the 'sing' method from the Human class to customize behavior for Superhero
    def sing(self):
        """Method specific to Superhero: Returns a 'singing' string."""
        return "Dan, dum, DUN!"

    # New method specific to Superhero class, which boasts about its superpowers.
    def boast(self):
        """Method that prints out each of the superhero's powers."""
        for power in self.superpowers:
            print(f"I wield the power of {power}!")

# Main execution block to test the Superhero class.
if __name__ == "__main__":
    # Creating an instance of the Superhero class with the name 'Tick'.
    sup = Superhero(name="Tick")

    # Using 'isinstance' to check if 'sup' is an instance of the Human class or its subclass.
    if isinstance(sup, Human):
        print("I am human")

    # Using 'type' to check if 'sup' is an instance of the Superhero class.
    if type(sup) is Superhero:
        print("I am a superhero")

    # Printing the method resolution order (MRO) of the Superhero class.
    # MRO is the order in which classes are searched when calling a method or attribute.
    print(Superhero.__mro__)

    # Accessing the species of the Superhero, which is different from Human's species.
    print(sup.get_species())

    # Calling the overridden 'sing' method specific to Superhero.
    print(sup.sing())

    # Using the 'say' method from the Human class to print a message.
    sup.say("Spoon")

    # Calling the 'boast' method specific to Superhero to display powers.
    sup.boast()

    # Printing the age of the superhero. This is accessed via the property 'age' from the Human class.
    print(sup.age)

    # Printing whether the superhero is eligible for an Oscar, based on the 'movie' attribute.
    print("Am I Oscar Eligible? " + str(sup.movie))
