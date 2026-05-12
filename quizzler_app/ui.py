from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.geometry("350x500")
        
        self.score = 0
        self.text_lbl = Label(text=f"Score: {self.score}",fg="white", bg=THEME_COLOR)
        self.text_lbl.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1,column=0, columnspan=2, padx=20, pady=20)



        self.window.mainloop()
