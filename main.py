from tkinter import * 
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title('Digital Clock')

def time():
    string = strftime('%H:%M:%S %p')
    Lbl.config(text = string)
    Lbl.after(1000, time)

Lbl = Label(window, font=('arial', 45 "bold"), background = 'orange')
Lbl.pack(anchor = "center")

time()
mainloop()