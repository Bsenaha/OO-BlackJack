# randomly determines next drawn card
# removes from deck, adds to hand, assigns drawn card to "drawn"
# input:
# hand = existing hand (list of Cards)
# deck = existing deck (list of Cards)

# output:
# hand = new hand (list of Cards)
# deck = updated deck (list of Cards)
# drawn = drawn card (Card)

def run(hand, deck):
    import random

    drawn = random.choice(deck)
    deck.remove(drawn)
    hand.append(drawn)

    return drawn, deck, hand
