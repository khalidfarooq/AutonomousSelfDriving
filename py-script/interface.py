import sys
import os
from tkinter import *

window=Tk()

window.title("GUI Vehichle Detection & Avoidance")
window.geometry('550x200')

def run():
    os.system('python3 main.py')

author = Label(window,text="Developed by Abaypiya")
btn = Button(window, text="Click To Start", bg="black", fg="white",command=run)

btn.place(relx=0.5, rely=0.5, anchor=CENTER)
author.place(relx=1, rely=1, anchor=SE)
window.mainloop()