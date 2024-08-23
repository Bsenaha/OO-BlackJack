# Hit Function (Draw Card)
# draws card to given hand AND recalculates hand value
# input:
# hand = existing hand (list of Cards)
# deck = existing deck (list of Cards)

# output:
# hand = new hand (list of Cards)
# hand value = numerical value of hand
# # bust = busted or not busted
# deck = updated deck (removed drawn Card)

def run(hand, deck, turn):
    import draw_card
    import calculate

    # draw Card
    # add drawing animation to hand position
    drawn, deck, hand = draw_card.run(hand, deck)

    # calculate
    hand_value, bust = calculate.run(hand)

    return hand_value, bust, drawn
