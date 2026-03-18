import turtle as t
from turtle import Turtle,Screen
import random
turtle = Turtle()
t.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen","red","blue","orange"]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

turtle.shape("arrow")
turtle.pensize(1)
turtle.speed("fastest")

for i in range(120):
    turtle.circle(200)
    turtle.left(3)
    turtle.color(random.choice(colours))


screen = Screen()
screen.exitonclick()