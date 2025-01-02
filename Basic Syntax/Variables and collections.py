# Python has a print function
print("Python has a print function")
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you! \n

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!")  # => Hello, World! \n

# Simple way to get input data from console
input_string_var = input("Enter some data: ")  # Returns the data as a string
print(f"Input received: {input_string_var}\n")

# There are no declarations, only assignments.
# Convention in naming variables is snake_case style
some_var = 5
print(f"some_var = {some_var}\n")  # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.

# Uncommenting the line below will raise a NameError
# print(some_unknown_var)  # Raises a NameError

# if can be used as an expression
result = "yay!" if 0 > 1 else "nay!"
print(f"if-else expression result: {result}\n")  # => "nay!"

# Lists store sequences
li = []
print("Initial empty list:", li, '\n')
# You can start with a prefilled list
other_li = [4, 5, 6]
print("Prefilled list:", other_li, '\n')

# Add stuff to the end of a list with append
li.append(1)    # li is now [1]
print("List after append(1):", li, '\n')
li.append(2)    # li is now [1, 2]
print("List after append(2):", li, '\n')
li.append(4)    # li is now [1, 2, 4]
print("List after append(4):", li, '\n')
li.append(3)    # li is now [1, 2, 4, 3]
print("List after append(3):", li, '\n')

# Remove from the end with pop
popped_value = li.pop()  # => 3 and li is now [1, 2, 4]
print(f"Popped value: {popped_value}, List after pop:", li, '\n')

# Let's put it back
li.append(3)    # li is now [1, 2, 4, 3] again.
print("List after append(3) again:", li, '\n')

# Access a list like you would any array, here indexing starts with 0 and ends at length of list-1
print(f"First element (li[0]): {li[0]}")   # => 1
# Look at the last element
print(f"Last element (li[-1]): {li[-1]}\n")  # => 3

# Looking out of bounds is an IndexError
# Uncommenting the line below will raise an IndexError
# li[4]  # Raises an IndexError

# You can look at ranges with slice syntax.
print(f"Slice from index 1 to 3: {li[1:3]}")   # Return list from index 1 to 3 => [2, 4]
print(f"Slice from index 2 onwards: {li[2:]}")    # Return list starting from index 2 => [4, 3]
print(f"Slice from start to index 3: {li[:3]}")    # Return list from beginning until index 3  => [1, 2, 4]
print(f"Slice with step size 2: {li[::2]}")   # Return list selecting elements with a step size of 2 => [1, 4]
print(f"List in reverse order: {li[::-1]}\n")  # Return list in reverse order => [3, 4, 2, 1]

# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.
print("Deep copy of list (li2):", li2, '\n')

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]
print("List after del li[2]:", li, '\n')

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
print("List after remove(2):", li, '\n')
# Uncommenting the line below will raise a ValueError
# li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again
print("List after insert(2) at index 1:", li, '\n')

# Get the index of the first item found matching the argument
print(f"Index of first occurrence of 2: {li.index(2)}")  # => 1
# Uncommenting the line below will raise a ValueError
# li.index(4)  # Raises a ValueError as 4 is not in the list

# You can add lists
print(f"Concatenating li + other_li: {li + other_li}\n")  # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]
print("List after extend:", li, '\n')

# Check for existence in a list with "in"
print(f"Is 1 in li? {1 in li}")  # => True

# Examine the length with "len()"
print(f"Length of li: {len(li)}\n")  # => 6

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
print(f"Tuple tup: {tup}")
print(f"tup[0]: {tup[0]}")      # => 1

# Uncommenting the line below will raise a TypeError
# tup[0] = 3  # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
print(f"Type of (1): {type((1))}")   # => <class 'int'>
print(f"Type of (1,): {type((1,))}")  # => <class 'tuple'>
print(f"Type of (): {type(())}\n")    # => <class 'tuple'>

# You can do most of the list operations on tuples too
print(f"Length of tup: {len(tup)}")         # => 3
print(f"Concatenating tup + (4, 5, 6): {tup + (4, 5, 6)}")  # => (1, 2, 3, 4, 5, 6)
print(f"tup[:2]: {tup[:2]}")          # => (1, 2)
print(f"2 in tup: {2 in tup}")         # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
print(f"Unpacking (1, 2, 3) -> a: {a}, b: {b}, c: {c}")

# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
print(f"Extended unpacking (1, 2, 3, 4) -> a: {a}, b: {b}, c: {c}")

# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
print(f"Unpacking (4, 5, 6) -> d: {d}, e: {e}, f: {f}")

# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4
print(f"After swapping e and d -> e: {e}, d: {d}")

# Dictionaries store mappings from keys to values
empty_dict = {}
print("Empty dictionary:", empty_dict, '\n')

# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}
print("Prefilled dictionary:", filled_dict, '\n')

# Note keys for dictionaries have to be immutable types.
# Uncommenting the line below will raise a TypeError
# invalid_dict = {[1,2,3]: "123"}  # => Yield a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
print("Valid dictionary with tuple keys:", valid_dict, '\n')

# Look up values with []
print(f"filled_dict['one']: {filled_dict['one']}")  # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
print(f"Keys in filled_dict: {list(filled_dict.keys())}\n")

# Get all values as an iterable with "values()". Once again we need to wrap it
print(f"Values in filled_dict: {list(filled_dict.values())}\n")

# Check for existence of keys in a dictionary with "in"
print(f"Is 'one' in filled_dict? {'one' in filled_dict}")  # => True
print(f"Is 1 in filled_dict? {1 in filled_dict}")      # => False

# Looking up a non-existing key is a KeyError
# Uncommenting the line below will raise a KeyError
# print(filled_dict["four"])  # KeyError

# Use "get()" method to avoid the KeyError
print(f"filled_dict.get('one'): {filled_dict.get('one')}")      # => 1
print(f"filled_dict.get('four'): {filled_dict.get('four')}")     # => None
# The get method supports a default argument when the value is missing
print(f"filled_dict.get('one', 4): {filled_dict.get('one', 4)}")   # => 1
print(f"filled_dict.get('four', 4): {filled_dict.get('four', 4)}")  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is now 5
print(f"filled_dict after setdefault: {filled_dict}", '\n')

# To remove a key and return the value, use "pop()"
print(f"filled_dict.pop('five'): {filled_dict.pop('five')}")     # => 5 and filled_dict is now {'one': 1, 'two': 2, 'three': 3}
print(f"filled_dict after pop('five'): {filled_dict}", '\n')

# You can update a dictionary with another dictionary
filled_dict.update({"four": 4})    # Now filled_dict is {"one": 1, "two": 2, "three": 3, "four": 4}
print(f"filled_dict after update: {filled_dict}", '\n')

# Deleting a key will remove it from the dictionary
del filled_dict["four"]   # Now filled_dict is {"one": 1, "two": 2, "three": 3}
print(f"filled_dict after del 'four': {filled_dict}\n")

# Sets are like dictionaries but only contain keys (no values).
empty_set = set()
print("Empty set:", empty_set, '\n')

# Sets are useful for performing set operations like union, intersection, and difference
some_set = {1, 2, 3}
print("Prefilled set:", some_set, '\n')

# Add values to a set
some_set.add(4)  # some_set is now {1, 2, 3, 4}
print("Set after add(4):", some_set, '\n')

# Remove an arbitrary item from a set
removed_value = some_set.pop()  # removed_value is one of {1, 2, 3, 4} and some_set is now a smaller set
print(f"Removed value: {removed_value}, Set after pop:", some_set, '\n')

# Delete everything in a set with clear()
some_set.clear()   # some_set is now an empty set
print("Set after clear():", some_set, '\n')

# To remove a value from a set, use remove()
some_set.add(4)
some_set.add(5)
some_set.remove(4)  # some_set is now {5}
print("Set after remove(4):", some_set, '\n')

# You can check set membership using "in"
print(f"Is 5 in some_set? {5 in some_set}")   # => True
print(f"Is 4 in some_set? {4 in some_set}")   # => False
print(f"Is 6 not in some_set? {6 not in some_set}\n")  # => True

# Perform set operations
other_set = {4, 5, 6, 7}
print(f"Union of some_set and other_set: {some_set.union(other_set)}")  # => {5, 6, 7}
print(f"Intersection of some_set and other_set: {some_set.intersection(other_set)}")  # => {5}
print(f"Difference of other_set from some_set: {other_set.difference(some_set)}")  # => {6, 7}
