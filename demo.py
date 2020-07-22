import random

ladders = {12: 25, 2: 16, 5: 20, 19: 31}
snakes = {35: 23, 28: 21, 22: 15, 14: 11}
players = {1: 0, 2: 0, 3: 0}


def dice():
    return random.randint(1, 6)


