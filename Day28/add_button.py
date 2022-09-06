from tkinter import *

tk = Tk()

# Create button

def starttimer():
    label3 = Label()
    label3.config(text=km)

button_start = Button(text="Start", command=starttimer, font="Verdana 20 bold")
button_start.grid(row=2, column=10)
button_start.config(padx=60, pady=10)

def resettimer():
    label3 = Label()
    label3.config(text=km)

button_reset = Button(text="Reset", command=resettimer, font="Verdana 20 bold")
button_reset.grid(row=2, column=30)
button_reset.config(padx=60, pady=10)





tk.mainloop()