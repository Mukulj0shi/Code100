#!usr/bin/env python3
"""
This program creates a POMODORO timer with 25 minute long breaks, 5 minutes short break and 15 minute llong break.
Tkinter module and math module is used.
Canvas is used to add text to tkinter(using PhotoImage)
Canvas.text is used to write a text over the image
"""
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer = None
rep = 1
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    tk.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer")  # >>>> Not working
    check_label.config(text="")
    global rep
    rep = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    print(rep)
    if rep % 8 == 0:
        rep += 1
        time_label.config(text="Long Break Earned")
        #long_break_label = Label(text="Long Break Earned", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=RED)
        #long_break_label.grid(row=1, column=2)
        count_down(LONG_BREAK_MIN * 60)
    elif rep % 2 == 0:
        rep += 1
        time_label.config(text="Short Break deserved")
        #short_break_label = Label(text="Short Break deserved", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
        #short_break_label.grid(row=1, column=2)
        count_down(SHORT_BREAK_MIN * 60)
    elif rep % 2 == 1:
        rep += 1
        time_label.config(text="Work")
        #work_label = Label(text="Work", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
        #work_label.grid(row=1, column=2)
        print(f"work {rep}")
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if count > 0:
        global timer
        if sec >= 10:
            canvas.itemconfig(timer_text, text=f"{min}:{sec}")
            timer = tk.after(1000, count_down, count - 1)
        elif sec < 10:
            canvas.itemconfig(timer_text, text=f"{min}:0{sec}")
            timer = tk.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        marks=""
        work_session = math.floor(rep/2)
        for _ in range (work_session):
            marks = "✓"
        check_label.config(text=marks)


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
start_button = Button(text="Start", command=start_timer, fg=GREEN)
start_button.grid(row=3, column=1)

reset_button = Button(text="reset", command=reset_timer, fg=GREEN)
reset_button.grid(row=3, column=3)

check_label = Label(text="", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=4, column=2)

tk.mainloop()
