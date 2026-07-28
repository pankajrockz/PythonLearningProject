"""
In python, we can pass a function as an argument of another function
"""

def add_1(number):
    return number + 1

def sq(number):
    return number ** 2

num = int(input('Enter a number: '))
res_1 = add_1(num)
res_2 = sq(res_1)
print(f'Output is: {res_2}')

# By passing function as an argument we can do thi
res = sq(add_1(num))
print(f'Output when passing function as an argument is: {res}')
