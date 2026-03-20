# from turtle import Turtle,Screen
#
# turtle=Turtle()
# screen=Screen()
#
# def move_forwards():
#     turtle.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()
#

from turtle import Turtle,Screen

turtle=Turtle()
screen=Screen()

def move_forwards():
    turtle.forward(10)
def move_backwards():
    turtle.backward(10)
def clockwise():
    turtle.right(90)
def counterclockwise():
    turtle.left(90)

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(counterclockwise,"a")
screen.onkey(clockwise,"d")
screen.exitonclick()
