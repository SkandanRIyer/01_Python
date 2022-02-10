from turtle import Turtle, Screen
from random import randint

game_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "grey"]
guess = screen.textinput(title="Select your Winner", prompt="Which turtle will win the race? Enter a color: ")

# create the turtles
sety = -160
setx = -240
turtles =[]

for num in range(7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[num])
    # Move the turtles to the starting position
    tim.setpos(setx, sety)
    turtles.append(tim)
    sety += 50

if guess:
    game_on = True

winner = ""
while game_on:
    for tim in turtles:
        steps = randint(0, 15)
        tim.forward(steps)
        if tim.xcor() > 240:
            winner = tim.pencolor()
            game_on = False
            break

if winner == guess:
    print(f"You Won!!!! Your {winner} turtle won the race!!!👌👌")
else:
    print(f"You lost. The winner is {winner}!!!😒😒😒")
screen.exitonclick()