"""
Simple Arithmetic Module: arithmetic.py
"""

# We will use this module in the another file

def add(num1, num2):
    """
    This function is to add two number
    :param num1: First Number
    :param num2: Second Number
    :return: Return sum of num1 and num2
    """
    return num1 + num2

def square_root(num):
    """
    This function is to find the square root of a provided number
    :param num: Number for which the square root needed
    :return: Square root of the provided num
    """
    return float(num ** 0.5)

"""
Dunder name: In Python, __name__ is a built-in variable that tracks how a script is currently being executed.
This is a variable which will help to find the execution path.
So when we import this module the runnable code will also be executed hence to avoid that we use dunder name variable to
to check if code is running from the module itself or its being imported in some other module
"""

"""
This will always run while we run the current module or use it in any other module during import
a = 5
b = 6
print(add(5, 6))
"""

# So we can use the same under a if condition where we will check the __name__ is __main__
# As we imported this module in use_of_user_defined_module.py, so for
# use_of_user_defined_module => __name__ => "__main""
# this module(arithmetic.py) => __name__ => "arithmetic" => basically a module name
if __name__ == "__main__":
    a = 5
    b = 6
    print(add(5, 6))

