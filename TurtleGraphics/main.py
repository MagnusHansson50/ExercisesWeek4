import turtle as t

def kvadrat(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def move_next(length):
    t.penup()
    t.forward(length)
    t.pendown()

def cirkel(steg, storlek, vinkel):
    for x in range(steg):
        t.forward(storlek)
        t.right(vinkel)

# # Upprepa 3 gånger
# for x in range(3):
#     t.forward(100)
#     t.left(120)
#
# t.penup()
# t.forward(200)
# t.pendown()
# t.dot(10, "red")
# t.color("blue")
# t.forward(50)

# for x in range(5):
#     kvadrat(100)
#     move_next(150)

cirkel(72, 20, 5)

t.mainloop()