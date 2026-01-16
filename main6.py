from tkinter import *

window = Tk()
window.title=("Age Calculator App")
window.geometry=("400x400")

def calculate_age():
    birth_year = int(birth_entry.get())
    current_year = int(current_entry.get())

    age = current_year - birth_year

    result_text.delete(1.0,END)
    result_text.insert(END, f"Your age is: {age} years")

Label(window, text= "Enter Birth Year: ").pack(pady=5)
birth_entry=Entry(window)
birth_entry.pack(pady=5)

Label(window, text="Enter Current Year: ").pack(pady=5)
current_entry=Entry(window)
current_entry.pack(pady=5)

calculate_button = Button(window, text= "Calculate age", command = calculate_age)
calculate_button.pack(pady=10)

result_text = Text(window, height= 2, width=30)
result_text.pack(pady=10)

window.mainloop()