import turtle
import turtle as t
import pandas

FONT = ('Arial', 8, 'normal')
ALIGN = "Center"

screen = t.Screen()
screen.title("U.S. States Game")
t_shape = "blank_states_img.gif"
screen.addshape(t_shape)
t.shape(t_shape)
pogo = t.Turtle()
pogo.penup()
pogo.hideturtle()

states_data = pandas.read_csv("50_states.csv")
initial = True
correct_guesses = []
states = states_data.state.to_list()

while len(correct_guesses) < 50:
    if initial:
        guess = screen.textinput("Guess the name of a state: ", "Enter a State's Name: ").title()
        initial = False
    else:
        guess = screen.textinput(f"{len(correct_guesses)}/50 states correct", "Enter a State's Name: ").title()

    if guess == "Exit":
        break

    if guess is not None and guess not in correct_guesses:
        if guess in states:
            state_info = states_data[states_data.state == guess]
            pogo.setposition(int(state_info.x), int(state_info.y))
            pogo.write(f"{guess}", align=ALIGN, font=FONT, move=False)
            correct_guesses.append(guess)

# states to learn
states_to_learn = [state for state in states if state not in correct_guesses]
print(states_to_learn)
final = pandas.DataFrame(states_to_learn)
final.to_csv("states_to_learn.csv")



screen.exitonclick()
