# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
pogo = Turtle()


setx = -300
sety = -200
pogo.penup()
for _ in range (10):
    pogo.setpos(setx, sety)
    for _ in range(10):
        pogo.dot(35, random.choice(color_list))
        pogo.forward(50)
    sety += 50

screen = Screen()
screen.exitonclick()
