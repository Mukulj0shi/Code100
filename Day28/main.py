#!usr/bin/env python3


"""
https://pythonguides.com/python-tkinter-image/
"""

from tkinter import *
from time import strftime

MAROON = "#31112C"
start_clock = True

tk = Tk()

# Create screen
tk.title("POMODORO")
tk.minsize(width=1000, height=500)

#create canvas class and assign and height and width to canvas
# over the canvas image will be pasted
canvas = Canvas(width=200, height=224, bg=MAROON, highlightthickness=0)
img = PhotoImage(file="image2.png")
canvas.create_image(100, 112, image=img)
#canvas.create_text(100, 10, text="Test Text", fill="BLACK", font=("",35, "bold"))
canvas.grid(row=10, column=10)


# Creating a clock in the screen
def clock_timer():
    hour = 00
    minute = 00
    while start_clock:
        canvas.create_text(100, 10, text=str(hour) + ":" + str(minute), fill="BLACK", font=("",35, "bold"))
        minute += 1
        if minute == 60:
            hour += 1


clock_timer()

tk.mainloop()