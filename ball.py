from turtle import Turtle

STARTING_POSITION = (0, 0)
STARTING_SPEED = 0.1
SPEEDUP_RATE = 0.9


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(2, 2)
        self.color("white")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.x_move = 10
        self.y_move = 10
        self.speedup = STARTING_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.speedup *= SPEEDUP_RATE

    def hit(self):
        self.x_move *= -1
        self.speedup *= SPEEDUP_RATE

    def reset_position(self):
        self.goto(0, 0)
        self.speedup *= STARTING_SPEED
        self.hit()
