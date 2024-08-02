import pygame
from pygame.locals import *
import deck_init
import hand_select
import calculate

# initialize
pygame.init()

# Create Screen & title
screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption("BlackJack")

image = pygame.image.load("game_images/cards/clubs/card_clubs_02.png")
position = (0, 0)

# GAME LOOP
gameOn = True
while gameOn:
    # check game exit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False

    # check player balance

    # shuffle check
    # initialize deck
    # # # if shuffle:
    deck = deck_init.run()

    # ask player bet

    # hand select
    player_hand, dealer_hand = hand_select.run(deck)
    # calculate
    player_val, bust = calculate.run(player_hand)

    # Player BJ Checks & potential cash-out

    # insurance case

    # regular dealer BJ Check, potential cash-out

    # ===== Player turn begin =====
    # # # H, S, D, P # # #
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


    screen.blit(image, position)

    pygame.display.flip()
