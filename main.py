import random 

from cards_list import full_list #Requires cards list from second file 

#Below print will print selected card, full_list[DECK NUMBER][CARD NUMBER]
# print(full_list[1][2])

#This will give random card from the list 
# print(full_list[random.randint(1, 4)][random.randint(1,52)])

def card_selector(): #This function will choose a card at random, storing the location of the card selected and then removing that card from the dictionary so it won't get drawn again. 
    chosen_deck = random.randint(1, 4) #Chooses random deck (From deck 1 - 4 ) 
    chosen_card = random.randint(1, 52) #Chooses random card from the chosen deck (1 - 52) 
    final_card = full_list[chosen_deck][chosen_card] #This is the final selected card 
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


def deal_player_cards(): #Provides players starting hand
    player_hand = card_selector() + " " + card_selector()
    return(player_hand)


def deal_dealer_cards(): #Provides dealer's starting hand
    dealer_hand = card_selector() + " " + card_selector()
    return(dealer_hand)


def count_hand(hand):
    hand = hand.split(' ')
    for c in range(len(hand)):
        print(c) 
        if hand[c] == "K":
            print("FOUND")
            hand[c] = 10
        else:
            pass
    print(f"hand: {hand}")
    print(f"Hand total: {sum(hand)}")
    # print(len(hand))
    # print(hand[1])
    
    # sum = 0
    # for x in range(len(hand)):
    #     if x % 2 != 0:
    #         sum = sum + x
    #     else:
    #         pass
    # print(f"sum: {sum}")


player = deal_player_cards()
dealer = deal_dealer_cards()

print(f"Dealer has: {dealer}")
print(f"Player has: {player}")

# print(player.split(' '))
count_hand(player)