from tkinter import *

root=Tk()
root.geometry("400x300")
root.title("Main")

def topwin():
    top = Toplevel()
    top.geometry("100x100")
    top.title("Top Level")

    l2 = Label(top, text="This is a Toplevel window")
    l2.pack()

    top.mainloop()

l = Label(root, text = "This is a root window")
btn = Button(root,text = "Click here to open another window",command=topwin)

root.mainloop()