from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]

    def create_snake(self):
        setx = 0
        for _ in range(3):
            self.add_piece((setx, 0))
            setx -= 20

    def add_piece(self, position):
        piece = Turtle(shape="square")
        piece.color("white")
        piece.speed("fastest")
        piece.penup()
        piece.setpos(position)
        self.pieces.append(piece)

    def extend_snake(self):
        self.add_piece(self.pieces[-1].position())

    def move(self):
        for piece_num in range(len(self.pieces) - 1, 0, -1):
            setx = self.pieces[piece_num - 1].xcor()
            sety = self.pieces[piece_num - 1].ycor()
            self.pieces[piece_num].setpos(setx, sety)
        self.pieces[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for piece in self.pieces:
            piece.hideturtle()
        self.pieces.clear()
        self.create_snake()
        self.head = self.pieces[0]
