import tkinter.messagebox
from tkinter import *
import tkinter.font as TkFont
from tkinter import ttk

window = Tk()

myFont = TkFont.Font(window, family="Helvetica", size=12)

def cto():
    if len(Entry2.get()) != 0 or len(Entry3.get()) != 0:
        tkinter.messagebox.showerror("Error!", "Multiple inputs in the other temperature textbox. Please delete other inputs from the other conversion and try again")
        reset()
        return None
    temperature = float(Entry1.get())
    fah = (temperature*9)/5 + 32
    kel = temperature + 273.15
    Entry2.insert(END, fah)
    Entry3.insert(END, kel)

def fto():
    if len(Entry1.get()) != 0 or len(Entry3.get()) != 0:
        tkinter.messagebox.showerror("Error!", "Multiple inputs in the other temperature textbox. Please delete other inputs from the other conversion and try again")
        reset()
        return None
    temperature = float(Entry2.get())
    cel = (temperature - 32) * 5/9
    kel = (temperature - 32) * 5/9 +273.15
    Entry1.insert(END, cel)
    Entry3.insert(END, kel)

def kto():
    if len(Entry1.get()) != 0 or len(Entry2.get()) != 0:
        tkinter.messagebox.showerror("Error!", "Multiple inputs in the other temperature textbox. Please delete other inputs from the other conversion and try again")
        reset()
        return None
    temperature = float(Entry3.get())
    cel = (temperature - 273.15)
    fah = (temperature - 273.15) * 9 / 5 + 32
    Entry1.insert(END, cel)
    Entry2.insert(END, fah)

def reset():
    Entry1.delete(0, "end")
    Entry2.delete(0, "end")
    Entry3.delete(0, "end")




Title = Label(window, text="Temperature Conversion", justify="center", background='#A5BFDA', font=(myFont))
Title.grid(column=0, row=0,ipadx=100,columnspan=2)
Title1 = Label(window, text="Celsius: ", justify="center", background='#A5BFDA',font=(myFont))
Title1.grid(column=0, row=1,pady=50)
Entry1 = Entry(bd=10)
Entry1.grid(column=1, row=1)
Title2 = Label(window, text="Fahrenheit", justify="center", background='#A5BFDA',font=(myFont))
Title2.grid(column=0, row=2)
Entry2 = Entry(bd=10)
Entry2.grid(column=1, row=2)
Title3 = Label(window, text="Kelvin", justify="center",  background='#A5BFDA',font=(myFont) )
Title3.grid(column=0, row=3, pady=50)
Entry3 = Entry(bd=10)
Entry3.grid(column =1 , row=3)
Button1 = Button(window, text="Convert from Celsius", font=(myFont), command=cto)
Button1.grid(column=0, row=5, columnspan=1, pady=20)
Button2 = Button(window, text="Convert from Fahrenheit", font=(myFont), command=fto)
Button2.grid(column= 1, row=5)
Button3 = Button(window, text="Convert from Kelvin", font=(myFont), command=kto )
Button3.grid(column=0, row=6, ipadx=7 )
Button4 = Button(window, text="RESET", font=(myFont), command=reset )
Button4.grid(column=1, row=6, ipadx=57)

window.geometry("385x500+20+50")
window.title("Calculator")
window.configure(background='#A5BFDA')
window.mainloop()



