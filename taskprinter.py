# tkinter = library with loads of interface options
# random  is needed for the random.shuffle
import io
from tkinter import *
import random

# Root is the main window from which we work can be called anything basically
# Title adds a title instead of TK
# Geometry opens the window bigger then base size
import output as output

root = Tk()
root.title("Task Manager")
root.geometry("800x800")

# This should go into a database


kids = ["Nick",
        "Xandra",
        "Natasha",
        "Anastasia"]


chores = ["Vaatwasser Inruimen",
          "Vaatwasser Uitruimen",
          "Wc Beneden",
          "Wc Boven",
          "Bed Verschonen",
          "Stofzuigen Beneden",
          "Stofzuigen Boven",
          "Kamer Opruimen"]


# This shuffles the lists so it picks random kid/chores


random.shuffle(kids)
random.shuffle(chores)
buffer = io.StringIO()

# This has the buttons and what they do


class Buttons:

    def __init__(self, parent):
        frame = Frame(parent)
        frame.grid()

        self.print_button = Button(frame, text="Print Task List", command=self.print_message, height=10, width=30,
                                      fg="yellow", bg="black")
        self.print_button.grid(row=0,)

        self.quit_button = Button(frame, text="Quit", command=frame.quit, height=10, width=30, fg="yellow",
                                     bg="black")
        self.quit_button.grid(row=0, column=1)

    def print_message(self):
        for i in range(len(kids)):
            print(kids[i])
            print((chores[i * 2:i * 2 + 2]))


# "def buttonClick(self, event):" part of somehow making it print to text block


text_field1 = Text()
# (buffer.getvalue())
text_field1.grid(row=0)

# dunno how to make this work "text_field1.insert("end-1c", output)"


# This shows where the buttons go


b = Buttons(root)


# This keeps the program running


root.mainloop()
