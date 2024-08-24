import pygame
from pygame.locals import *
import deck_init
import hand_select
import calculate
import time
import button
import hit
import sys

hit_event = pygame.USEREVENT + 1
ADD_hit = pygame.event.Event(hit_event)

# initialize
pygame.init()

# Create Screen & title
screen_width = 300
screen_height = 500
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("BlackJack")

# blit BG image
bg_img = pygame.image.load('game_images/Table.jpg')
bg_img = pygame.transform.scale(bg_img, screen_size)
# disp bg image
screen.blit(bg_img, (0, 0))

# define all necessary positions
# define initial position of hit card for player
player_hand_position = [100, 325]
dealer_hand_position = [100, 30]

# define where hit cards should go
player_hit_position = [100, 200]
# dealer_hit_position =

# buttons
hit_butt_position = [115, 450]
# stand_butt_position =
# dd_butt_position =
# split_butt_position =

# define button attributes
width = 80
height = 100
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)

# GAME LOOP

# define global variable as key for event handler
key = 'new hand'
gameOn = True
while gameOn:
    # check game exit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False

        # dealing new hand
        match key:
            case 'new hand':
                # initialize deck
                deck = deck_init.run()
                player_hand, dealer_hand = hand_select.run(deck)

                for i in range(0, 2):
                    screen.blit(player_hand[i].image, player_hand_position)
                    pygame.display.update()
                    player_hand_position[0] += 30
                    player_hand_position[1] += 20
                    pygame.time.delay(500)

                    screen.blit(dealer_hand[i].image, dealer_hand_position)
                    pygame.display.update()
                    dealer_hand_position[0] += 30
                    dealer_hand_position[1] += 20
                    pygame.time.delay(500)

                key = 'Player Decision'

        # if player's turn
        match key:
            case 'Player Decision':
                # initialize player option buttons
                hit_butt = button.Button('hit', screen, hit_butt_position)  # [100,400]

                # stores the (x,y) coordinates into
                # the variable as a tuple
                mouse = pygame.mouse.get_pos()

                # IF HIT
                hit_butt.run_button(screen, event, mouse, hit_butt_position, ADD_hit)
                if event.type == hit_event:
                    hand_value, bust, drawn = hit.run(player_hand, deck, 0)
                    screen.blit(drawn.image, player_hit_position)
                    pygame.display.update()
                    player_hit_position[0] += 40

                # IF DD

                # IF STAND


    # check player balance

    # shuffle check
    # initialize deck
    # # # if shuffle:

    # ask player bet

    # hand select
    # player_hand, dealer_hand = hand_select.run(deck)
    # calculate
    # player_val, bust = calculate.run(player_hand)
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
