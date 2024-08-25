# Betting process before dealing each hand

from button import Button
import pygame


def run(balance, screen, event, mouse, position, ADD_bet):
    # create chip "buttons"
    ten = Button('ten', screen, position[0])
    tf = Button('tf', screen, position[1])
    deal = Button('deal', screen, position[3])

    # overlay chip
    ten.run_button(screen, event, mouse, position[0], ADD_bet[0])
    tf.run_button(screen, event, mouse, position[1], ADD_bet[1])
    deal.run_button(screen, event, mouse, position[3], ADD_bet[3])


