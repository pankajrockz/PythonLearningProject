import random

'''
Write a program to simulate a roll of die/dice
A die has 6 faces with numbers 1 to 6 written on them
The program should randomly print a number between 1 and 6
'''


print('Welcome to the game of rolling the dice!')

while True:
    choice = input("Press 'Enter' to roll a dice or q to quit: ").strip()
    if choice == 'q':
        print('Thanks for playing, Bye!')
        break
    elif choice == '':
        number = random.randint(1, 6)
        print(f'Your number is {number}')
    else:
        print('Invalid input')

print('GAME OVER!!!!')