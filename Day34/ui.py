#!usr/bin/env python3

"""
This class creates a UI interface using Tkinter module and is called in main.py
"""
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain=QuizBrain):
        self.quiz_text = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.time_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.time_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.quiz = self.canvas.create_text(150, 125, text="00:00", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, command=self.correct_answer, font="Verdana 20 bold")
        self.right_button.grid(row=2, column=0)
        self.right_button.grid()

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, command=self.incorrect_answer, font="Verdana 20 bold")
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz_text.next_question()
        self.canvas.itemconfig(self.quiz, text=q_text)

    def correct_answer(self):
        right_ans = self.quiz_text.check_answer("True")
        self.right_button.

    def incorrect_answer(self):
        wrong_ans = self.quiz_text.check_answer("False")