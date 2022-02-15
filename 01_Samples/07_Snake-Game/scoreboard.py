from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.setpos(-10, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def increment(self):
        self.score += 1
        self.display_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.display_score()

    def game_end(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"Game over!! Final Score: {self.score}", align=ALIGN, font=FONT)