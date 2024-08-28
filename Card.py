# Create Card Class
import pygame


# card class
# assign image and card's value
class Card(pygame.sprite.Sprite):

    def __init__(self, suit, img_ID, val):
        # inputs:
        pygame.sprite.Sprite.__init__(self)
        super(Card, self).__init__()
        if suit == 'card back':
            self.image = pygame.image.load('game_images/cards/card_back.png')
            self.image = pygame.transform.scale(self.image, (71, 81))
        else:
            self.image = pygame.image.load(f'game_images/cards/{suit}/{img_ID}')
            self.image = pygame.transform.scale(self.image, (70, 80))
            self.value = val
            self.rect = self.image.get_rect()
