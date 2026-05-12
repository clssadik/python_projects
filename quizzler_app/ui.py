from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,width=350,height=500)
        self.score = 0
        self.text_lbl = Label(text=f"Score: {score}")




        self.window.mainloop()
