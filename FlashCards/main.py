from pydoc import text
from tkinter import *
import pandas
import random

from pandas.core.frame import com

data_file = pandas.read_csv("data/french_words.csv")
cards = data_file.to_dict(orient="records")
current_card = random.choice(cards)


def new_card_everytime():
    current_card = random.choice(cards)
    word(text=current_card["French"])

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0,bg=BACKGROUND_COLOR)
photo = PhotoImage(file=("images/card_front.png"))
canvas.create_image(400,263,image=photo)
canvas.grid(row=0,column=0,columnspan=2)

title = Label(text="Title",font=("Ariel",40,"italic"),fg="black",bg="white")
title.place(x=400,y=150,anchor="center")

word = Label(text=current_card["French"],font=("Ariel",60,"bold"),fg="black",bg="white")
word.place(x=400,y=263,anchor="center")

wrong_image = PhotoImage(file="images/wrong.png")
button1 = Button(image=wrong_image, highlightthickness=0,borderwidth=0,relief="flat",command=new_card_everytime)
button1.grid(row=1,column=0)

right_image = PhotoImage(file="images/right.png")
button2 = Button(image=right_image,highlightthickness=0,borderwidth=0,relief="flat",command=new_card_everytime)
button2.grid(row=1,column=1)

window.mainloop()

