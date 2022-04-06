from textwrap import wrap
from tkinter import *
import random


class Start:
    def __init__(self, parent):
        # initialise start frame; get quiz difficulty here
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.quiz_label = Label(self.start_frame, text="LoL Champion Game", justify=LEFT, font="arial 14 bold", bg="white")
        self.quiz_label.grid(row=0)

        self.quiz_instructions = Label(self.start_frame, bg="white",font="arial 10", text="Please select a difficulty level to continue", wrap=150)
        self.quiz_instructions.grid(row=1)

        # set reusable fonts and images here
        button_font = "Arial 12 bold"
        silver_image = PhotoImage(file="challenger.gif")

        # stakes buttons frame (row 3)
        self.difficulty_frame = Frame(self.start_frame, bg="white")
        self.difficulty_frame.grid(row=4, pady=10)

        # silver button (medium/average difficulty)
        self.medium_difficulty_button = Button(self.difficulty_frame, image=silver_image, font=button_font, bg="#FFF2CC", command=lambda: self.to_game(2)).pack()
        self.medium_difficulty_button.grid(row=0, column=1, pady=10, padx=5)        

        # challenger button (hard difficulty)
        self.hard_difficulty_button = Button(self.difficulty_frame, text="Hard", font=button_font, bg="#F8CECC", command=lambda: self.to_game(3))
        self.hard_difficulty_button.grid(row=0, column=2, pady=10)

    def to_game(self):
        print()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("League of Legends Champions")
    something = Start(root)
    root.mainloop()