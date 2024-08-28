# animates drawn card to specified position
import pygame
import math


def run(screen, card, position, time):
    # define off-screen position for cards to fly in from
    current = [0, 0]
    screen_copy = screen.copy()

    for i in range(1, time):
        current[0] = ((position[0] - 20) * (i/time) ** .6) + 20
        current[1] = ((position[1] + 80) * (i/time) ** .6) - 80

        if round(current[0]) != position[0]:
            screen.blit(screen_copy, current, (current[0], current[1], 70, 80))

        screen.blit(card.image, current)
        pygame.display.update()
