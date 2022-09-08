#!usr/bin/env python3

"""

"""
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
# Clicking ADD button will call this function.
def add_data():
    # Use get method to save the entry text into a variable.
    name_website = website_input.get()
    name_user = username_input.get()
    user_password = password_input.get()
    if len(name_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="incomplete information", message="some fields are not filled correctly")
    else:
        is_ok = messagebox.askyesno(title="Press OK to continue", message="Do you want to continue")
        if is_ok:
            # Append data to the file. If file doesn't exist then create a new file.
            # Following way of creating file is better it will close the file automatically.
            with open("data.txt", "a") as file:
                file.write(name_website + " | ")
                file.write(name_user + " | ")
                file.write(user_password + "\n")
            # Deleting text entry in tkinter using delete() method. Delete takes 2 parameter (start_of_index, end_of_index)
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

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

password_button = Button(text="Generate Password", command=generate_pass, font="Verdana 20 bold")
password_button.grid(row=4, column=2)

add_button = Button(text="Add", command=add_data, width=36, font="Verdana 20 bold")
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
