import random
from cards_list import full_list

def card_selector(): 
    """_summary_
    This function will choose a card at random, storing the location of the card selected and then removing that card from the dictionary so it won't get drawn again. 
    Returns:
        _type_: _description_
    """
    chosen_deck = random.choice(list(full_list.keys())) #Randomly chooses from a list of the keys and assigns that key to chosen deck
    chosen_card = random.choice(list(full_list[chosen_deck].keys())) #Randomly chooses from a list of all items WITHIN the chosen deck
    # print(f"CHOSEN DECK: {chosen_deck}")
    # print(f"CHOSEN card: {chosen_card}") 
    final_card = full_list[chosen_deck][chosen_card] #This is the final selected card 
    # print(f"FINAL CARD: {final_card}")
    del full_list[chosen_deck][chosen_card]
    return final_card


def face_checker(hand): 
    """Goal is to add additional number next to the hands to help people track what they have in hand."""
    # hand = hand.split(' ') #Splits hand on spaces to get list of values in var
    # print(hand)
    for c in range(len(hand)): #Replaces the JQKA values with 10/10/10/11 - ACE to be fixed to be 1 or 11 
        # print(c) 
        if hand[c] == "K" or hand[c] == "Q" or hand[c] == "J":
            hand[c] = 10
        elif hand[c] == "A":
            hand[c] = 11
        else:
            pass
    return hand
    # print(f"test hand: {hand}")