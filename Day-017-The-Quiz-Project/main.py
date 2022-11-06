from question_model import Question
# from data import question_data
from data_opentdb import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.user_score}/{quiz.question_number}")