'''
.py file is a module
Usage: Similar type of tasks or functions can be made part of single python file to group togather so the code is easier to
code or read. This also make code logically organized

There are two types of module
1. Builtin Modules: These modules are availble by default when we install python like Math, random, datetime, etc.
2. User defined Modules

We need to import a module and then start using the functions of the modules.
Syntax: import module_name
Syntax of importing only few functions of module: from module_name import f1, f2, f3
Syntax of import and create an alias name for the module: import module_name as alias_name
'''

#BuiltIn Module
import math #Entire module is imported
num = 100
output = math.sqrt(num)
print(f'Square roo of {num} is {output}')
'''
Output:
Square roo of 100 is 10.0
'''

# Calculating area of circle.
# Math module has pi value
radius = 5
area_of_circle = math.pi * (radius ** 2)
print(f'Area of circle with radius {radius} is {area_of_circle}')
'''
Output:
Area of circle with radius 5 is 78.53981633974483
'''

# Throw a die problem where we use randint function of random module
from random import randint

value = randint(1,6) # When we import only a method of a module, we don't need to write the module name while calling
print(f'Random value of a die is: {value}')
'''
Output:
Random value of a die is: 3
'''

# Import module and set an alias
import datetime as dt
t = dt.time(8, 43, 51)
print(f'Formated time is {t}')
'''
Output:
Formated time is 08:43:51
'''
