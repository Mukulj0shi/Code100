from turtle import Turtle, Screen
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = Scoreboard()

    def create_turtle(self):
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(1, 1)
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.clear()
        self.create_turtle()
        self.score.new_score()

    def crossed(self):
        if self.ycor() == FINISH_LINE_Y:
            self.reset_turtle()
            return True

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT, align='center')



