import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create the initial snake
snake = Snake()
screen.listen()
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # keep the snake moving
    snake.move()

screen.exitonclick()