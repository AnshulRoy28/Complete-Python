#A module is a file that contains code snippets, this includes functions, classes or even Variables allowing us to use and orgnaise these easily 

#we can access a module using the import keyword
import math #Math is a module that cotains various mathematical functions.
print(math.sqrt(16)) #in order to use a module use a simply do modulename.functioname
print("\n")

from math import ceil,floor # we can also import specific functions from a module
print(ceil(3.7))
print(floor(3.7))
print()

from math import * #We can also import all functions from module tho this is not reccomended as it takes unnessesary space

import math as m # We can also assign names to modules, this is called aliasing
print(math.sqrt(16)==m.sqrt(16))
print()

import math
print(dir(math)) #We can also use the dir command to find all the functions present in a module
print()

#We can also create our own modules, to do so simply create ur functions in a seperate file
#and import them
#Keep in mind however if we have created a module called math and we import math in our code file
# the program will load our math.py file instead of the in built module
#this is because local files have higher priority than pythons in built modules
