
def func1():
    """
    This is a doc string
    We can write what the function does here
    :return: None
    """

    return None

print(help(func1))

def divide(num1, num2):
    """
    Number will be divided.
    :param num1: A number to be divided (Numerator)
    :param num2: A number that divides num1 (Denominator)
    :return: float (if num2 is non-zero) OR str (if num2 is 0)
    """
    if num2 == 0:
        return 'Cannot divide as denominator is 0!'
    return num1/num2

print(divide(2,1))
print(divide(2,0))
help(divide)
help(len)