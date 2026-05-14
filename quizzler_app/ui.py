from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        # Set window title and background color
        
        self.score = 0
        self.text_lbl = Label(text=f"Score: {self.score}",fg="white", bg=THEME_COLOR)
        self.text_lbl.grid(row=0,column=1)
        # Display current score label

        self.canvas = Canvas(width=300,height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        self.canvas.create_text(150, 125, text="question", fill=THEME_COLOR, width=280,font=("Arial",20,"italic"))
        # Canvas for displaying quiz questions
        
        self.right_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")
        
        self.button_right = Button(image=self.right_image,highlightthickness=0)
        self.button_right.grid(row=2,column=0)

        self.button_wrong = Button(image=self.wrong_image,highlightthickness=0)
        self.button_wrong.grid(row=2,column=1)
        # True and False answer buttons

        
        
        
        
        
        
        self.window.mainloop()
        # Start the Tkinter event loop
