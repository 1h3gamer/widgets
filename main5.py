from tkinter import *

root = Tk()
root.title=("Getting started with Widgets")
root.geometry=("400x300")

frame = Frame(master=root,height=360,width=200,bg="white")
lbl1 = Label(frame,text="This will calculate the product of any two given numbers",bg="#3895D3",fg="white",width=12)
lbl2 = Label(frame,text="Number 1",bg="#3895D3",fg="white",width=12)
lbl3 = Label(frame,text="Number 2",bg="#3895D3",fg="white",width=12)

number1_entry = Entry(frame)
number2_entry = Entry(frame)

def product():
    number1=number1_entry.get()
    number2=number2_entry.get()
    multiply = number1 * number2
    textbox.insert(END,multiply)

textbox = Text(fg="black",bg="white")

btn = Button(text="Multiply?",command=product,bg="red")

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
number1_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
number2_entry.place(x=150,y=88)
lbl3.place(x=20,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()