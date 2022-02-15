import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self, level):
        num_cars = level * 10 + 20
        if len(self.all_cars) < num_cars:
            car = Turtle(shape="square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            sety = random.randint(-250, 250)
            car.setpos(300, sety)
            car.setheading(180)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.carspeed)

    def next_level(self):
        self.carspeed += MOVE_INCREMENT

    def pop_cars(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                self.all_cars.remove(car)
