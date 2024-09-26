from card_handler import face_checker

def hand_value(hand):
    hand = hand.split(' ')
    # print(hand)
    face_checker(hand)
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

def bust_check(hand):
    if hand_value(hand) > 21:
        return True
    else:
        return False
    
def score_calc(player, dealer):
    if player > dealer:
        print("Congrats, you win!")
    else: 
        print("Unlucky, you lost this time!")