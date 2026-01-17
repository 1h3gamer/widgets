from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.title("Denomination Calculator")
root.configure(bg='light blue')
root.geometry("650x400")

try:
    upload=Image.open("money1_cxi7bu.jpg")
    upload=upload.resize(300,300)
    image=ImageTk.PhotoImage(upload)
    label=Label(root,image=image,bg='light blue')
    label.pack(x=180,y=20)
except:
    pass

label1 = Label(root,text="Hey user!Welcome to denomination counter app",bg='light blue')
label1.place(relx=0.5,rely=340)

def msg():
    messagebox.showinfo("Alert!","Do you want to calculate the denomination count?")
    topwin()

button1 = Button(root,text="Let's get started", command=msg, bg="brown", fg="white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel(root)
    top.title("Denomination calculator")
    top.configure(bg="light grey")
    top.geometry("600x360")

    label = Label(top, text="Enter total amount", bg='light blue')
    label.place(x=230, y=50)

    entry = Entry(top)
    entry.place(x=200, y=80)

    lbl = Label(top, text="Here are the number of notes for each denomination:", bg='lightblue')
    lbl.place(x=120, y=170)

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    def calculate():
        try:
            amount=int(entry.get())

            note2000 = amount//2000
            amount = amount % 2000

            note500 = amount//500
            amount = amount % 500

            note100 = amount//100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END, note2000)
            t2.insert(END, note500)
            t3.insert(END, note100)
        except ValueError:
            messagebox.showerror("Error","Please enter a valid number")
    btn = Button(top, text="Calculate", command=calculate, bg="brown", fg="white")
    btn.place(x=240, y=120)

root.mainloop()