from turtle import Turtle, Screen

turtle_obj = Turtle()
screen_obj = Screen()
default_position = turtle_obj.heading()

def move_fwd():
    turtle_obj.forward(10)


def move_back():
    turtle_obj.backward(10)


def move_anticlockwise():
    turtle_obj.right(-10)


def move_clockwise():
    turtle_obj.left(-10)


def clear_screen():
    turtle_obj.clear()
    turtle_obj.penup()
    turtle_obj.hideturtle()
    turtle_obj.setpos(0, 0)
    turtle_obj.setheading(default_position)
    turtle_obj.pendown()
    turtle_obj.showturtle()


screen_obj.listen()
screen_obj.onkey(fun=move_fwd, key="w")
screen_obj.onkey(fun=move_back, key="s")
screen_obj.onkey(fun=move_anticlockwise, key="a")
screen_obj.onkey(fun=move_clockwise, key="d")
screen_obj.onkey(fun=clear_screen, key="c")

screen_obj.exitonclick()
