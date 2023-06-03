# in This project we create the dice using simulation 
import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x400")
window.title("Dice Simulator")

Dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
image1 = None  # Declare the variable globally


def dice_roll():
    global image1  # Use the global variable
    image1 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    label.configure(image=image1)
    label.image = image1


image1 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
label = tk.Label(window, image=image1)
label.image = image1
label.place(x=200, y=100)

button = tk.Button(window, text="Roll", bg="black", font="Time 20 bold", fg="red", command=dice_roll)
button.place(x=235, y=250)

window.mainloop()
