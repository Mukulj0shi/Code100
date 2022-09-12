#!usr/bin/env python3

"""
Saving user name and password in a json format and retrievinng that data
using try except block to catch the exception
"""
from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    name_website = website_input.get()
    print(name_website)
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        website_name = data[name_website]
    except FileNotFoundError:
        messagebox.showinfo(title=name_website, message="file doesn't exist")
    except KeyError:
        messagebox.showinfo(title=name_website, message="this website is not in the database")
    else:
        user_name = data[name_website]["username"]
        pass_word = data[name_website]["password"]
        messagebox.showinfo(title=name_website, message=user_name)
    finally:
        # Deleting text entry in tkinter using delete() method. Delete takes 2 parameter (start_of_index, end_of_index)
        website_input.delete(0, 'end')
        password_input.delete(0, 'end')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for number1 in range(nr_letters)]
    password_list2 = [random.choice(symbols) for number in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for number in range(nr_numbers)]
    password_list = password_list1 + password_list2 + password_list3

    random.shuffle(password_list)
    password = "".join(password_list)
    # Adding automatically generated password in the input screen using insert method().
    # Input screen is filled with the information that we created.
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Clicking ADD button will call this function.
def add_data():
    # Use get method to save the entry text into a variable.
    name_website = website_input.get()
    name_user = username_input.get()
    user_password = password_input.get()
    add_data = {
        name_website:{
            "username": name_user,
            "password": user_password
        }
    }
    # Messagebox method is used to create warning or information screen while working with tkinter.
    if len(name_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="incomplete information", message="some fields are not filled correctly")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        # If file doesn't exist then create the file and serialize native data to JSON format
        except FileNotFoundError as error_mssg:
            with open("data.json", "w") as file:
                json.dump(add_data, file, indent=4)
                print(f"{error_mssg}, file created")
        else:
            data.update(add_data)
            with open("data.json", "w") as file:
                write_data = json.dump(data, file, indent=4)
                print(write_data)
        finally:
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
website_input = Entry(width=20, font="Verdana 20 bold")
website_input.focus()
website_input.grid(row=2, column=1)

username_input = Entry(width=35, font="Verdana 20 bold")
username_input.focus()
username_input.grid(row=3, column=1, columnspan=2)

password_input = Entry(width=20, font="Verdana 20 bold")
# Using focus() method will keep the cursor at the beginning of the input entry
password_input.focus()
password_input.grid(row=4, column=1)

# Create button
search_button = Button(text="Search", width=15, command=search, font="Verdana 20 bold")
search_button.grid(row=2, column=2)

password_button = Button(text="Generate Password", command=generate_pass, font="Verdana 20 bold")
password_button.grid(row=4, column=2)

add_button = Button(text="Add", command=add_data, width=36, font="Verdana 20 bold")
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()