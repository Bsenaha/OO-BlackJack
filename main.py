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
import disp_bet
import cashout


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

# load card back
card_back_img = pygame.image.load('game_images/cards/card_back.png')
card_back_img = pygame.transform.scale(card_back_img, (70, 80))

# define font
font = pygame.font.SysFont('Grand9K Pixel', 35)
color = (255, 255, 255)

# define all necessary positions
# define initial position of hit card for player
player_hand_position = [100, 325]
dealer_hand_position = [100, 30]

# define where hit cards should go
player_hit_position = [70, 230]
dealer_hit_position = [70, 140]

# buttons
hit_butt_position = [115, 450]
stand_butt_position = [30, 450]
# dd_butt_position =
# split_butt_position =

# chip positions (includes deal button position]
chip_positions = [[200, 400], [200, 430], [200, 460], [120, 420]]

# initiate bet and balance
balance = 100
bet = 0

# GAME LOOP
# define global variable as key for event handler
key = 'betting'
disp_once = True
check_player_BJ = True
check_dealer_BJ = True

# set game cashout conditions
dealer_bust = False
player_BJ = False
win = False

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

                # runs once (reset stuff)
                if disp_once:
                    # display balance
                    disp_balance.run(screen, balance, font, color)
                    disp_bet.run(screen, bet, font, color)
                    win = False
                    disp_once = False

                # run betting (ask bet)
                betting.run(balance, screen, event, mouse, chip_positions, ADD_bet)

                # if each value triggered
                if event.type == bet_10:
                    # add to balance
                    bet += 10
                    balance -= 10
                    # reset screen with updated bet
                    screen.blit(bg_img, (0, 0))
                    disp_balance.run(screen, balance, font, color)
                    disp_bet.run(screen, bet, font, color)
                    betting.run(balance, screen, event, mouse, chip_positions, ADD_bet)
                    pygame.display.flip()

                if event.type == bet_25:
                    bet += 25
                    balance -= 25
                    # reset screen with updated bet
                    screen.blit(bg_img, (0, 0))
                    disp_balance.run(screen, balance, font, color)
                    disp_bet.run(screen, bet, font, color)
                    betting.run(balance, screen, event, mouse, chip_positions, ADD_bet)
                    pygame.display.flip()

                if event.type == deal:
                    # clear buttons and go to new hand
                    screen.blit(bg_img, (0, 0))
                    # display bet
                    disp_balance.run(screen, balance, font, color)
                    disp_bet.run(screen, bet, font, color)
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
                    # disp card back for dealer second card
                    if i == 1:
                        screen.blit(card_back_img, dealer_hand_position)
                        dealer_hand_position[0] -= 30
                        dealer_hand_position[1] -= 20

                    pygame.display.update()
                    dealer_hand_position[0] += 30
                    dealer_hand_position[1] += 20
                    pygame.time.delay(500)

                key = 'Player Decision'

        # if player's turn
        match key:
            case 'Player Decision':

                # check blackjack
                player_value, player_bust = calculate.run(player_hand)
                if check_player_BJ:
                    if player_value == 21:
                        print('player blackjack')
                        key = 'End Turns'
                    check_player_BJ = False

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
                    key = 'Dealer Turn'

                if player_bust:
                    print('player bust')
                    pygame.time.delay(2000)
                    # display player bust, short pause
                    key = 'End Turns'


        match key:
            case 'Dealer Turn':

                # check blackjack
                dealer_value, dealer_bust = calculate.run(dealer_hand)
                if check_dealer_BJ:
                    screen.blit(dealer_hand[1].image, dealer_hand_position)
                    pygame.display.update()
                    pygame.time.delay(1000)
                    if dealer_value == 21:
                        print('dealer blackjack')
                        key = 'End Turns'
                    check_dealer_BJ = False

                if dealer_bust:
                    key = 'End Turns'


                if dealer_value < 17:
                    dealer_value, bust, drawn = hit.run(dealer_hand, deck, 0)
                    pygame.time.delay(500)
                    screen.blit(drawn.image, dealer_hit_position)
                    pygame.display.update()
                    dealer_hit_position[0] += 40

                else:
                    key = 'End Turns'

        match key:
            case 'End Turns':
                # check busts first
                if player_bust:
                    print('player bust')
                    pygame.time.delay(500)
                    balance = cashout.run(balance, bet, player_BJ, win)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    key = 'betting'

                elif dealer_bust:
                    print('dealer bust')
                    win = True
                    pygame.time.delay(500)
                    balance = cashout.run(balance, bet, player_BJ, win)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    key = 'betting'

                # compare hand values
                elif player_value > dealer_value:
                    print('player win')
                    win = True
                    pygame.time.delay(500)
                    balance = cashout.run(balance, bet, player_BJ, win)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    key = 'betting'

                elif dealer_value > player_value:
                    print('dealer win')
                    pygame.time.delay(500)
                    balance = cashout.run(balance, bet, player_BJ, win)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    key = 'betting'

                elif dealer_value == player_value:
                    print('push')
                    pygame.time.delay(500)
                    balance += bet
                    pygame.display.update()
                    pygame.time.delay(2000)
                    key = 'betting'

                # clear table, buttons, and go to new hand
                screen.blit(bg_img, (0, 0))

                # re-initialize values
                # define initial position of hit card for player
                player_hand_position = [100, 325]
                dealer_hand_position = [100, 30]

                # define where hit cards should go
                player_hit_position = [70, 230]
                dealer_hit_position = [70, 140]

                # reset player bet
                bet = 0
                disp_once = True

                # reset BJ check
                check_player_BJ = True
                check_dealer_BJ = True

                # reset and dealer bust
                dealer_bust = False

    pygame.display.flip()
pygame.quit()
