# displays balance
# position is hardcoded

def run(screen, balance, font, color):
    balance_text = font.render(f'BALANCE: {balance}', True, color)
    screen.blit(balance_text, (75, 475))
