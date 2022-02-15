from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(-260, 260)
        self.level = 0
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def end_game(self):
        self.clear()
        self.setposition(-40,0)
        self.write("GAME OVER", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()


