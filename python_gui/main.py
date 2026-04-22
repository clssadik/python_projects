from tkinter import *

window = Tk()
window.title("Python GUI")
window.minsize(500, 300)

my_label = Label(text="Hello World", font=("Times", 25, "italic"))
my_label.pack()

my_label["text"] = "New Text"

# Buton yaratma

def button_clicked():
    input_data = data.get()
    my_label.config(text=input_data)

button = Button(text="Click me", command=button_clicked, background="blue")
button.pack()

# Data girişi
data = Entry()
data.pack()











window.mainloop()