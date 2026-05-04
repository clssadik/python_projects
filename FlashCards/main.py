from tkinter import *
from turtle import xcor

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0,bg=BACKGROUND_COLOR)
photo = PhotoImage(file=("images/card_front.png"))
canvas.create_image(400,263,image=photo)
canvas.grid(row=0,column=1)

title_text = Label(text="Title",font=("Ariel",40,"italic"),fg="black",bg="white")
title_text.place(x=400,y=150)




window.mainloop()

