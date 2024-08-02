import pygame
from pygame.locals import *
import deck_init


deck = deck_init.run()
print(deck)

# initialize
pygame.init()

# Create Screen & title
screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption("BlackJack")

image = pygame.image.load("game_images/cards/clubs/card_clubs_02.png")
position = (0, 0)

gameOn = True
while gameOn:
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                gameOn = False

        elif event.type == QUIT:
            gameOn = False
    screen.blit(image, position)

    pygame.display.flip()
