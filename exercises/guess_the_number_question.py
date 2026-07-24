'''
Create a simple nuber guessing game.
User gets 10 chances to guess a number.
If the user guesses the number before 10 chances, stop asking the number from the user, say Congrats and end the game.
If user never guesses the number in 10 chances, stop asking the number from the user and end the game.
'''
import random
winning_number = random.randint(1, 50)
chances = 10
if_guess_correct = False
print("WELCOME TO GUESS THE NUMBER GAME..........")
print("The secret number is between 0 and 50")
for i in range(10):
    print(f'You have {chances} chances to guess the number.')
    user_choice = int(input('Enter a guess: '))
    if user_choice == winning_number:
        print(f'Congrats, you win! You guessed the number in {10-chances+1} chances.')
        if_guess_correct = True
        break
    elif user_choice > winning_number:
        chances -= 1
        print(f'Your guess is wrong! Try lower')
    elif user_choice < winning_number:
        chances -= 1
        print(f'Your guess is wrong! Try higher')

if not if_guess_correct:
    print(f'You exhausted all your chances, the correct number was {winning_number}')
print('GAME OVER, COME BACK AGAIN!!!!!')