class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question_appear = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{question_appear.text} (True/False):")
        self.check_answer(question_appear.answer, user_answer)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print(f"{self.score}/{self.question_number}")
            print("answer is correct")
        else:
            print(f"{self.score}/{self.question_number}")
            print("answer is incorrect")








