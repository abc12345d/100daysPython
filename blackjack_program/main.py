############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

from replit import clear
import art
import random

def count_score(listOfCards):
    '''[cards] -> score of cards'''
    total = sum(listOfCards)
    no_of_11 = listOfCards.count(11)
    while no_of_11 and total > 21:
        total -= 10
        no_of_11 -= 1
        
    return total

def has_blackjack(listOfCards):
    '''get a list of two cards return True if the two cards form black jack else False'''
    if len(listOfCards) == 2 and count_score(listOfCards) == 21:
        return True
    return False

def get_final_message(player, comp):
    final_message = f"  Your final hand: {player}, final score: {count_score(player)}" 
    final_message += "\n"
    final_message += f"  Computer's final hand: {comp}, final score: {count_score(comp)} "
    final_message += "\n"

    return final_message

def get_card_message(player, comp):
    card_message = f"  Your cards: {player}, current score: {count_score(player)}" 
    card_message += "\n"
    card_message += f"  Computer's first card: {comp[0]}"
    card_message += "\n"

    return card_message

def run_game():

    player = [random.choice(cards), random.choice(cards)]
    comp = [random.choice(cards), random.choice(cards)]

    if has_blackjack(comp):
        print(get_final_message(player, comp))
        print("Comp got a blackjack! You lose.")
        return

    elif has_blackjack(player):
        print(get_final_message(player, comp))
        print("You got a blackjack! You win.")
        return
    
    print(get_card_message(player, comp))
    while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        player.append(random.choice(cards))

        if count_score(player) > 21:
            print(get_final_message(player, comp))
            print("You went over. You lose 😭")
            return
        
        print(get_card_message(player, comp))
        
    while count_score(comp) < 16:
        comp.append(random.choice(cards))

        if count_score(comp) > 21:
            print(get_final_message(player, comp))
            print("Opponent went over. You win 😁")
            return
    
    print(get_final_message(player, comp))
    if count_score(comp) == count_score(player):
        print("It's a draw.")
    elif count_score(comp) > count_score(player):
        print("You lose 😤")
    else:
        print("You win 😃")

    return

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    print(art.logo)
    run_game()