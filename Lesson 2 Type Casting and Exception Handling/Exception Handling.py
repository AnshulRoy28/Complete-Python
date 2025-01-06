#While Exceptions have already been covered in the basic syntax file
#We shall be going over them in more detail in this section

#Some Examples of errors are
#while True print("Hello World") #Syntax errors are a very common type of exception

#Division by Zero Error
#print(10*(1/0))

#Name Error:- Occures when a variable is called that has not been defined previously
#print(4+python*3)

#Type Error:- Occures when their is a mismatch of types in the program
#print('1'+1)

#Now handling these errors is a essential part of programming
#Below is a simple example for Revision

while True:
    try: # The try block is executed first
        x=int(input("Enter a number")) #If an exception occures here then we move to the except blocks
        break
    except ValueError:
        print("Not a value number Try again...")
print()
# A try clause can have multiple Except blocks but the downside is that only a single except block can run at any partciular point int time
# A Except handler bloack can also have multiple exceptions as shown below
try:
    x=int(input("Hi please enter a number"))
except(RuntimeError,TypeError,NameError,ValueError):
    print("Oops exception occured")

print()
# Exceptions also apply to classes, we can define a heirarchy of exceptions
class B(Exception):
    #Base exception class
    pass
class C(B):
    #A derived Class from B 
    pass
class D(C):
    #A derived Class from C (And indirectly from B)
    pass

#Iterate Through the list of Exception Classes[B,C,D]
for cls in [B,C,D]:
    try:
        #Rise an exception interface of the current class in the iteration
        raise cls()
    except D:
        #This block handles exceptions of type D
        # Since D is the most specific exception in the hierarchy, it will only catch instances of D.
        print("D")
    except C:
        # This block will handle exceptions of type C.
        # It also catches instances of any subclasses of C (like D),
        # but only if they weren't caught by a previous except block.
        print("C")
    except B:
        # This block will handle exceptions of type B.
        # It also catches instances of any subclasses of B (like C and D),
        # but only if they weren't caught by previous except blocks.
        print("B")
print()

#When an exception occures it might have some associated values known as its Arguments 
# The except clause may specify a variable after the exception name. This variable is bount 
#to the exception instace which has an args attribute that stores the arguments.
# Built in exception types define a __str__() to print all the arguments

# We're raising an exception here with two messages: 'spam' and 'eggs'
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    # Print the type of the exception (it will show 'Exception')
    print(type(inst))  # Shows that it's an Exception
    
    # Print the details (arguments) of the exception
    print(inst.args)  # Will print the tuple ('spam', 'eggs')
    
    # This is the string version of the exception (it’s automatically created)
    print(inst)  # This prints the message '('spam', 'eggs')'

    # We're unpacking the two arguments from the exception
    x, y = inst.args  # Unpacks the two values 'spam' and 'eggs'
    
    # Print out the arguments
    print("First argument: " + x)  # Prints 'First argument: spam'
    print("Second argument: " + y)  # Prints 'Second argument: eggs'

print()

# This block shows how we can handle common errors and keep track of them.
import sys

try:
    # Try to open a file and read the first line
    f = open('sampleFile.txt')
    s = f.readline()  # Read one line from the file
    i = int(s.strip())  # Convert the line to an integer (might fail if it's not a number)
except OSError as err:
    # If there's an error opening the file (like the file doesn't exist)
    print("Error with the file:", err)
except ValueError:
    # If the content can't be converted into an integer
    print("Couldn't turn the file content into a number.")
except Exception as err:
    # This catches all other errors that aren't specifically handled above
    print(f"Unexpected error: {err}")
    # Reraise the error to stop the program and show it to the user
    raise

print()

# The 'else' block: It runs only if everything in 'try' worked with no issues.
try:
    # Try to open a file for reading
    file_name = "example.txt"
    f = open(file_name, 'r')
except FileNotFoundError:
    # If the file doesn't exist, print an error
    print(f"Oops! The file '{file_name}' is missing.")
except OSError as e:
    # If there are any other problems (like permission issues), print them
    print(f"Couldn't open the file '{file_name}'. Reason: {e}")
else:
    # If there were no errors, run this part to process the file
    content = f.read()  # Read the content of the file
    print(f"The file '{file_name}' has {len(content.splitlines())} lines.")  # Count and print the lines
    f.close()  # Always remember to close the file after using it
print()

#Exceptions are handled even if they occur inside functions called by the try bloack like below 

def div_by_zero():
    sample=1/0 #Divide by zero error

try:
    div_by_zero() #Calling this function results in an exeption to occur which is in turn handled by the except block
except ZeroDivisionError as err:
    print("Handling run time error that occured in the function: ",err)
print()


#We can alsoe raise exceptions artifially forcing them to occur
#raise(NameError("Hi how are you")) #Uncommenting this code forces the name error to occur

#Multiple Exceptions can occur at the same time as well i.e when an exception occures inside an 
#Except block as shown below

#try:
#    open("Sample.txt")
#except OSError:
#    raise RuntimeError("Unable to handle the OS Error")

#Anouther Example of Chaining Exmaples
#def func():
#    raise ConnectionError #Inside this function we raise the Connection Error
#try:
#    func() #Calling the function to trigger the Exception
#except ConnectionError as exc: #Calling the exception as an alias
#    raise RuntimeError('Failed to open the database') from exc #Raise a secondary exception inside the original handle block for the exception

#We are also able to disable Automatic Exception Chaining by using the from None Idiom

print("Preventing the Exception chain from being Triggered")
try:
    #Inner Try Except Block to handle the OSError
    try:
        #Attempt to the file that does not exist
        open('myFile.txt')
    except OSError:
        #When the OS error occures raise a Runtime Error
        #The "from None" ensures that we do not chain together any more exceptions
        raise RuntimeError("Custom Message: I am unable to open the File") from None
except RuntimeError as err:
    #Add an outer Except block to catch the RuntimeError
    print(f"RuntimeError Handled {err}")

print("We handled the Exceptions")



