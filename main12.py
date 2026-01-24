from tkinter import *

main = Tk()
main.title("Password checker")
main.geometry("500x500")

l1=Label(main,text="Type in a password",fg="black")
e1=Entry(main)
l2=Label(main,text="Weak password",fg="black")
l3=Label(main,text="Strong password",fg="black")

for i in e1:
    if i<=6:
        print(f"{l2}")
    else:
        print(f"{l3}")

main.mainloop