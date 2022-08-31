from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    question = Question(items["text"], items["answer"])
    question_bank.append(question)
#print(question_bank)

question_obj = QuizBrain(question_bank)
while question_obj.still_has_questions():
    question_obj.next_question()

print("Congratulations you have completed the quiz")
print(f"You scored is {question_obj.score}/{len(question_obj.question_list)}")