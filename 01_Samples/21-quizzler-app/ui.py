from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Some Questions", fill=THEME_COLOR,
                                                     font=(FONT_NAME, 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label()
        self.score_label.config(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        photo_t = PhotoImage(file="./images/true.png")
        self.b_true = Button(image=photo_t, command=self.check_true, highlightthickness=0)
        self.b_true.grid(column=0, row=2)

        photo_f = PhotoImage(file="./images/false.png")
        self.b_false = Button(image=photo_f, command=self.check_false, highlightthickness=0)
        self.b_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.update_score()
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="Game Over!!!")
            self.b_false.config(state="disabled")
            self.b_true.config(state="disabled")

    def update_score(self) -> None:
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def check_true(self) -> None:
        self.show_result(self.quiz.check_answer("true"))

    def check_false(self) -> None:
        self.show_result(self.quiz.check_answer("false"))

    def show_result(self, get_result) -> None:
        if get_result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)




