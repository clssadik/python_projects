import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []
missing_states = all_state.copy()


while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",prompt = "What's another state's name? ").title()
    if answer_state == "Exit":
        break
    if answer_state in all_state:
        missing_states.remove(answer_state)
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

missing_states123 = pandas.DataFrame(missing_states,columns = ["States"])
missing_states123.to_csv("missing_states.csv")


