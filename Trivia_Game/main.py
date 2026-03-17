from data import question_data,another_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for letter in another_data:
    question_text = letter["question"]
    question_answer = letter["correct_answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
