from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data_file = pandas.read_csv("data/french_words.csv")
cards = data_file.to_dict(orient="records")
current_card = random.choice(cards)

def reset_frontt():
    global current_card
    current_card = random.choice(cards)
    canvas.itemconfig(title_id,text="French",fill="black")
    canvas.itemconfig(word_id, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image,image=front)
    window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(word_id, text=current_card["English"], fill="white")
    canvas.itemconfig(title_id, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=back)


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
window.after(3000,flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0,bg=BACKGROUND_COLOR)
front = PhotoImage(file=("images/card_front.png"))
back = PhotoImage(file=("images/card_back.png"))
canvas_image = canvas.create_image(400,263,image=front)
canvas.grid(row=0,column=0,columnspan=2)

title_id = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
word_id = canvas.create_text(400, 263, text=current_card["French"], font=("Ariel", 60, "bold"), fill="black")

wrong_image = PhotoImage(file="images/wrong.png")
button1 = Button(image=wrong_image, highlightthickness=0,borderwidth=0,relief="flat",command=reset_front)
button1.grid(row=1,column=0)

right_image = PhotoImage(file="images/right.png")
button2 = Button(image=right_image,highlightthickness=0,borderwidth=0,relief="flat",command=reset_front)
button2.grid(row=1,column=1)

window.mainloop()

