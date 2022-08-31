from turtle import Turtle, Screen

style = ('Courier', 20, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 360)
        self.color('white')
        self.i = 0
        self.write('Score:' + str(self.i), font=style, align='center')
        self.hideturtle()

    def new_score(self):
        self.clear()
        self.i += 1
        self.write('Score:' + str(self.i), font=style, align='center')

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.color('white')
        self.write('Score:' + str(self.i), font=style, align='center')
