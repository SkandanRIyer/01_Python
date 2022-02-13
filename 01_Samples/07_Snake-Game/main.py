import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create the initial snake
snake = Snake()
food = Food()
score = ScoreBoard()
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

    # detect collision with food
    if snake.head.distance(food) < 15:
        score.increment()
        snake.extend_snake()
        food.set_food()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or \
            snake.head.ycor() < -280:
        score.game_end()
        game_is_on = False

    # detect collision with any piece
    for piece in snake.pieces[1:]:
        if snake.head.distance(piece) < 10:
            score.game_end()
            game_is_on = False

screen.exitonclick()
