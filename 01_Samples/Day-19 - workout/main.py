from turtle import Turtle, Screen

pogo = Turtle()
screen = Screen()


def go_forward():
    pogo.forward(20)


def go_backward():
    pogo.backward(20)


def go_clockwise():
    pogo.right(10)


def go_counter_clockwise():
    pogo.left(10)


def clear():
    pogo.clear()
    pogo.reset()


screen.listen()
screen.onkey(fun=go_forward, key="w")
screen.onkey(fun=go_backward, key="s")
screen.onkey(fun=go_clockwise, key="d")
screen.onkey(fun=go_counter_clockwise, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
