#Type casting is the process of converting data from one type to anouther for example
#Converting an integer to a string

#Typecasting in python can be done in two ways implicit(Automatic) or explicit(Manual)

#By default python automatically converts one data type to anouther(Implicit conversion)
#An examples of this are shown below

#Converting an integer to a float
integer_num=123
float_num=1.23
print("Integer num",type(integer_num))
print("Type of float num",type(float_num))
new_num=integer_num+float_num

print("New num:- ",new_num)
print("Type of new number is:- ",type(new_num))
print()
#Here we have two variables one of type int one of type Float one of type int and one of type float 
#We have then added these two and stores the result in new_num
#Python by default performs these conversions unlike in languages like Java or C

#Note that adding an integer to a string results in an error as python is unable
#To perform implicit type conversion here resulting in a type error

int_num=21
str_num='12'
#print(int_num+str_num) #Uncommenting this code snippet results in a type error


#Explicit Type Conversion:-
#Explicit type conversion is when the user covnerts the data type manually to a desired data type
#Python has several built in functions for explicit type conversion such as
#int(),float(),str() and many more, the use of these functions is shown below
#Explicit type conversion is also known as Type Casting

#Operations on Integers
# Converting a string to an integer
str_num = "123"
int_num = int(str_num)
print("String to Integer:", int_num, type(int_num))

# Converting a float to an integer (truncates the decimal part)
float_num = 123.45
int_num = int(float_num)
print("Float to Integer (truncated):", int_num, type(int_num))
print()

#Operations on Floats
# Converting a string to a float
str_num = "123.45"
float_num = float(str_num)
print("String to Float:", float_num, type(float_num))

# Converting an integer to a float
int_num = 100
float_num = float(int_num)
print("Integer to Float:", float_num, type(float_num))
print()

#Operations on Strings
# Converting an integer to a string
int_num = 123
str_num = str(int_num)
print("Integer to String:", str_num, type(str_num))


# Converting a float to a string
float_num = 123.45
str_num = str(float_num)
print("Float to String:", str_num, type(str_num))
print()

#Operations on Boolean
# Converting various types to boolean
int_num = 0
float_num = 0.0
str_empty = ""
str_non_empty = "Python"

print("Integer to Boolean:", bool(int_num))        # False because 0 is falsy
print("Float to Boolean:", bool(float_num))        # False because 0.0 is falsy
print("Empty String to Boolean:", bool(str_empty)) # False because empty string is falsy
print("Non-Empty String to Boolean:", bool(str_non_empty)) # True because string is not empty
print()

#Operations on Lists
# Converting a string to a list
str_val = "Python"
list_val = list(str_val)
print("String to List:", list_val, type(list_val))

# Converting a tuple to a list
tuple_val = (1, 2, 3)
list_val = list(tuple_val)
print("Tuple to List:", list_val, type(list_val))
print()

#Operations on Tuples
# Converting a string to a tuple
str_val = "Python"
tuple_val = tuple(str_val)
print("String to Tuple:", tuple_val, type(tuple_val))

# Converting a list to a tuple
list_val = [1, 2, 3]
tuple_val = tuple(list_val)
print("List to Tuple:", tuple_val, type(tuple_val))
print()

#Operations on Sets
# Converting a string to a set
str_val = "hello"
set_val = set(str_val)
print("String to Set:", set_val, type(set_val)) # Removes duplicates

# Converting a list to a set
list_val = [1, 2, 3, 2, 1]
set_val = set(list_val)
print("List to Set:", set_val, type(set_val)) # Removes duplicates
print()

#Operations on Dictionary
# Converting a list of tuples to a dictionary
list_of_tuples = [("name", "Alice"), ("age", 25)]
dict_val = dict(list_of_tuples)
print("List of Tuples to Dictionary:", dict_val, type(dict_val))

# Converting a set of tuples to a dictionary
set_of_tuples = {("name", "Bob"), ("age", 30)}
dict_val = dict(set_of_tuples)
print("Set of Tuples to Dictionary:", dict_val, type(dict_val))
print()

#Operations on Complex Numbers
# Converting an integer to a complex number
int_num = 5
complex_num = complex(int_num)
print("Integer to Complex:", complex_num, type(complex_num))

# Converting a float to a complex number
float_num = 3.2
complex_num = complex(float_num)
print("Float to Complex:", complex_num, type(complex_num))

# Creating a complex number with real and imaginary parts
real_part = 2
imaginary_part = 3
complex_num = complex(real_part, imaginary_part)
print("Real and Imaginary to Complex:", complex_num, type(complex_num))

# By leveraging these type conversion functions, Python allows us to seamlessly adapt data types
# to meet the requirements of various operations, making it a versatile and powerful tool for developers
