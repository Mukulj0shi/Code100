# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')


# Creating a clock in the screen
def clock_timer():
    time = strftime('%H:%M:%S %p')
    canvas.create_text(100, 10, text=time, fill="BLACK", font=("", 35, "bold"))
    time_label = Label()
    time_label.grid(row=5, column=10)
    time_label.after(1000, clock_timer)


clock_timer()

mainloop()