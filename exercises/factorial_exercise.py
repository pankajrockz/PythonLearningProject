
def factorial(num):
    fact = 1
    if num < 0:
        print('Factorial of negative number can\'t be defined.')
    elif num == 1 or num == 0:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f'Factorial of {number} is: {factorial(number)}')