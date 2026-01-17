from tkinter import *

window = Tk()
window.title("Length Converter App")
window.geometry("400x400")

entry = Entry()
entry.place(x=120, y=120)

def convert():
    l1 = Label(text="The result in cm is")
    enter = entry.get()
    multiply = enter * 2.54
    l1 = multiply
    return l1

btn = Button(window,text="Click me",command=convert,fg="brown",bg="black")
btn.place(x=220,y=120)

window.mainloop()