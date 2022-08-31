from turtle import Turtle, Screen

turtle_object = Turtle()
screen_object = Screen()

for i in range(0, 11):
    turtle_object.forward(10)
    turtle_object.penup()
    turtle_object.forward(10)
    turtle_object.pendown()

screen_object.exitonclick()


