# Draw Starting Hands (random)
# input:
# deck = list of Card classes containing all unused cards

# output:
# player hand = list of Cards in player starting hand
# dealer hand = list of Cards in dealer starting hand

def run(deck):
    import random

    # draw Cards (one after another) for initial hand
    # add drawing animation to hand position
    player_card1 = random.sample(deck, 1)
    deck.remove(player_card1)
    # animate card draw

    dealer_card1 = random.sample(deck, 1)
    deck.remove(dealer_card1)
    # animate card draw

    player_card2 = random.sample(deck, 1)
    deck.remove(player_card2)
    # animate card draw

    dealer_card2 = random.sample(deck, 1)
    deck.remove(dealer_card2)
    # animate card draw

    player_hand = [player_card1, player_card2]
    dealer_hand = [dealer_card1, dealer_card2]

    return player_hand, dealer_hand
