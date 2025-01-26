# Regular Expressions in Python are patterns used to match, search, and manipulate strings
# Based on specific character combinations

# Essentially, they allow us to match text patterns within strings

# First, let's import the re library to utilize Python's regular expression functionality
import re

# Sample string to search within
sample_string = 'An example word:Beluga Whale'

# This regular expression looks for the first occurrence of 'word:' followed by exactly 3 word characters (letters, digits, or underscores)
# \w matches a word character, and \w\w\w means exactly three word characters after 'word:'
sample_match = re.search(r'word:\w\w\w', sample_string)

# If a match is found, it will print the matched string; otherwise, it prints "Not found"
if sample_match:
    print('found', sample_match.group())
else:
    print("Not found")


# Now let's explore more examples of regular expressions

# Searching for 'iii' in the string 'piiig', this will match the first occurrence of 'iii'
match = re.search(r'iii', 'piiig')
print(match.group())  # Output: iii
print()

# Searching for 'igs' in 'piiiigs', this will match the first occurrence of 'igs'
match = re.search(r'igs', 'piiiigs')
print(match.group())  # Output: igs
print()

# Searching for '....g' in 'piiig', this matches any four characters followed by 'g'
match = re.search(r'....g', 'piiig')
print(match.group())  # Output: piiig
print()

# Searching for exactly three digits '\d\d\d' in the string 'p123g'
match = re.search(r'\d\d\d', 'p123g')
print(match.group())  # Output: 123
print()

# Searching for exactly three word characters '\w\w\w' in '@@abcd!!'
match = re.search(r'\w\w\w', '@@abcd!!')
print(match.group())  # Output: abc
print()

# Searching for 'pi+' where 'i+' means one or more 'i's in the string 'piiiiiiiiig'
match = re.search(r'pi+', 'piiiiiiiiig')
print(match.group())  # Output: piiiiiiii
print()

# Searching for one or more 'i's in 'piigiiii'
match = re.search(r'i+', 'piigiiii')
print(match.group())  # Output: iii
print()

# Searching for the pattern of 3 digits with optional spaces in between: '\d\s*\d\s*\d' in 'xx1 2   3xx'
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print(match.group())  # Output: 1 2 3
print()
# Searching for the same pattern in 'xx12  3xx'
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
print(match.group())  # Output: 12 3
print()

# Searching for the same pattern in 'xx123xx'
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print(match.group())  # Output: 123
print()

# Searching for a word that starts with 'b' and contains word characters, using '^b\w+' (starts with 'b')
try:
    match = re.search(r'^b\w+', 'foobar')  # The string does not start with 'b', so no match
    print(match.group())
except AttributeError:
    print("None Type Detected")  # Expected because no match is found

# Searching for a word that starts with 'b' and contains word characters (doesn't require it to be at the start)
match = re.search(r'b\w+', 'foobar')
print(match.group())  # Output: bob (the first match starting with 'b')
print()


# One of the powerful use cases of regular expressions is extracting email addresses from a string

# Sample string containing an email address
sample_string = 'xyz alicia-blanche@google.com midnight monkey matchmaker'

# Regular expression to find the first occurrence of an email-like pattern (e.g., username@domain)
# The pattern matches one or more word characters followed by '@' and then one or more word characters
match = re.search(r'\w+@\w+', sample_string)
if match:
    print(match.group())  # Output: alicia-blanche@google
print()


# The above search does not get the full email address, including domain extensions like '.com'
# To capture the full email, including characters like '.', we modify the regex to:
# '[\w.-]+@[\w.-]+' will match any word characters, dots, or hyphens in both the username and domain
match = re.search(r'[\w.-]+@[\w.-]+', sample_string)
print(match.group())  # Output: alicia-blanche@google.com
print()


# Let's look at the group feature, which allows us to extract specific parts of the matched text
str = 'purple alice-b@google.com monkey dishwasher'

# The regex pattern '([\w.-]+)@([\w.-]+)' uses parentheses to capture parts of the match into groups
# Group 1 captures the username (before '@') and Group 2 captures the domain (after '@')
match = re.search(r'([\w.-]+)@([\w.-]+)', str)

if match:
    print(match.group())   # Output: 'alice-b@google.com' (the whole match)
    print(match.group(1))  # Output: 'alice-b' (the username, group 1)
    print(match.group(2))  # Output: 'google.com' (the domain, group 2)
print()


# The findall function is a very powerful function in the re module; it returns all valid matches as a list of strings

# Sample string with multiple email addresses
sample_str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

# Using findall to find all email addresses in the string
emails = re.findall(r'[\w\.-]+@[\w\.-]+', sample_str)
print(emails)  # Output: ['alice@google.com', 'bob@abc.com']
print()

# Looping through the list of found email addresses and printing each one
for i in emails:
    print(i)


# We can also use findall with files
# Open a file called 'test.txt' (make sure the file exists and contains some text to search for)
f = open('test.txt', encoding='utf-8')

# Feed the file text into findall() and it returns a list of all the found strings
# Example search for a specific pattern, here 'some pattern'
strings = re.findall(r'some pattern', f.read())
print(strings)
print()

# Lastly, we can use findall with groups to capture multiple parts of each match
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

# Using findall with groups to capture both the username and the host (domain)
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## Output: [('alice', 'google.com'), ('bob', 'abc.com')]
print()

# Looping through the found tuples and printing each part (username and host)
for tuple in tuples:
    print(tuple[0])  ## Output: 'alice' and 'bob' (the usernames)
    print(tuple[1])  ## Output: 'google.com' and 'abc.com' (the domains)
print()
