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
import animate
import Card
import disp_value

### define user events
hit_event = pygame.USEREVENT + 1
ADD_hit = pygame.event.Event(hit_event)
stand_event = pygame.USEREVENT + 9
ADD_stand = pygame.event.Event(stand_event)
DD_event = pygame.USEREVENT + 8
ADD_DD = pygame.event.Event(DD_event)

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
card_back = Card.Card('card back', 'card_back.png', 0)
deal_speed = 1500
small_delay = 200

# define font
font = pygame.font.Font('Emulogic-zrEw.ttf', 15)
color = (255, 255, 255)

# define all necessary positions
# define initial position of hit card for player
player_hand_position = [100, 325]
dealer_hand_position = [100, 30]

# define where hit cards should go
player_hit_position = [70, 230]
dealer_hit_position = [70, 140]

# define where to display hand values
player_value_position = [70, 350]
dealer_value_position = [70, 55]

# buttons
hit_butt_position = [115, 430]
stand_butt_position = [30, 430]
DD_butt_position = [200, 430]
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
dealer_BJ = False
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
                    pygame.display.update()
                    pygame.time.delay(400)
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

                    animate.run(screen, player_hand[i], player_hand_position, deal_speed)
                    player_hand_position[0] += 30
                    player_hand_position[1] += 20
                    pygame.time.delay(small_delay)

                    if i == 0:
                        animate.run(screen, dealer_hand[i], dealer_hand_position, deal_speed)
                    # disp card back for dealer second card
                    if i == 1:
                        animate.run(screen, card_back, dealer_hand_position, deal_speed)
                        dealer_hand_position[0] -= 30
                        dealer_hand_position[1] -= 20

                    dealer_hand_position[0] += 30
                    dealer_hand_position[1] += 20
                    pygame.time.delay(small_delay)

                key = 'Player Decision'

        # if player's turn
        match key:
            case 'Player Decision':

                # check blackjack
                player_value, player_bust = calculate.run(player_hand)

                # runs once to check for BJ
                if check_player_BJ:
                    player_value_text = font.render(f'{player_value}', True, color)
                    screen.blit(player_value_text, player_value_position)

                    if player_value == 21:
                        player_BJ = True
                        key = 'End Turns'
                    check_player_BJ = False

                # initialize player option buttons and hand value
                hit_butt = button.Button('Hit', screen, hit_butt_position)
                stand_butt = button.Button('Stand', screen, stand_butt_position)
                DD_butt = button.Button('Double Down', screen, DD_butt_position)

                # stores the (x,y) coordinates into
                # the variable as a tuple
                mouse = pygame.mouse.get_pos()

                # IF HIT
                hit_butt.run_button(screen, event, mouse, hit_butt_position, ADD_hit)
                if event.type == hit_event:
                    hand_value, bust, drawn = hit.run(player_hand, deck, 0)
                    animate.run(screen, drawn, player_hit_position, deal_speed)
                    player_hit_position[0] += 40
                    player_value, player_bust = calculate.run(player_hand)
                    disp_value.run(screen, player_value, font, player_value_position, bg_img, color)

                # IF DD
                DD_butt.run_button(screen, event, mouse, DD_butt_position, ADD_DD)
                if event.type == DD_event:
                    hand_value, bust, drawn = hit.run(player_hand, deck, 0)
                    animate.run(screen, drawn, (110, 230), deal_speed)
                    player_value, player_bust = calculate.run(player_hand)
                    disp_value.run(screen, player_value, font, player_value_position, bg_img, color)
                    pygame.time.delay(400)
                    key = 'Dealer Turn'

                # IF STAND
                stand_butt.run_button(screen, event, mouse, stand_butt_position, ADD_stand)
                if event.type == stand_event:
                    pygame.time.delay(400)
                    key = 'Dealer Turn'

                if player_bust:
                    # display player bust, short pause
                    pygame.time.delay(500)
                    bust_player_text = font.render('Player Busts', True, color)
                    screen.blit(bust_player_text, (80, 250))
                    pygame.display.update()
                    key = 'End Turns'

        match key:
            case 'Dealer Turn':

                # check blackjack
                dealer_value, dealer_bust = calculate.run(dealer_hand)

                if check_dealer_BJ:
                    screen.blit(dealer_hand[1].image, dealer_hand_position)
                    pygame.display.update()
                    pygame.time.delay(small_delay)
                    dealer_value_text = font.render(f'{dealer_value}', True, color)
                    screen.blit(dealer_value_text, dealer_value_position)
                    pygame.display.update()
                    pygame.time.delay(1000)

                    if dealer_value == 21:
                        print('dealer blackjack')
                        key = 'End Turns'
                    check_dealer_BJ = False

                if dealer_bust:
                    print('dealer bust')
                    key = 'End Turns'

                if dealer_value < 17:
                    dealer_value, bust, drawn = hit.run(dealer_hand, deck, 0)
                    pygame.time.delay(500)
                    dealer_value, dealer_bust = calculate.run(dealer_hand)
                    animate.run(screen, drawn, dealer_hit_position, deal_speed)
                    disp_value.run(screen, dealer_value, font, dealer_value_position, bg_img, color)
                    dealer_hit_position[0] += 40

                else:
                    key = 'End Turns'

        match key:
            case 'End Turns':
                # check player BJ
                if player_BJ and not dealer_BJ:
                    print('player blackjack')
                    pygame.time.delay(500)
                    balance = cashout.run(balance, bet, player_BJ, win)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    key = 'betting'

                # if dealer wins
                elif player_bust or dealer_value > player_value and not dealer_bust:
                    print('dealer wins')
                    pygame.time.delay(500)
                    balance = cashout.run(balance, bet, player_BJ, win)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    key = 'betting'

                # if player wins
                elif dealer_bust or player_value > dealer_value:
                    win = True
                    print('player wins')
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
                player_BJ = False
                dealer_BJ = False
                dealer_bust = False

    pygame.display.flip()
pygame.quit()
