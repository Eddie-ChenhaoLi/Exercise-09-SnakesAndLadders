import random

ladders = {12: 25, 2: 16, 5: 20, 19: 31}
snakes = {35: 23, 28: 21, 22: 15, 14: 11}
players = {1: 0, 2: 0, 3: 0}


def dice():
    return random.randint(1, 6)

def move_ladders(position):
    for bottom, top in ladders.items():
        if position == bottom:
            return top
    return position

def move_snakes(position):
    for head, tail in snakes.items():
        if position == head:
            return tail
    return position

def move(position, i):
    position += i
    return position

def win(position):
    if position >= 36:
        return 1
    else:
        return 0


def start():
    while (True):
        for player, position in players.items():
            i = dice()
            position = move(position, i)
            position = move_ladders(position)
            position = move_snakes(position)
            players[player] = position
            print('{} now is in {}'.format(player, position))
            if win(position) == 1:
                print('The winner is {}'.format(player))
                return
        print('================')


start()
