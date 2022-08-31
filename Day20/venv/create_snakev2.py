#!/usr/bin/env python

"""
# This is snake class.
# Create snake body by calling the Snake() class
# Move snake by calling snake_move() method.
"""

from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0),
                      (-40, 0)]  # Constant are defined at the top of the program in capital letters and snake case.
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.turt_obj_list = []  # Here we are defining the attributes related to snake creation.
        self.create_snake()
        self.head = self.turt_obj_list[0]
        self.tail = self.turt_obj_list[-1]
        self.position = (0.00, 0.00)

    # Define snake body
    def create_snake(self):
        for cord in STARTING_POSITIONS:
            self.snake_segment(cord)

    def snake_segment(self, position):
        turtle_obj1 = Turtle()  # This will create 3 turtle objects.
        # Specifying object outside loop will create only single object.
        turtle_obj1.shape("square")
        turtle_obj1.color("white")
        turtle_obj1.penup()
        turtle_obj1.goto(position)
        self.turt_obj_list.append(turtle_obj1)  # Calling attributes in methods using self.attribute_name.

    def addtail(self):
        self.snake_segment(self.turt_obj_list[-1].position())

    def move_snake(self):
        for items in range((len(self.turt_obj_list) - 1), 0, -1):
            x_cord = self.turt_obj_list[items - 1].xcor()  # Last item moves to second last item position
            y_cord = self.turt_obj_list[items - 2].ycor()
            self.turt_obj_list[items].goto(x_cord, y_cord)
        self.head.forward(MOVE_DISTANCE)  # Calling attributes in methods using self.attribute_name.

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def endgame(self):
        # print(self.head.position()[0])
        if self.head.position()[0] <= -400 or self.head.position()[0] >= 400 or self.head.position()[1] <= -400 or \
                self.head.position()[1] >= 340:
            return True

    # create_snake()
    # move_snake()
    # screen_obj.exitonclick()
