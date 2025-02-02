def greeting(s):
    print(f"{s} är en fena på programmering!!!")

def eko(s, x):
    i = 0
    while i < x:
        print(f"{s}", end="")
        i += 1
    print()

def pretty_print(l):
    length = len(l)
    if length > 0:
        print(f"Listan har {length} element:")
        i = 1
        for item in l:
            print(f"{i}. {item}")
            i += 1
    else:
        print("Listan är tom")

