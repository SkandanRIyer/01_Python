from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.setx = 10
        self.sety = 10
        self.ball_speed = 0.1

    def move(self):
        setx = self.xcor() + self.setx
        sety = self.ycor() + self.sety
        self.setpos(setx, sety)

    def hits_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True

    def bounce_y(self):
        self.sety *= -1

    def bounce_x(self):
        self.setx *= -1

    def reposition(self):
        self.setpos(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        self.ball_speed *= 0.95
