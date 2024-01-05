from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
# for i in question_data:
#     choice = []
#     for keys in i:
#         choice.append(i[keys])
#     question_bank.append(Question(choice[0], choice[1]))
# print(question_bank)
# print(question_bank[1].text)
# print(question_bank[1].answer)
