import tkinter.messagebox
from tkinter import *
import tkinter.font as TkFont
from tkinter import ttk
window = Tk()

myFont = TkFont.Font(window, family="Helvetica", size=12)

def smallestnum():
    if len(Entry1.get()) == 0 or len(Entry2.get()) == 0 or len(Entry3.get()) == 0:
        tkinter.messagebox.showerror("Error!", "Missing input! Please try again and make sure each textbox has an input")
        reset()
        return None
    # Find the least number among three numbers
    Entry4.delete(0,"end")
    L = []
    L.append(int(Entry1.get()))
    L.append(int(Entry2.get()))
    L.append(int(Entry3.get()))
    Largenum.set(int(min(L)))

def reset():
    Entry1.delete(0, "end")
    Entry2.delete(0, "end")
    Entry3.delete(0, "end")

lbl1 = Label(window, text = "The Program that Finds the smallest Number", bg='#A5BFDA', font=(myFont))
lbl1.grid(row=0, column=0, columnspan=2)
lbl2 = Label(window,text = "Enter the first number:", bg='#A5BFDA', font=(myFont))
lbl2.grid(row=1, column=0, sticky=W,pady=25)
Entry1 = Entry(bd=10)
Entry1.grid(row=1, column=1)
lbl3 = Label(window,text = "Enter the second number:", bg='#A5BFDA', font=(myFont))
lbl3.grid(row=2, column=0,sticky=W)
Entry2 = Entry(bd=10)
Entry2.grid(row=2, column=1)
lbl4 = Label(window, text= "Enter the third number:", bg='#A5BFDA', font=(myFont))
lbl4.grid(row=3, column=0,sticky=W,pady=25)
Entry3 = Entry(bd=10)
Entry3.grid(row=3, column=1)
Bt1 = Button(window, text="Find the Smallest number", command=smallestnum,bd=5)
Bt1.grid(row=4, column=1)
lbl5 = Label(window, text="The Smallest variable is: ", bg='#A5BFDA', font=(myFont))
lbl5.grid(row=5, column=0, sticky=W,pady=25)
Largenum = StringVar(window, "Smallest number will appear here")
Entry4 = Entry(bd=10, textvariable=Largenum,justify="center")
Entry4.grid(row=5, column=1,ipadx=50,padx=75)





window.title("Find the smallest number")
window.geometry("525x300+20+10")
window.configure(background='#A5BFDA')
mainloop()