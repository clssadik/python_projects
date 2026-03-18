from turtle import Turtle,Screen
import random
turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen","red","blue","orange"]

which_way = ["east","north","south","west"]


turtle.shape("arrow")
turtle.pensize(10)
turtle.speed("fastest")

for i in range(300):
    turtle.forward(30)
    choice = random.choice(which_way)
    if choice == "east":
        turtle.setheading(0)
    elif choice == "north":
        turtle.setheading(90)
    elif choice == "south":
        turtle.setheading(270)
    elif choice == "west":
        turtle.setheading(180)
    turtle.color(random.choice(colours))


screen = Screen()
screen.exitonclick()