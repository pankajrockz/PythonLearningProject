"""
Recursion - Recursion is a process in which a function calls itself  till certain condition is met.
Factorial of n => n * (n-1) * (n-2)....2*1

There are 2 parts to any recursive function
1. Base/terminal condition
2. Recursive condition
"""

#Factorial without recursion

def fact(num =5):
    factor = 1
    while num > 1:
        factor *= num
        num -= 1
    return factor

num = 5
print(f'Factorial of {num} is {fact(num)}')


# Factorial with Recursion
def fact_with_recursion(num):
    if num == 1:
        return 1
    else:
        fact = num * fact_with_recursion(num - 1)
        return fact

num = 5
print(f'Factorial of {num} with recursion is {fact(num)}')
