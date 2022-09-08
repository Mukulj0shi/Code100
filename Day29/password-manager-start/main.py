#!usr/bin/env python3

"""

"""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Clicking ADD button will call this function.
def add_data():
    name_website = website_input.get()
    name_user = username_input.get()
    user_password = password_input.get()
    file = open("confidential.txt", "a")
    file.write(name_website + " | ")
    file.write(name_user + " | ")
    file.write(user_password + "\n")
    file.close()


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

# Create a window using tkinter
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Use Canvas from tkinter to upload image in the window.
canvas = Canvas(width=200, height=200)
fill_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=fill_image)
canvas.grid(row=1, column=1)

# Create label(text) in the window
website_label = Label(text="Website")
website_label.grid(row=2, column=0)

username_label = Label(text="Email/Username")
username_label.grid(row=3, column=0)

password_label = Label(text="Password")
password_label.grid(row=4, column=0)

# Get input from user using input
website_input = Entry(width=35, font="Verdana 20 bold")
website_input.focus()
website_input.grid(row=2, column=1, columnspan=2)

username_input = Entry(width=35, font="Verdana 20 bold")
username_input.focus()
username_input.grid(row=3, column=1, columnspan=2)

password_input = Entry(width=20, font="Verdana 20 bold")
password_input.focus()
password_input.grid(row=4, column=1)


# Create button

#password_button = Button(text="Generate Password", command=generate_pass, font="Verdana 20 bold")
#password_button.grid(row=4, column=2)

add_button = Button(text="Add", command=add_data, width=36, font="Verdana 20 bold")
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
