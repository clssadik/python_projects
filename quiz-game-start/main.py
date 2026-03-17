from data import question_data
from question_model import Question

question_bank = []
for letter in question_data:
    question_text = letter["text"]
    question_answer = letter["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)