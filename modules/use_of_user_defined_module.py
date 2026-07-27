"""
Here we will import the user defined module arithmetic.py
"""
import arithmetic

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sqrt_num = float(input("Enter number for which square root required: "))

print(f'Sum of {num1} and {num2} using the user defined module arithmetic.py is {arithmetic.add(num1, num2)}')
print(f'Square root of {sqrt_num} using the user defined module arithmetic.py is {arithmetic.square_root(sqrt_num)}')

'''
Output:
Enter first number: 12
Enter second number: -6
Enter number for which square root required: 4.84
Sum of 12 and -6 using the user defined module arithmetic.py is 6
Square root of 4.84 using the user defined module arithmetic.py is 2.2
'''

