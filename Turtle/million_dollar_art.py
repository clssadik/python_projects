import random

import colorgram
from turtle import Turtle,Screen
turtle = Turtle()
screen = Screen()

screen.colormode(255)
turtle.penup()
turtle.goto(-225, -225)
turtle.pendown()

color = colorgram.extract("paint.jpg", 12)
rgb_colors = []
for i in color[1:]:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgb_colors.append((r,g,b))

turtle.speed("fastest")
def sag():
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.left(90)

def sol():
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.right(90)

def logic():
    for j in range(0,10):
        turtle.dot(20, random.choice(rgb_colors))
        if j < 9:
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()

for i in range(0,10):
    if turtle.heading() == 0.0:
        logic()
        sag()
    elif turtle.heading() == 180:
        logic()
        sol()


screen.exitonclick()