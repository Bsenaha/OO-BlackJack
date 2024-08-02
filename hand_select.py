# Draw Starting Hands (random)

def run(deck):
    import random

    player.card1 = random.sample(deck, 1)
    deck.remove(player_card1)

    dealer_card1 = random.sample(deck, 1)
    deck.remove(dealer_card1)

    player_card2 = random.sample(deck, 1)
    deck.remove(player_card2)

    dealer_card2 = random.sample(deck, 1)
    deck.remove(dealer_card2)
