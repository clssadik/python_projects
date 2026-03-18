from turtle import Turtle,Screen

turtle = Turtle()
turtle.shape("arrow")
turtle.color("orange")
turtle.speed(1)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)


screen = Screen()
screen.exitonclick()