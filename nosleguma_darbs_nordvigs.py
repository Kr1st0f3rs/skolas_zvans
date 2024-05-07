import tkinter as tk
from tkinter import *
import time as time

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

#animacija
def animacija(elapsed_time=0):
    if elapsed_time < 110:
        canvas.move(zvans6, -1, 0)
        canvas.move(zvans5, -1, 0)
        logs.after(1, lambda: animacija(elapsed_time + 1))
    else:
        pass

def animacija_atpakal(elapsed_time=0):
    if elapsed_time < 110:
        canvas.move(zvans6, 1, 0)
        canvas.move(zvans5, 1, 0)
        logs.after(1, lambda: animacija_atpakal(elapsed_time + 1))
    else:
        pass

# Define buttons to trigger animations
animacija_poga = Button(logs, text="animacija", command=lambda: animacija())
animacija_poga.place(x=700, y=600)
animacija_poga2 = Button(logs, text="animacija_back", command=lambda: animacija_atpakal())
animacija_poga2.place(x=700, y=500)


logs.mainloop()
#izveidot skolas zvanu, kas skan ikpēc katras stundas, un starpbrīža.