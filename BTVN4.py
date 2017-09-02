from turtle import *

shape("turtle")

def draw_star(x,y,length):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

color('red')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(50, 101)
    draw_star(x, y, length)

mainloop()