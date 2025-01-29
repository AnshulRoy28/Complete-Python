# Example 1: __new__ and __init__
# The __new__ method is called when a new instance of the class is created.
# It creates and returns a new instance of the class.
# The __init__ method initializes the instance's attributes after it's created.
class Employee:
    def __new__(cls):
        print("__new__ method is called")
        instance = super().__new__(cls)  # Creates a new instance using super() method
        return instance  # Returns the instance
    
    def __init__(self):
        print("__init__ method is being called")  # Called to initialize the instance
        self.name = 'Satya'  # Assigning default value to the name attribute
        self.salary = 12000  # Assigning default value to the salary attribute

    def __str__(self):
        # Returns a string representation of the Employee instance for printing
        return f'Employee: name={self.name}, Salary=${self.salary}'

e = Employee()  # Creating an Employee instance
print(e)  # Prints the Employee instance using __str__ method
print()  # Blank line for better readability

# Example 2: __add__ and __str__
# The __add__ method is used to define the behavior of the addition operator (+)
# Here, it adds two Distance objects (in feet and inches).
class Distance:
    def __init__(self, feet=0, inches=0):
        self.feet = feet  # Initialize feet attribute
        self.inches = inches  # Initialize inches attribute

    def __add__(self, other):
        # Adds two Distance objects by converting everything to inches first
        total_inches = self.feet * 12 + self.inches + other.feet * 12 + other.inches
        new_feet = total_inches // 12  # Converts total inches back to feet
        new_inches = total_inches % 12  # Remainder is the remaining inches
        return Distance(new_feet, new_inches)  # Returns a new Distance object

    def __str__(self):
        # Provides a human-readable string representation of the Distance object
        return f'{self.feet} feet {self.inches} inches'

d1 = Distance(3, 10)  # Creating a Distance object (3 feet 10 inches)
d2 = Distance(4, 4)  # Creating another Distance object (4 feet 4 inches)
print(f"d1 = {d1}, d2 = {d2}")  # Prints the two Distance objects
d3 = d1 + d2  # Adds the two Distance objects using __add__ method
print(f"d1 + d2 = {d3}")  # Prints the result of the addition
print()  # Blank line for readability

# Example 3: __ge__ (greater than or equal to)
# The __ge__ method allows us to use the 'greater than or equal to' operator (>=) on Distance objects.
class Distance:
    def __init__(self, feet=0, inches=0):
        self.feet = feet  # Initialize feet
        self.inches = inches  # Initialize inches

    def __ge__(self, other):
        # Compares two Distance objects by converting everything to inches
        val1 = self.feet * 12 + self.inches
        val2 = other.feet * 12 + other.inches
        return val1 >= val2  # Returns True if this distance is greater than or equal to the other

d1 = Distance(2, 1)  # Creating a Distance object (2 feet 1 inch)
d2 = Distance(4, 10)  # Creating another Distance object (4 feet 10 inches)
print(f"Is d1 >= d2? {d1 >= d2}")  # Checks if d1 is greater than or equal to d2
print()  # Blank line for readability

# Example 4: __eq__ (equality) and __len__
# The __eq__ method is used to compare two objects for equality.
# The __len__ method returns the length of the object (in this case, the number of pages in a book).
class Book:
    def __init__(self, title, pages):
        self.title = title  # Initialize the title attribute
        self.pages = pages  # Initialize the pages attribute

    def __eq__(self, other):
        # Compares two Book objects based on their title and pages
        return self.title == other.title and self.pages == other.pages

    def __len__(self):
        # Returns the number of pages in the book
        return self.pages

    def __str__(self):
        # Provides a string representation of the Book object
        return f'Book: {self.title}, Pages: {self.pages}'

book1 = Book("Python Programming", 300)  # Creating a Book object
book2 = Book("Python Programming", 300)  # Another Book object with the same title and pages
book3 = Book("Advanced Python", 400)  # A different Book object
print(f"book1 == book2: {book1 == book2}")  # Compares book1 and book2 for equality
print(f"book1 == book3: {book1 == book3}")  # Compares book1 and book3 for equality
print(f"Length of book1: {len(book1)} pages")  # Prints the length (number of pages) of book1
print()  # Blank line for readability

# Example 5: __call__ (making an instance callable)
# The __call__ method allows us to make an instance of the class callable like a function.
# In this example, each call increments a counter.
class Counter:
    def __init__(self):
        self.count = 0  # Initialize the count attribute

    def __call__(self):
        self.count += 1  # Increments the count each time the instance is called
        return self.count  # Returns the updated count

counter = Counter()  # Creating an instance of Counter
print(f"Counter: {counter()}")  # Calls the instance (increments and returns count)
print(f"Counter: {counter()}")  # Calls the instance again
print(f"Counter: {counter()}")  # Calls the instance once more
print()  # Blank line for readability

# Example 6: __getitem__ and __setitem__ (indexing and assignment)
# The __getitem__ and __setitem__ methods allow us to use indexing (e.g., inventory[key]) on custom objects.
class Inventory:
    def __init__(self):
        self.items = {}  # Initialize an empty dictionary to store items

    def __getitem__(self, key):
        # Returns the value (quantity) of an item in the inventory, defaulting to 0 if not found
        return self.items.get(key, 0)

    def __setitem__(self, key, value):
        # Sets the quantity of an item in the inventory
        self.items[key] = value

    def __str__(self):
        # Returns the inventory as a string representation (dictionary of items)
        return str(self.items)

inventory = Inventory()  # Creating an Inventory object
inventory['apple'] = 10  # Adding 10 apples to the inventory
inventory['banana'] = 5  # Adding 5 bananas to the inventory
print(f"Inventory: {inventory}")  # Prints the entire inventory
print(f"Apples in inventory: {inventory['apple']}")  # Accessing the quantity of apples
print(f"Oranges in inventory: {inventory['orange']}")  # Accessing the quantity of oranges (not in inventory)
print()  # Blank line for readability

# Example 7: __enter__ and __exit__ (context management)
# The __enter__ and __exit__ methods are used to manage resources in a context manager (e.g., files).
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename  # Store the filename
        self.mode = mode  # Store the mode (e.g., write 'w')

    def __enter__(self):
        # Opens the file when entering the context
        self.file = open(self.filename, self.mode)
        return self.file  # Returns the file object for use within the context

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Closes the file when exiting the context, even if an error occurred
        self.file.close()

with ManagedFile('example.txt', 'w') as f:
    # Writes to the file within the context manager block
    f.write('Hello, World!')

print("File 'example.txt' has been written.")  # Confirmation that the file was written
print()  # Blank line for readability

# Example 8: __iter__ and __next__ (iteration)
# The __iter__ and __next__ methods allow an object to be used in a for loop (iteration).
class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize the starting number for countdown

    def __iter__(self):
        # Returns itself as an iterator
        return self

    def __next__(self):
        # Decrements the start value each time next() is called, raises StopIteration when done
        if self.start <= 0:
            raise StopIteration  # Stops the iteration when the countdown reaches 0
        current = self.start
        self.start -= 1
        return current

countdown = Countdown(5)  # Creating a Countdown object starting at 5
print("Countdown:")
for number in countdown:  # Iterating through the countdown
    print(number)
print()  # Blank line for readability

# Example 9: __repr__ (official string representation)
# The __repr__ method provides an official string representation of an object.
class Point:
    def __init__(self, x, y):
        self.x = x  # Initialize x coordinate
        self.y = y  # Initialize y coordinate

    def __repr__(self):
        # Provides an official representation of the Point object for debugging
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)  # Creating a Point object at (3, 4)
print(f"Point: {p}")  # Prints the string representation of the Point object
print()  # Blank line for readability

# Example 10: __contains__ (membership test)
# The __contains__ method allows us to use the 'in' operator to test for membership in a custom object.
class Playlist:
    def __init__(self, songs):
        self.songs = songs  # Initialize the list of songs

    def __contains__(self, song):
        # Checks if a song is in the playlist
        return song in self.songs

playlist = Playlist(['Song1', 'Song2', 'Song3'])  # Creating a Playlist object
print(f"Is 'Song2' in the playlist? {'Song2' in playlist}")  # Checks if 'Song2' is in the playlist
print(f"Is 'Song4' in the playlist? {'Song4' in playlist}")  # Checks if 'Song4' is in the playlist
print()  # Blank line for readability
