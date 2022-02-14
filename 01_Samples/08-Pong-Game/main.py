import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="Right")
screen.onkey(fun=paddle_l.down, key="Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)

    # move the ball
    ball.move()

    # bounce the ball if its hits the wall
    if ball.hits_wall():
        ball.bounce_y()

    # detect whether the ball hits the paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or \
       (ball.distance(paddle_l) < 50 and ball.xcor() > -320):
        ball.bounce_x()
        ball.increase_speed()

    # detect when paddle_r misses
    if ball.xcor() > 380:
        scoreboard.increment_lscore()
        ball.reposition()

    # detect when paddle_l misses
    if ball.xcor() < -380:
        scoreboard.increment_rscore()
        ball.reposition()

screen.exitonclick()
