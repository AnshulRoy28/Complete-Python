# The Bat class represents a bat, inheriting basic attributes and behaviors such as flying ability
# and communication (via sound). This class demonstrates instance attributes, methods, and basic object behavior.

class Bat:
    # Class Attribute: 'species' defines the species for all instances of the Bat class.
    species = "Baty"

    # The __init__ method initializes a new Bat object, with an optional parameter 'can_fly'
    # to determine if the bat can fly (defaults to True).
    def __init__(self, can_fly=True):
        self.fly = can_fly  # The 'fly' attribute stores whether the bat can fly or not.

    # Instance Method: 'say' takes a message and overrides it
    # It returns a predefined message instead of using the input message.
    def say(self, msg):
        msg = "... ... ..."
        return msg
      
    def sonar(self):
        """Method that simulates a bat's echolocation sound."""
        return "***__***"

# Main execution block, runs only when this file is executed directly (not imported as a module).
if __name__ == "__main__":
    # Creating an instance of the Bat class
    b = Bat()

    # Calling the 'say' method on the Bat instance and printing the returned message.
    print(b.say("Hi"))  # This will print the bat's default message "... ... ..."

    # Accessing and printing the 'fly' attribute to see if the bat can fly.
    print(b.fly)  # This will print True (default value for 'can_fly')
