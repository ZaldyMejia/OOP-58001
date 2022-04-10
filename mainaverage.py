from tkinter import *
from tkinter import ttk
window = Tk()

class person:
    def __init__(self, win):

        self.pre = None
        self.mid = None
        self.fin = None
        self.name = None
        self.lbl1 =Label(win, text = "Enter your student number:")
        self.lbl1.place(x=100, y=125)

        self.t1 = Entry()
        self.t1.place(x=275, y=125)

        self.lbl2=Label(win, text = "Average grade: ")
        self.lbl2.place(x=100, y=350)

        self.t2 = Entry()
        self.t2.place(x= 225, y =350)

        self.b1 = Button(win , text = "See grades", command=lambda:[self.studentinfo(), self.grades()])
        self.b1.place (x= 225, y = 170)

        self.studentname = Label(win, text = "Student Name: ")
        self.studentname.place (x = 0, y =0)
        self.namelabel = Entry(bg = "#f0f0f0", bd = 0)
        self.namelabel.place(x=85, y=3)

        self.prelimlbl = Label(win, text="Prelim grade: ")
        self.prelimlbl.place(x=100, y=225)
        self.prelim = Entry()
        self.prelim.place(x=225, y=225)

        self.midtermlbl = Label(win, text="Midterm grade: ")
        self.midtermlbl.place(x=100, y=260)
        self.midterm = Entry()
        self.midterm.place(x=225, y=260)

        self.finalslbl = Label(win, text = "Finals grade: ")
        self.finalslbl.place(x = 100 , y = 300)
        self.finals = Entry()
        self.finals.place(x = 225, y = 300)


    def studentinfo(self):
        self.prelim.delete(0, "end")
        self.midterm.delete(0, "end")
        self.finals.delete(0, "end")
        self.t2.delete(0, "end")
        self.namelabel.delete(0, "end")

        if self.t1.get() == "202111103":
            self.pre = 88
            self.mid = 89
            self.fin = 90
            self.name = "Zaldy Mejia"

        if self.t1.get() == "202135909":
            self.pre = 84
            self.mid = 81
            self.fin = 87
            self.name = "James Alderney"

        if self.t1.get() == "202111697":
            self.pre = 89
            self.mid = 93
            self.fin = 97
            self.name = "Vincent Fabron"

        self.prelim.insert(END, str(self.pre))
        self.midterm.insert(END, str(self.mid))
        self.finals.insert(END, str(self.fin))
        self.namelabel.insert(END, str(self.name))


    def grades(self):
        averagegrade = (self.pre*0.3) + (self.mid*0.3) + (self.fin*0.4)
        self.t2.insert(END, str("%0.2f" % (averagegrade)))

windowobj = person(window)
window.title("Average grade calculator")
window.geometry("700x400+500+30")
window.mainloop()
