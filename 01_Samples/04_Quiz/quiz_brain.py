class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer == c_answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("That's not correct!!")
        print(f"The correct answer is: {c_answer}.\nYour current score is {self.score}/ {self.question_number} \n")

