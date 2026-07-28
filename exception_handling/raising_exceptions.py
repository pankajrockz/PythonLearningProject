'''
Raise Exception can be used when we have to set our own exception based on certain failure case. We can also handle
these exceptions with try-except for proper error handling. We can raise predefined exceptions like 'ValueError' or we
can also raise general exception called 'Exception' which can be any exception.
'''
salary = float(input("Enter your salary: "))
if salary < 0:
    raise ValueError("Salary cannot be negative!")
else:
    print(f'Your salary is {salary}')
'''
Output: 
1. When there is no exception raised
Enter your salary: 3
Your salary is 3.0

2. When exception is raised
Enter your salary: -1
Traceback (most recent call last):
  File "raising_exceptions.py", line 6, in <module>
    raise ValueError("Salary cannot be negative!")
ValueError: Salary cannot be negative!

Process finished with exit code 1

'''

age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!!!")
elif age >=18:
    print("You can vote!!!")
else:
    print("You cannot vote!!!")
'''
Output:
1. When exception is raised
Enter your age: -1
Traceback (most recent call last):
  File "raising_exceptions.py", line 28, in <module>
    raise ValueError("Age cannot be negative!!!")
ValueError: Age cannot be negative!!!

Process finished with exit code 1
2. When exception is not raised
Enter your age: 18
You can vote!!!
'''