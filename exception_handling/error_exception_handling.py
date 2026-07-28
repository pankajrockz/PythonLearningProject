"""
There are two type of error / exceptions in  Python:
1. Compile time error - In which we have two types of error, syntax error and indentation error
2. Exceptions - Are errors duing execution as there syntax is correct, like index error, file not found exception
"""

'''
Compile time error examples:
============================
1. Syntax error:
age =24
print(age 

=> Here we will get compile time error: SyntaxError: '(' was never closed

2. Indentation error
age =24
if age>=18
print("Adult")

=> Here we will get compile time error: IndentationError: expected an indented block after 'if' statement in line 17
'''

'''
print(10/0)
=> Here we will get runtime exception: ZeroDivisionError: division by zero

x = 100
result = x + y
=> Here we will get runtime exception: NameError: name 'y' is not defined
'''

'''
BuiltIn Exception: BuiltIn exceptions are exceptions when there is issue with the program and Python identifies the 
exceptions and give it to us. To handle these exception we can use `try-except` block.

Below lines of code will give runtime exception of ZeroDivisionError when num2 passed as 0
result = num1/num2
print(result)

We can use try-except to handle this effectively, like below
try:
    statement1
    statement2
except:
    statementWhenErrorEncountered
    
except: => This except will catch all the exceptions and its generally not a good practice. If we know which exception
we can get we can handle it accordingly like below.

We can also have multiple except blocks for different error. Like if we provided char in place of int for num1 or num2
it should thorow ValueError
'''
try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("The denominator cannot be 0")
except ValueError:
    print("Only integer values is allowed.")
