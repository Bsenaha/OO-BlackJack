# Deck Initialization (assigns img_IDs, values)
# returns card images and value list used for calculating hand value

from Card import Card


def run():
    from os import listdir
    from os.path import isfile, join

    # DECK INITIALIZATION
    # create list of img_IDs and according values
    # loop through folder to assign

    # assign clubs image file names to alpha list
    clubs_path = 'C:/Users/Brando/PycharmProjects/BlackJack GAME/game_images/cards/clubs'
    clubs_img = [f for f in listdir(clubs_path) if isfile(join(clubs_path, f))]

    # assign diamonds images ...
    diamonds_path = 'C:/Users/Brando/PycharmProjects/BlackJack GAME/game_images/cards/diamonds'
    diamonds_img = [f for f in listdir(diamonds_path) if isfile(join(diamonds_path, f))]

    # assign hearts images ...
    hearts_path = 'C:/Users/Brando/PycharmProjects/BlackJack GAME/game_images/cards/hearts'
    hearts_img = [f for f in listdir(hearts_path) if isfile(join(hearts_path, f))]

    # assign spades images ...
    spades_path = 'C:/Users/Brando/PycharmProjects/BlackJack GAME/game_images/cards/spades'
    spades_img = [f for f in listdir(spades_path) if isfile(join(spades_path, f))]

    # join lists to create combined deck
    card_img_IDs = [clubs_img + diamonds_img + hearts_img + spades_img
                    + clubs_img + diamonds_img + hearts_img + spades_img
                    + clubs_img + diamonds_img + hearts_img + spades_img
                    + clubs_img + diamonds_img + hearts_img + spades_img]

    # create value list of cards
    card_vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10] * 16

    # find card attributes and append it to deck
    deck = []
    for i in range(0, len(card_img_IDs[0])):

        # ID the card img
        card_img = card_img_IDs[0][i]

        # ID the suit based on position
        suit_ID = i % 52
        if suit_ID < 13:
            suit = 'clubs'
        elif suit_ID < 26:
            suit = 'diamonds'
        elif suit_ID < 39:
            suit = 'hearts'
        else:
            suit = 'spades'

        # find according value
        val = card_vals[i]
        deck.append(Card(suit, card_img, val))

    return deck
