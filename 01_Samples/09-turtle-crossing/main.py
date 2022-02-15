import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

REFRESH_RATE = 0.5

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)


car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
sleep_time = 0.0
while game_is_on:
    if scoreboard.level > 0:
        sleep_time *= 0.99
    else:
        sleep_time = REFRESH_RATE
    time.sleep(sleep_time)
    screen.update()

    # create and move the cars
    car_manager.create_car(scoreboard.level)
    car_manager.move_cars()

    # detect if player hits a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.end_game()
            game_is_on = False

    if player.at_finish():
        scoreboard.level_up()
        car_manager.next_level()
        player.restart()

    car_manager.pop_cars()

screen.exitonclick()