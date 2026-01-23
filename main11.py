from tkinter import *

main = Tk()
main.title("Interest Calculator")
main.geometry("500x500")


l1 = Label(main, text="Principle", bg='light grey')
l2 = Label(main, text="Interest", bg='light grey')
l3 = Label(main, text="Num of Years", bg='light grey')

l1.place(x=180, y=200)
l2.place(x=180, y=230)
l3.place(x=180, y=260)

t1 = Entry(main)
t2 = Entry(main)
t3 = Entry(main)

t1.place(x=270, y=200)
t2.place(x=270, y=230)
t3.place(x=270, y=260)



def calculate():
    p = float(t1.get())
    r = float(t2.get())
    t = float(t3.get())

    interest = (p * r * t)/100
    result_label.config(text="Simple Interest = "+str(interest))

Button(main, text = "Calculate", command = calculate).pack(pady=10)
result_label = Label(main, text = "Simple interest = ")
result_label.pack()

main.mainloop()