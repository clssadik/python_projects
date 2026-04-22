from tkinter import *

window = Tk()
window.title("Python GUI")
window.minsize(500, 300)

my_label = Label(text="Hello World", font=("Times", 25, "italic"))
my_label.pack()

my_label["text"] = "New Text"

# Buton yaratma

def button_clicked():
    print("Button clicked")

button = Button(text="Click me", command=button_clicked)
button.pack()











window.mainloop()