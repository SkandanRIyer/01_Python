from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.set_food()

    def set_food(self):
        setx = randint(-280, 280)
        sety = randint(-280, 280)
        self.setpos(setx, sety)
