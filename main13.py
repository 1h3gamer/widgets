import tkinter as tk
import random

window = tk.Tk()
window.title("Rock,Paper,Scissors")
window.geometry("400x400")

heading = tk.Label(window, text = "Rock, Paper, Scissors", font = ("Arial", 16 ,"bold"))
heading.pack(pady = 10)

instruction = tk.Label(window, text = "Choose one: ", font = ("Arial", 16 ,"bold"))

rock_btn = tk.Button(window, text = "Rock", width = 12, command =lambda: play("Rock"))
rock_btn.pack(pady = 5)

paper_btn = tk.Button(window, text = "Paper", width = 12, command =lambda: play("Paper"))
paper_btn.pack(pady = 5)

scissors_btn = tk.Button(window, text = "Scissors", width = 12, command =lambda: play("Scissors"))
scissors_btn.pack(pady = 5)

choices = ["Rock","Paper","Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    result_text = "You chose: " + user_choice + "\nComputer chose: " + computer_choice

    if user_choice ==computer_choice:
        result_text += "\nResult: It's a Tie!"
    elif(user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text += "\nResult: You Win!"
    else:
        result_text += "\nResult: Computer Wins!"

    result_label.config(text=result_text)

result_label = tk.Label(window, text = "", font = ("Arial", 11), fg = "blue")
result_label.pack(pady = 15)

window.mainloop()