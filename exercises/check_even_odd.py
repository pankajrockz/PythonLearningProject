'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
Expected Output:
The program should return an output like:
Enter a number: 7
7 is an odd number.
Enter a number: 12
12 is an even number.
'''

number = int(input('Enter a number: '))
if number % 2 == 0:
    print(f'{number} is an even number.')
else:
    print(f'{number} is an odd number.')







