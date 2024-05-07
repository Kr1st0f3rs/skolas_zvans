import tkinter as tk
from tkinter import *
import time

#logs
logs=Tk()
logs.title("Skolas zvans")
canvas = Canvas(logs, width=800, height=700)
canvas.pack()

#galvenais cikls


#zvans
zvans1=canvas.create_rectangle(300,200,500,600,fill="dark gray",outline="")
zvans2=canvas.create_rectangle(150,500,650,600,fill="light gray",outline="")
zvans3=canvas.create_oval(250,100,550,400,fill="orange",outline="")
zvans4=canvas.create_oval(375,225,425,275,fill="gray",outline="")
zvans5=canvas.create_polygon(580,500,680,250,700,250,600,500,fill="gray",outline="")
zvans6=canvas.create_oval(660,230,710,280,fill="red",outline="")



logs.mainloop()
#izveidot skolas zvanu, kas skan ikpēc katras stundas, un starpbrīža.