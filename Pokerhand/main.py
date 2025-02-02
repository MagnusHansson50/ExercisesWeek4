import random

def slump_kort():
    varde = random.randint(2, 14)
    farg = random.randint(1, 4)
    if farg == 1:
        farg = "hjärter"
    elif farg == 2:
        farg = "ruter"
    elif farg == 3:
        farg = "klöver"
    elif farg == 4:
        farg = "spader"
    kort = [farg, varde]
    return kort

def nytt_kort(c):
    inte_unik = True
    kort = []
    while inte_unik:
        kort = slump_kort()
        if len(c) > 0:
            for item1 in c:
                if item1 != kort:
                    inte_unik = False
        else:
            inte_unik = False
    return kort

def jamfor_tva_kort(c1, c2):
    if c1[1] == c2[1]:
        return True
    else:
        return False

def poker_hand(cards):
    counter = 0
    i = 0
    while i < 5:
        item1 = cards[i]
        j = i + 1
        while j < 5:
            item2 = cards[j]
            if jamfor_tva_kort(item1, item2):
                counter += 1
            j += 1
        i += 1
    if counter == 1:
        print("Minst två kort är av samma valör")
    # elif counter == 2:
    #     print("Tre kort är av samma valör")
    # elif counter == 3:
    #     print("Fyra kort är av samma valör")

def pretty_print(l):
    length = len(l)
    if length > 0:
        i = 1
        for item in l:
            print(f" {item}", end = "")
            i += 1
        print()
    else:
        print("Listan är tom")

def get_a_new_hand():
    ny_hand = []
    for x in range(5):
        ny_hand.append(nytt_kort(ny_hand))
    return ny_hand

hand = get_a_new_hand()

#print(f"kort1: {kort1}, kort2: {kort2}. Har de samma valör: {jamfor_tva_kort(kort1, kort2)}")
pretty_print(hand[0])
pretty_print(hand[1])
pretty_print(hand[2])
pretty_print(hand[3])
pretty_print(hand[4])
print(f"kort1: {hand[0]}")
print(f"kort2: {hand[1]}")
print(f"kort3: {hand[2]}")
print(f"kort4: {hand[3]}")
print(f"kort5: {hand[4]}")
poker_hand(hand)
