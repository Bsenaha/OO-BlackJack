# creates button for player actions (used for betting and card actions)
import pygame


class Button:
    def __init__(self, button_name, screen, position):
        # define button colors
        # white color
        self.color = (255, 255, 255)
        # light shade of the button
        self.color_light = (170, 170, 170)
        # dark shade of the button
        self.color_dark = (100, 100, 100)

        # defining button size
        self.width = 75
        self.height = 25

        # defining a font
        self.font = pygame.font.Font('Emulogic-zrEw.ttf', 13)

        # rendering text
        self.text = self.font.render(f'{button_name}', True, self.color)

        pygame.draw.rect(screen, self.color_dark, pygame.Rect(position[0], position[1], self.width, self.height))

        # superimposing the text onto our button
        screen.blit(self.text, (position[0] + 20, position[1]))
        pygame.display.update()

    def run_button(self, screen, event, mouse, position, event_add):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # CHECK HIT
            # if the mouse is clicked on the
            # button the hit event triggered
            if position[0] <= mouse[0] <= position[0] + self.width and position[
                1] \
                    <= mouse[1] <= position[1] + self.height:
                pygame.event.post(event_add)

        # if mouse is hovered on a button it
        # changes to lighter shade
        if position[0] <= mouse[0] <= position[0] + self.width and position[1] \
                <= mouse[1] <= position[1] + self.height:
            pygame.draw.rect(screen, self.color_light,
                             pygame.Rect(position[0], position[1], self.width,
                                         self.height))
            screen.blit(self.text, (position[0] + 20, position[1]))

        # updates the frames of the game
        pygame.display.update()
