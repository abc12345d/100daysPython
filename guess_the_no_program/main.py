#%%
import art
import random
from replit import clear

def run_game():

    welcome = '''Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.'''
    
    print(art.logo)
    print(welcome)

    lucky_no = random.randint(1,100)

    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if mode == "easy":
        no_guess = 10
    else:
        no_guess = 5

    is_game_over = False
    while (no_guess > 0 and not is_game_over):
        print(f"You have {no_guess} attempts remaining to guess the number.")
        guess = input("Make a guess: ")

        if int(guess) == lucky_no:
            is_game_over = True
            print(f"You got it! The answer was {lucky_no}.")
        elif int(guess) > lucky_no:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

        no_guess -= 1
        

while input("Do you want to play a game of Number Guessing Game? Type 'y' or 'n': ") == 'y':
    clear()
    run_game()
    
# %%
