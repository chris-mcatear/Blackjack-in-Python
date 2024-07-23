import random 

from cards_list import full_list #Requires cards list from second file 

#Below print will print selected card, full_list[DECK NUMBER][CARD NUMBER]
# print(full_list[1][2])

#This will give random card from the list 
# print(full_list[random.randint(1, 4)][random.randint(1,52)])


def card_selector(): #This function will choose a card at random, storing the location of the card selected and then removing that card from the dictionary so it won't get drawn again. 
    chosen_deck = random.choice(list(full_list.keys())) #Randomly chooses from a list of the keys and assigns that key to chosen deck
    chosen_card = random.choice(list(full_list[chosen_deck].keys())) #Randomly chooses from a list of all items WITHIN the chosen deck
    # print(f"CHOSEN DECK: {chosen_deck}")
    # print(f"CHOSEN card: {chosen_card}") 
    final_card = full_list[chosen_deck][chosen_card] #This is the final selected card 
    # print(f"FINAL CARD: {final_card}")
    del full_list[chosen_deck][chosen_card]
    return final_card
    

def game_start():
    print("Hello, welcome to Blackjack")
    print("The aim is to get the closest to 21 without going over.")
    print("Going over 21, will result in you going bust and losing.")
    print("You will be facing the dealer (CPU) in a 1v1 scenario.")
    print("Here is your first hand: ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

# game_start()
# print(card_selector())


def deal_dealer_cards(): #Provides dealer's starting hand
    dealer_hand = card_selector() + " " + card_selector()
    return(dealer_hand)


def deal_player_cards(): #Provides players starting hand
    player_hand = card_selector() + " " + card_selector()
    return(player_hand)


def count_hand(hand): #Goal is to add additional number next to the hands to help people track what they have in hand. 
    hand = hand.split(' ') #Splits hand on spaces to get list of values in var
    # print(hand)
    for c in range(len(hand)): #Replaces the JQKA values with 10/10/10/11 - ACE to be fixed to be 1 or 11 
        # print(c) 
        if hand[c] == "K":
            # print("FOUND K")
            hand[c] = 10
        elif hand[c] == "Q":
            # print("FOUND Q")
            hand[c] = 10
        elif hand[c] == "J":
            # print("FOUND J")
            hand[c] = 10
        elif hand[c] == "A":
            hand[c] = 11
        else:
            pass

    sum = 0 # sum of the hand values after being changed to 10 for JQK
    pos = 1 # this is handling the position in  the hand list 
    for x in range(int(len(hand)/2)):
        # print(pos)
        sum = sum + int(hand[-pos])
        if pos <= len(hand):
            pos = pos + 2
        # print(f"new {-pos}")
    # print(f"sum: {sum}")
    return sum


player = deal_player_cards()
dealer = deal_dealer_cards()


print(f"Dealer has: {dealer} ({count_hand(dealer)})")
print(f"Player has: {player} ({count_hand(player)})")
#print(full_list)


# print(player.split(' '))
count_hand(player)
count_hand(dealer)
