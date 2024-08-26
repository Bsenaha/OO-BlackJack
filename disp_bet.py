# displays bet
# position is hardcoded

def run(screen, bet, font, color):
    bet_text = font.render(f'{bet}', True, color)
    screen.blit(bet_text, (0, 60))
