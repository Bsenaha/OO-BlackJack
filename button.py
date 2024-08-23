# creates button for player actions (used for betting and card actions)
import pygame


class Button:
    def __init__(self, button_name, screen):
        # define button colors
        # white color
        self.color = (255, 255, 255)
        # light shade of the button
        self.color_light = (170, 170, 170)
        # dark shade of the button
        self.color_dark = (100, 100, 100)

        # defining button size
        self.width = 80
        self.height = 100

        # defining a font
        self.font = pygame.font.SysFont('segoeuisymbol', 35)

        # rendering text
        self.text = self.font.render(f'{button_name}', True, self.color)

        pygame.draw.rect(screen, self.color_dark, [self.width / 2, self.height / 2, 140, 40])

        # superimposing the text onto our button

        screen.blit(self.text, (self.width / 2 + 50, self.height / 2))
        pygame.display.update()

    # finds if button is clicked
    # returns True if clicked
    def isClicked(self, screen):
        isClicked = False
        for event in pygame.event.get():
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # stores the (x,y) coordinates into
                # the variable as a tuple
                mouse = pygame.mouse.get_pos()

                # if the mouse is clicked on the
                # button the hit event triggered
                if self.width / 2 <= mouse[0] <= self.width / 2 + 140 and self.height / 2 <= mouse[
                    1] <= self.height / 2 + 40:
                    isClicked = True
                    return isClicked

                # if mouse is hovered on a button it
                # changes to lighter shade
                if self.width / 2 <= mouse[0] <= self.width / 2 + 140 and self.height / 2 <= mouse[
                    1] <= self.height / 2 + 40:
                    pygame.draw.rect(screen, self.color_light, [self.width / 2, self.height / 2, 140, 40])

            # updates the frames of the game
            pygame.display.update()
            return isClicked
