from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.setpos(-10, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increment(self):
        self.score += 1
        self.display_score()

    def game_end(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"Game over!! Final Score: {self.score}", align=ALIGN, font=FONT)