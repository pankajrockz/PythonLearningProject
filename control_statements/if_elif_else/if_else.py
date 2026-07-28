#if
#Syntax of if where statement 1 to statement n is only executed when condition is true.
#For conditions, we use relational operator ==, >=, <=, >, <, !=
# if condition:
#     statement 1
#     statement 2
#     .
#     .
#     statement n
# statement N

age = float(input('What is your age?'))
if age >= 18:
    print(f'Congrats!you are an adult with age {age}. You can cast vote!!!')
print('Rest of the program')

#if-else
# if condition:
#     statement 1
#     statement 2
#     .
#     .
#     statement n
# else:
#     block of code when condition is false.
# statement N

age = float(input('What is your age?'))
if age >= 18:
    print(f'Congrats!you are an adult with age {age}. You can cast vote!!!')
else:
    print(f'Few more years before you can vote. Remaining years are {18 - age}')
print('Rest of the program')

#Write a program to print if number is even or odd
#even = when number is divisible by 2. Remainder should be 0
#odd = when number is not divisible by 2. Remainder should not be 0

num = int(input('Enter a number: '))
if num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

#Write a program to check if the number is negative or positive

num1 = float(input('Enter a number: '))
if num1 >=0:
    print(f'{num1} is positive')
else:
    print(f'{num1} is negative')