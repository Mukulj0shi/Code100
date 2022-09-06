#!usr/bin/env python3
"""

"""
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    count_down(5)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    minute = 0
    second = 0
    count_down(minute, second)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(min, sec):
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if sec <= 59:
        tk.after(1000, count_down, min, sec + 1)
    elif sec == 60:
        tk.after(1000, count_down, min + 1, 0)


# ---------------------------- UI SETUP ------------------------------- #
tk = Tk()
tk.title("POMODORO")
tk.config(padx=100, pady=100, bg=YELLOW)

time_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
time_label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
fill_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=fill_image)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


# count_down(5)

def clickbutton():
    pass


start_button = Button(text="Start", command=start_timer, fg=GREEN)
start_button.grid(row=3, column=1)

reset_button = Button(text="reset", command=reset_timer, fg=GREEN)
reset_button.grid(row=3, column=3)

check_label = Label(text="✓", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=4, column=2)

tk.mainloop()
