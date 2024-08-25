# displays balance

def run(screen, balance, font, color):
    balance_text = font.render(f'{balance}', True, color)
    screen.blit(balance_text, (0, 0))