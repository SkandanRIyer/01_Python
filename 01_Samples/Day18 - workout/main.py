import random
import turtle
from turtle import Turtle, Screen
from random import choice

pogo = Turtle()
pogo.shape("square")
# pogo.color("white")
# for _ in range(4):
#     pogo.forward(100)
#     pogo.right(90)
# for _ in range(15):
#     pogo.forward(5)
#     pogo.penup()
#     pogo.forward(5)
#     pogo.pendown()

# turtle_colors = ["dark green", "green", "blue", "yellow", "orange", "brown", "purple"]

# for num in range(3, 11):
#     pogo.pencolor(choice(turtle_colors))
#     for _ in range(num):
#         pogo.forward(100)
#         pogo.right(360 / num)

direction = [0, 90, 180, 270]
# pogo.pensize(10)
pogo.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# while True:
#     pogo.pencolor(random_color())
#     pogo.forward(50)
#     pogo.setheading(choice(direction))
for num in range(0, int(360 / 4)):
    pogo.setheading(pogo.heading() + 4)
    pogo.pencolor(random_color())
    pogo.circle(100)

screen = Screen()
screen.colormode(255)
# screen.bgcolor("black")
screen.exitonclick()
