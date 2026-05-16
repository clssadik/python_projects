from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        # Set window title and background color
        
        self.score_screen = 0
        self.text_lbl = Label(text=f"Score: {self.score_screen}",fg="white", bg=THEME_COLOR)
        self.text_lbl.grid(row=0,column=1)
        # Display current score label

        self.canvas = Canvas(width=300,height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="question", fill=THEME_COLOR, width=280, font=("Arial",20,"italic"))
        
        self.right_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")

        self.get_next_question()

        self.button_right = Button(image=self.right_image,highlightthickness=0,command=self.right_answer)
        self.button_right.grid(row=2,column=0)

        self.button_wrong = Button(image=self.wrong_image,highlightthickness=0,command=self.wrong_answer)
        self.button_wrong.grid(row=2,column=1)

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.text_lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

    def right_answer(self):
        self.give_feedback(self.quiz.check_answer("True")) 
        
    
    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False")) 

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000,self.get_next_question)