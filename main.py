import pygame
from pygame.locals import *
import deck_init
import hand_select
import calculate
import time
import button
import hit
import sys

hit_event = pygame.USEREVENT + 0


# initialize
pygame.init()

# Create Screen & title
screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption("BlackJack")


img = pygame.image.load('game_images/cards/clubs/card_clubs_02.png')

# GAME LOOP
gameOn = True
# define global variable as key for event handler
key = 'new hand'

# define initial position of hit card for player
position = [0, 0]

while gameOn:
    # check game exit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False

        # dealing new hand
        if key == 'new hand':
            # initialize deck
            deck = deck_init.run()
            player_hand, dealer_hand = hand_select.run(deck)

            # initialize player option buttons
        hit_butt = button.Button('hit', screen)

        # if button clicked
        if hit_butt.isClicked(screen) and key == 'new hand':
            print('hit')
            value, bust, drawn = hit.run(player_hand, deck, 0)
            img = drawn.image
            screen.blit(img, position)
            position[0] += 40
            print(position)
            # disallow actions

        # if player's turn
        if key == 'player decision':
            if event.type == hit:   # if hit
                screen.blit(img, position)

            # elif event.type ==

    # check player balance

    # shuffle check
    # initialize deck
    # # # if shuffle:

    # ask player bet

    # hand select
    #player_hand, dealer_hand = hand_select.run(deck)
    # calculate
    #player_val, bust = calculate.run(player_hand)
    # Player BJ Checks & potential cash-out

    # insurance case

    # regular dealer BJ Check, potential cash-out

    # ===== Player turn begin =====
        # if H

        # if S
        # if D
        # if P

        # if busted, cash-out
        # if hit 21, display, end turn
        # ===== Player turn end =====

        # ===== Dealer turn begin =====
        # reveal hand
        # # # H, S, D, P # # # (depending on < 17)

        # if 21, cash-out
        # if bust, cash-out
    # ===== Dealer turn end =====

    # Compare hands
    # Final cash-out




    pygame.display.flip()
pygame.quit()
