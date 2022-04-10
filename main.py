from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("1280x720+275+20")
window.title("Welcome to the program")

nottuB = Button(window ,text = "Button", fg = "red", bg = "blue" , font = ("Verdana",16))
nottuB.place(x=50, y=70)

label = Label(window, text = "Labels", fg = "red")
label.place(x=75, y=130)

fldtxt = Entry(window, text = "This is a text field", bd =5 )
fldtxt.place(x= 45, y = 150)

v1 = IntVar()
buttonradio = Radiobutton(window, text = "Male" , value = 1, variable= v1)
buttonradio.place(x= 45, y = 170)
buttonradio1 = Radiobutton(window, text = "Female" , value = 2, variable= v1)
buttonradio1.place(x= 45, y = 190)

v2 = StringVar()
v2.set("Bruh1")
data1 = "Student1", "Student2", "Student3"

obmoc = ttk.Combobox(window ,values = data1)
obmoc.place(x = 45, y = 320)

data = "Student1", "Student2", "Student3"

bl = Listbox(window, height= 5, selectmode= "multiple")
for num in data:
    bl.insert(END, num)

bl.place(x = 45, y = 210)

window.mainloop()