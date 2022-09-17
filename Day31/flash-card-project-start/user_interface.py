#!usr/bin/env python3
"""
This program creates flash card for learning french to english translation.
"""
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import time


FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"
timer = None
select_card = {}
try:
    read_words = pd.read_csv("data/word_to_learn.csv")
    # It creates a list of dictionary items from DataFrame with 2 items in each list.
except FileNotFoundError:
    read_words = pd.read_csv("data/french_words.csv")
finally:
    word_dict = read_words.to_dict("records")


#----------------------------------Flip Card-------------------------------------------#
# Creates a english card after 300 second
def flip_card():
    canvas.itemconfig(card_cover, image=back_image)
    canvas.itemconfig(title_text, text="English")
    english_word = select_card["English"]
    #print(f"English: {english_word}")
    canvas.itemconfig(word_text, text=english_word)


#----------------------------------Generate words--------------------------------------#
# French word appear on flash card when button is pressed.
# window.after will call flip.card() function after 300 seconds. As a result card changes to translated english card.

def create_words():
    global select_card
    canvas.itemconfig(title_text, text="french")
    select_card = random.choice(word_dict)
    french_word = select_card["French"]
    #print(f"franch: {french_word}")
    canvas.itemconfig(word_text, text=french_word)
    window.after(3000, flip_card)


def word_known():
    print(len(word_dict))
    print(select_card)
    create_words()
    word_dict.remove(select_card)
    data_unknown = pd.DataFrame(word_dict)
    data_unknown.to_csv("data/word_to_learn.csv", index=False)

# -----------------------------------Create UI-----------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=50, bg=BACKGROUND_COLOR)

# Use Canvas from tkinter to upload image in the window.
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_cover = canvas.create_image(400, 300, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
title_text = canvas.create_text(400, 200, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 300, text="word", font=(FONT_NAME, 60, "bold"))

# Create button
wrong_image = PhotoImage(file="images/wrong.png")
unknown_word = Button(image=wrong_image, command=create_words, highlightthickness=0.1)
unknown_word.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_word = Button(image=right_image, command=word_known, highlightthickness=0.1)
known_word.grid(row=1, column=1)


window.mainloop()