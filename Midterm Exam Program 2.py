from tkinter import *
from tkinter import ttk
window = Tk()

class person:
    def __init__(self, win):
        self.lbl1 =Label(win, text = "Enter your full name: ", fg = "red")
        self.lbl1.place(x=100, y=125)
        self.t1 = Entry(bd = 3)
        self.t1.place(x=275, y=125)

        self.t2 = Entry(bd=3)
        self.t2.place(x=300, y=200)

        self.b1 = Button(win, text="Click to display your full name", fg = "red" , command= self.yourname)
        self.b1.place(x=100, y=200)

    def yourname(self):
        self.t2.delete(0, "end")
        name = str(self.t1.get())
        self.t2.insert(END, str(name))

windowobj = person(window)
window.title("Midterm in OOP")
window.geometry("700x400+500+30")
window.mainloop()