import random


def new_card():
    card = random.randint(1, 13)
    return card

def dator_new_card(x, y,  c):
    if x < 15 or x < y:
        x += new_card()
    while c:
        if x < 15 or x < y:
            x += new_card()
        c = False
    return x