import pygame
from pygame.locals import *
import deck_init
import hand_select
import calculate
import time
import button
import hit
import sys
import betting
import disp_balance


### define user events
hit_event = pygame.USEREVENT + 1
ADD_hit = pygame.event.Event(hit_event)
stand_event = pygame.USEREVENT + 9
ADD_stand = pygame.event.Event(stand_event)

# betting
bet_10 = pygame.USEREVENT + 2
ADD_10 = pygame.event.Event(bet_10)
bet_25 = pygame.USEREVENT + 3
ADD_25 = pygame.event.Event(bet_25)
bet_100 = pygame.USEREVENT + 4
ADD_100 = pygame.event.Event(bet_100)

deal = pygame.USEREVENT + 5
deal_hand = pygame.event.Event(deal)

ADD_bet = [ADD_10, ADD_25, ADD_100, deal_hand]

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

# define font
font = pygame.font.SysFont('Grand9K Pixel', 35)
color = (255, 255, 255)

# define all necessary positions
# define initial position of hit card for player
player_hand_position = [100, 325]
dealer_hand_position = [100, 30]

# define where hit cards should go
player_hit_position = [70, 230]
# dealer_hit_position =

# buttons
hit_butt_position = [115, 450]
stand_butt_position = [30, 450]
# dd_butt_position =
# split_butt_position =

# chip positions (includes deal button position]
chip_positions = [[200, 400], [200, 430], [200, 460], [120, 420]]

# initiate balance
balance = 20

# GAME LOOP
# define global variable as key for event handler
key = 'betting'
disp_once = True
gameOn = True
while gameOn:
    # check game exit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False

        # ask for player bet
        match key:
            case 'betting':

                # stores the (x,y) coordinates into
                # the variable as a tuple
                mouse = pygame.mouse.get_pos()

                if disp_once:
                    # display balance
                    disp_balance.run(screen, balance, font, color)
                    disp_once = False

                # run betting (ask bet)
                betting.run(balance, screen, event, mouse, chip_positions, ADD_bet)

                # if each value triggered
                if event.type == bet_10:
                    # add to balance
                    balance += 10
                    # reset screen with updated bet
                    screen.blit(bg_img, (0, 0))
                    disp_balance.run(screen, balance, font, color)
                    betting.run(balance, screen, event, mouse, chip_positions, ADD_bet)
                    pygame.display.flip()

                if event.type == bet_25:
                    balance += 25
                    # reset screen with updated bet
                    screen.blit(bg_img, (0, 0))
                    disp_balance.run(screen, balance, font, color)
                    betting.run(balance, screen, event, mouse, chip_positions, ADD_bet)
                    pygame.display.flip()

                if event.type == deal:
                    # clear buttons and go to new hand
                    screen.blit(bg_img, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(500)
                    key = 'new hand'

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
                hit_butt = button.Button('hit', screen, hit_butt_position)
                stand_butt = button.Button('stand', screen, stand_butt_position)

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
                stand_butt.run_button(screen, event, mouse, stand_butt_position, ADD_stand)
                if event.type == stand_event:
                    print('stand')


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
