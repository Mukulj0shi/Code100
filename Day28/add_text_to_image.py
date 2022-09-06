#!usr/bin/env python3

"""
This programs uses canvas class to use image and to write a text in that image.
"""
from tkinter import *
MAROON = "#31112C"

tk = Tk()
tk.title("Add text to image")
tk.config(padx=50, pady=20, bg=MAROON)

#create canvas class and assign and height and width to canvas
# over the canvas image will be pasted
canvas = Canvas(width=200, height=224, bg=MAROON, highlightthickness=0)
img = PhotoImage(file="image2.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(100, 10, text="Test Text", fill="BLACK", font=("",35, "bold"))
canvas.grid()

tk.mainloop()