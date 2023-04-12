import art
import game_data
import random
from replit import clear


# get acc from game_data
def get_acc():
    '''randomly get an acc from game_data'''
    return random.choice(game_data.data)


def get_description(acc_dict):
    '''format the acc_dict for display'''
    return f"{acc_dict['name']}, a {acc_dict['description'].lower()}, from {acc_dict['country']}"


def get_compare_message(acc_dict_a, acc_dict_b):
    '''return compare message'''
    compare_message = f"Compare A: {get_description(acc_dict_a)}\n"
    compare_message += art.vs
    compare_message += "\n"
    compare_message += f"Against B: {get_description(acc_dict_b)}"

    return compare_message


def run_higher_lower_game():
    score_counter = 0
    is_game_over = False
    a = get_acc()
    b = get_acc()
    while a == b:
        b = get_acc()

    while not is_game_over:
        clear()
        print(art.logo)

        if score_counter > 0:
            print(f"You're right! Current score: {score_counter}")

        print(get_compare_message(a, b))

        guess = input("Who has more followers? Type 'A' or 'B': ")

        if a['follower_count'] > b['follower_count']:
            if guess == 'A':
                score_counter += 1
                a = a
                b = get_acc()
                while a == b:
                    b = get_acc()
            else:
                is_game_over = True
        else:
            if guess == 'B':
                score_counter += 1
                a = b
                b = get_acc()
                while a == b:
                    b = get_acc()
            else:
                is_game_over = True

    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score_counter}")


while input("Do you want to play a game of Higher-Lower? Type 'y' or 'n': ") == 'y':
    clear()
    run_higher_lower_game()
