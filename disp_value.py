# displays value at specified position (for hand values)

import pygame


def run(screen, value, font, position, bg_img, color):
    if value > 21:
        value_text = font.render(f'{value}', True, color)
        screen.blit(bg_img, position, (position[0], position[1], 30, 30))
        screen.blit(value_text, position)
        pygame.display.update()

    if value == 21:
        value_text = font.render(f'{value}', True, color)
        screen.blit(bg_img, position, (position[0], position[1], 30, 30))
        screen.blit(value_text, position)
        pygame.display.update()

    else:
        value_text = font.render(f'{value}', True, color)
        screen.blit(bg_img, position, (position[0], position[1], 30, 30))
        screen.blit(value_text, position)
        pygame.display.update()
