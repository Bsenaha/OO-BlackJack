# Calculate input hand total value
# input:
# hand = list of Cards in hand

# output:
# hand value = numerical value of hand
# bust = busted or not busted


def run(hand):
    hand_tot = 0
    ace_in_hand = 0
    for Card in hand:
        hand_tot += Card.value  # add card value to hand total
        if Card.value == 11:
            ace_in_hand += 1
    hand_value = hand_tot

    # if bust (consider ace first)
    while hand_value > 21:
        if ace_in_hand == 0:
            bust = True
            return hand_value, bust
        if ace_in_hand:
            ace_in_hand -= 1
            hand_value -= 10

    # if busted
    if hand_value > 21:
        bust = True
        return hand_value, bust

    # if 21
    elif hand_value == 21:
        bust = False
        return hand_value, bust

    # if not busted
    elif hand_value < 21:
        bust = False
        return hand_value, bust
