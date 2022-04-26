from tkinter import *
window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

class myWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text = "Standard Calculator", )
        self.lbl1.place(relx=0.50,y=50, anchor="center")
        self.lbl2 = Label(window, text = "Input 1st number: ")
        self.lbl2.place(x = 50, y = 80)
        self.txtfld2 = Entry(window, bd = 3)
        self.txtfld2.place(x=180, y = 80)
        self.lbl3 = Label(window, text = "Input 2nd number: ")
        self.lbl3.place(x= 50, y =130)
        self.txtfld3 = Entry(window, bd = 3)
        self.txtfld3.place(x= 180, y = 130)

        self.lbl4 = Label(window, text = "Choose among the following operators", bg = "Yellow")
        self.lbl4.place(x = 100 , y = 250)
        self.btn1 = Button(window, text= "Add(+)", command= self.add)
        self.btn1.place(x=50 , y =170)
        self.btn2 = Button (window, text="Subtract(-)", command=self.subtract)
        self.btn2.place(x=120, y =170)
        self.btn3 = Button(window, text= "Multiply(*)", command=self.mult)
        self.btn3.place(x = 210 , y = 170)
        self.btn4 = Button (window, text = "Division(/)")
        self.btn4.place(x = 300, y = 170)
        self.btn4.bind("<Button-1>", self.div)


        self.lbl5 = Label(window, text = "Answer:")
        self.lbl5.place (x = 50, y= 210)

        self.txtfld4 = Entry(window, bd = 3)
        self.txtfld4.place(x = 180 , y =210)

    def add(self):
        self.txtfld4.delete(0, "end")
        num1 = int(self.txtfld2.get())
        num2 = int(self.txtfld3.get())
        answer = num1+num2
        self.txtfld4.insert(END, answer)

    def subtract(self):
        self.txtfld4.delete(0, "end")
        num1 = int(self.txtfld2.get())
        num2 = int(self.txtfld3.get())
        answer = num1-num2
        self.txtfld4.insert(END, answer)

    def mult(self):
        self.txtfld4.delete(0, "end")
        num1 = int(self.txtfld2.get())
        num2 = int(self.txtfld3.get())
        answer = num1*num2
        self.txtfld4.insert(END, answer)

    def div(self, event):
        self.txtfld4.delete(0, "end")
        num1 = int(self.txtfld2.get())
        num2 = int(self.txtfld3.get())
        answer = num1/num2
        self.txtfld4.insert(END, answer)

windowobj = myWindow(window)
window.mainloop()
