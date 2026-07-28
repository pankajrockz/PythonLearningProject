# Function is block of code which can be called when required. We have builtin functions like print(), len(), etc.
# User define function: As builtin function is predefined function iwth python. Builtin functions are those which we can
# use to create based on the requirement.
# def function_name(arg1, arg2, ....argN):
#     statements1
#     statements1
#     .
#     .
#     statementsN

def greeting_someone(name):
    print(f'Hello {name}, good morning!')
    print('It\'s a beautiful day!')

#Calling the function
greeting_someone('Mark')
greeting_someone('John')
greeting_someone('Elon')

def add(num1, num2):
    result = num1 + num2
    print(f'Result: {result}')

#Calling
add(9, 4)
add(9, -4)

#Function with returning value
def even_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

#Calling
result = even_odd(2)
print(result)

#Changing the add function to return a single value
def add(num1, num2):
    result = num1 + num2
    return result

#Calling
val_1 = int(input('Enter first number: '))
val_2 = int(input('Enter second number: '))
val = add(val_1, val_2)
print(f'Addition of {val_1} and {val_2} is {val}')

#Returning multiple values
def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    return add, sub, mul

#Calling
val_1 = int(input('Enter first number: '))
val_2 = int(input('Enter second number: '))
res1, res2, res3 = arithmetic(val_1, val_2)
print(f'Addition of {val_1} and {val_2} is {res1}')
print(f'Substraction of {val_1} and {val_2} is {res2}')
print(f'Multiplication of {val_1} and {val_2} is {res3}')
