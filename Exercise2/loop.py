def loop():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == 5:
            break
    print(y)
