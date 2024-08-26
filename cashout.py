# cashout/calculate new player balance

def run(balance, bet, player_BJ, win):
    # if player blackjack
    if player_BJ:
        balance += 3*bet
    # if player wins
    elif win:
        balance += 2*bet
    # if player doesn't lose, leave balance alone
    return balance
