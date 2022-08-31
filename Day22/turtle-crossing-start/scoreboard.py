from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.new_level_no = 1
        self.hideturtle()
        self.penup()
        self.goto(-240, 250)
        self.color('black')
        self.write("Level: " + str(self.new_level_no), font=FONT, align='center')

    def new_score(self):
        self.clear()
        self.new_level_no += 1
        self.write("Level: " + str(self.new_level_no), font=FONT, align='center')


