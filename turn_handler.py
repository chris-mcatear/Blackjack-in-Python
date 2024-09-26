from card_handler import *
from score_tracker import *

def player_turn(player):
    print(f"Current Hand: {player} ({hand_value(player)})")
    while hand_value(player) < 22:
        hit_or_stick = input("Do you want to hit or stick? (H / S) : ")
        if hit_or_stick.lower() == "h":
            new_card = card_selector()
            player = player + f" {new_card}"
            print(f"You got dealt {new_card}")
            print(f"Current Hand: {player} ({hand_value(player)})")
        elif hit_or_stick.lower() == "s":
            return
        else:
            print("Invalid input, do you want to hit or stick? (H / S) : ")
    else: 
        print("oh no you're bust loser")
            
            
def dealers_turn(dealer):
    if hand_value(dealer) < 16:
        dealer = dealer + " " + card_selector()
        print("Dealer takes another card...")
        print(f"Dealer new hand: {dealer} ({hand_value(dealer)})")
    elif hand_value(dealer) > 21:
        print("The dealer is bust! Player wins!")
    else: 
        pass
        
