# Draw Starting Hands (random)

def run(card_img_IDs, card_vals):
    import random

    Valid_hand = False

    while not Valid_hand:
        hand_player = random.sample(card_img_IDs, 2)