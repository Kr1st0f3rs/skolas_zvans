import tkinter as tk
from tkinter import *
import time

#logs
logs=Tk()
logs.title("Skolas zvans")
canvas = Canvas(logs, width=800, height=800)
canvas.pack()

#galvenais 
zvans1=canvas.create_oval(250,100,550,400,fill="orange",outline="")
zvans2=canvas.create_rectangle(300,200,500,600,fill="gray",outline="")


logs.mainloop()
#izveidot skolas zvanu, kas skan ikpēc katras stundas, un starpbrīža.