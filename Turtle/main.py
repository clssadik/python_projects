# from turtle import Turtle,Screen
#
# turtle = Turtle()
# turtle.shape("arrow")
# turtle.color("orange")
# turtle.speed(1)
#
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)
#
#
# screen = Screen()
# screen.exitonclick()

from turtle import Turtle,Screen

turtle = Turtle()
turtle.shape("arrow")
turtle.color("orange")
turtle.speed(1)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()