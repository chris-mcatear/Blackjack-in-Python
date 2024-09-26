import random 
from card_handler import * 
from turn_handler import *
from players_handler import *
from cards_list import full_list #Requires cards list from second file 
# from dealer import dealers_turn #This doesn't work rip 

#Below print will print selected card, full_list[DECK NUMBER][CARD NUMBER]
# print(full_list[1][2])

#This will give random card from the list 
# print(full_list[random.randint(1, 4)][random.randint(1,52)])

def game_start():
    print("Hello, welcome to Blackjack")
    print("The aim is to get the closest to 21 without going over.")
    print("Going over 21, will result in you going bust and losing.")
    print("You will be facing the dealer (CPU) in a 1v1 scenario.")
    print("Here is your first hand: ")


# def ace_checker(hand):
#     if face_checker(hand) > 21:
        
        
# def final_scoring(player, dealer): 
#     #TODO
    

print(f"Dealer has: {dealer} ({hand_value(dealer)})")
print(f"Player has: {player} ({hand_value(player)})")
#print(full_list)


# player = player + " " + card_selector()
# print(f"{player} : {hand_value(player)}")


player_turn(player)
dealers_turn(dealer)
score_calc(player, dealer)