#Flow of control, If , else, elseif, match case

#Sample Variable
variable=5

#Flow of control begins with conditional statements.
#Python uses 'if','elif' and 'else' for decision-making.
#Indentaion plays a significant role in Python, the default is 4 blank spaces.

if variable>10:
    print("The variable is greater than 10 \n")
elif variable<10:
    print("The variable is lesser than 10 \n")
else:
    print("The variable is equal to 10 \n")

#As of python 3.10 We have anouther way of evaluating Conditionals called Match Cases
#A match case is essentially python's version of a Switch case, it is a clean way to handle 
#Multiple Conditionals instead of using if, elif and else statements
variable=12
match variable:
    case i if i>10: #Case for when i is greater than 10
        print("The variable is greater than 10 \n")
    case i if i<10: #Case for when i is lesser than 10
        print("The variable is lesser than 10 \n")
    case _: #Default Case when None of the previous Conditions are met
        print("The variable is equal to 10 \n")


#For loops:- Can be used to iterate over sequences like lists, tuples, ranges or strings.

#Example 1:- Iterating over a list
animals=["dog","cat","fish"]
for animal in animals:
    print(f"{animal} is a mammal") #Utillising f strings here for printing in a cleaner format


#Example 2:- Using the 'range()' function to generate numbers or an iterable of numbers
for i in range(4):
    print(i) #Prints 0,1,2,3
print()

#"range(Start,Stop)" returns an iterable of numbers from start to stop-1
for i in range(2,6):
    print(i) #Prints: 2,3,4,5
print()

#"range(Start,Stop,Step)" returns an iterable of numbers from start to stop while incrementing by step
#The default value of step is 1

for i in range(4,8,2):
    print(i) #prints 4,6
print()

#The enumerate function allows us to get both the index and value of an element in a list

animals=["dog","cat","fish"]
for i,val in enumerate(animals): #enumerate function allows us to loop with indices
    print(f"Index {i}:{val}")
print()

#Iterating thorugh a string with a for loop
sample_string="I love Python"
for char in sample_string:
    print(char,end=" ")
print()
#A while loops is a loop that continues looping until a condition is False.
x=0
while x<4:
    print(x)
    x+=1
print()
#A while loop can perform the same operations a for loop can in fact a while loop is more powerful than a for loop 

#Iterating through a string with a while loop
index=0
sample_string="I love Python"
while index<len(sample_string):
    print(sample_string[index],end=" ")
    index+=1
print()


#Exception Handling:- A how to on Managing errors gradefully.

try: #Block to execute code that might throw errors
    raise IndexError("An index error occured") #Intentionally triggering an index error
except IndexError: #Code to handle an Index Error
    print(f"Error: {IndexError}")# Displaying the error message
except(TypeError,NameError): #Code to handle other exceptions
    print("Oops looks like other errors occured") #Display message for other exceptions
else: #If no error occured this executes
    print("No errors occured.") #Indicates no error
finally: #This block always executes for cleanup
    print("Completed")
print()
#Essentially Exception handling allows us to prevent potentially fatal errors from causing our program to stop running


#File Handling:- A very important segment allowing us to read from ,write to and manage files.
#Python has several built in functions to interact with files .

#Opening Files:- Files in python can be opened using the open command. This returns a file object
with open("sampleFile.txt") as f: #Open function by default opens a file in read mode
    for line in f: #Iterate through each line in the opened file
        print(line)
print()
# A file can be opened in 3 formats
# 'r':- Read mode for when we only want to read data from a file
# 'w':- Write mode , this empties the previous contents of the file and instead puts the new content
# 'a':- Append mode, this allows us to simply add to the previous content of the file

#Writing to a file
content={'aa':12,"bb":21}
with open("myfile.txt","w") as file: #Openeing a file in write mode creates a new file of that name if one does not already exist
    file.write(str(content)) #Writes a string to the file

#We can also write files in various formats one popular format is json

import json #in order to handle json files we require this library
with open("myfile2.txt","w") as file:
    file.write(json.dumps(content)) #Writing the data as a json object
#It is important to note that here we are not using the json as a file type but instead as a format

with open("myfile.txt") as file:
    contents=file.read() #Reads a string from the file
    print(type(contents))
print(contents)

with open("myfile2.txt","r") as file:
    contents=json.load(file) #Reads a json object from the file
    print(type(contents))
print(contents)
print()

#We shall be exploring file handling in more detail as the days Progress so stay tuned


#Python also provides anouther abstraction called an iterable.
#An iterable is an object that can be treated as a sequence. One example is the output of the return function

sample_dict={"one":1,"two":2,"three":3}
our_iterable=sample_dict.keys() #This objecs implements our iterable
print(our_iterable)

#Once we have our iterable we can freely iterate over it
for i in our_iterable:
    print(i)
print()

#We cannot however index over an iterable
#Uncommenting the follwoing code results in a Type Error:
#our_iterable[1]

#An iterable is an object that can create an iterator 
print(our_iterable)
our_iterator=iter(our_iterable)
print(our_iterator,"\n")

#our_iterator is an object that keeps track of the state as we traverse through it.
#We can move to the next object with the "next()" function

print(next(our_iterator))
print(next(our_iterator))
print(next(our_iterator))
print()
#If we reach the end of an iterator using the next command again results in a stop Iteration Exception
#next(our_iterable) #Uncomment this code to see the error

#We can also use a for Loop to iterate through an iterable

our_iterator=iter(our_iterable) #Resetting the out_iterable
for i in our_iterator:
    print(i) #Prints one, two and three
print()

#We can also get all elements of an iterable by converting it to a list
print(list(our_iterable))
print(list(our_iterator))
