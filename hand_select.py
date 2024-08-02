# Draw Starting Hands (random)
# input:
# deck = list of Card classes containing all unused cards

# output:
# player hand = list of Cards in player starting hand
# dealer hand = list of Cards in dealer starting hand
# deck =

def run(deck):
    import random
    import draw_card

    # initiate hands
    player_hand = []
    dealer_hand = []

    # draw Cards (one after another) for initial hand
    # Player 1
    drawn, deck, player_hand = draw_card.run(player_hand, deck)
    # animate card draw

    # Dealer 1
    drawn, deck, dealer_hand = draw_card.run(dealer_hand, deck)
    # animate card draw

    # Player 2
    drawn, deck, player_hand = draw_card.run(player_hand, deck)
    # animate card draw

    # Dealer 2
    drawn, deck, dealer_hand = draw_card.run(dealer_hand, deck)
    # animate card draw

    return player_hand, dealer_hand
