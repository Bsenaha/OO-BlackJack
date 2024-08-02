# Create Card Class
import pygame


# card class
# assign image and card's value
class Card(pygame.sprite.Sprite):

    def __init__(self, suit, img_ID, val, speed=20):
        # inputs:
        pygame.sprite.Sprite.__init__(self)
        super(Card, self).__init__()
        self.image = pygame.image.load(f'game_images/cards/{suit}/{img_ID}')
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.value = val
        self.speed = speed
        self.rect = self.image.get_rect()
