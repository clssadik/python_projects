from turtle import Turtle,Screen
import random
turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(3,10):
    angle = 360/i
    turtle.color(random.choice(colours))
    for j in range(i):
        turtle.right(angle)
        turtle.forward(100)

screen = Screen()
screen.exitonclick()