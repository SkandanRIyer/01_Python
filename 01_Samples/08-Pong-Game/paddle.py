from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

    def up(self):
        sety = self.ycor() + 20
        self.setpos(self.xcor(), sety)

    def down(self):
        sety = self.ycor() - 20
        self.setpos(self.xcor(), sety)
