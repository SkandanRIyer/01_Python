from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.draw_midline()
        self.score_l = 0
        self.score_r = 0
        self.update()

    def draw_midline(self):
        self.setpos(0, 300)
        self.setheading(270)
        self.pencolor("white")
        self.pensize(width=10)
        for steps in range(0, 600, 20):
            self.forward(20)
            if self.isdown():
                self.penup()
            else:
                self.pendown()

    def update(self):
        self.clear()
        self.setposition(-100, 200)
        self.write(self.score_l, font=FONT, align=ALIGN)
        self.setposition(100, 200)
        self.write(self.score_r, font=FONT, align=ALIGN)

    def increment_rscore(self):
        self.score_r += 1
        self.update()

    def increment_lscore(self):
        self.score_l += 1
        self.update()