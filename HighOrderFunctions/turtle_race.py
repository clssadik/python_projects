import random
from turtle import Screen, Turtle

turtles = []
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def add_turtle():
    y_eks = -100
    for i in range(0, 6):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(x=-230, y=y_eks)
        y_eks += 41


add_turtle()

flag = True

if choice is None:
    flag = False

while flag:
    for i in range(0, 6):
        if turtles[i].xcor() > 230:
            flag = False
            winner_1 = turtles[i].pencolor()

            if winner_1 == choice:
                print(f"You win! The winner is: {winner_1}")
            else:
                print(f"You lose! The winner is: {winner_1}")

            break

        step_1 = random.randint(0, 10)
        turtles[i].forward(step_1)

screen.exitonclick()