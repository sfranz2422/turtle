from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)
        print("move right")

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)
        print("move left")

    def return_to_start(self):
        self.goto(STARTING_POSITION)
