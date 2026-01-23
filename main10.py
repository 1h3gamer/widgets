import tkinter as tk
from tkinter import messagebox

class restaurantApp():
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant management System")
        self.root.geometry("500x500")

        self.menu = {
            "fries menu":2,
            "Lunch menu":2,
            "Burger Meal":3,
            "Pizza Meal":4,
            "Cheese Burger":2.5,
            "Drinks":1
        }

        tk.Label(root,text="Restaurant management System",font=("Arial",16,"bold")).pack(pady=10)

        self.entries = {}

        frame = tk.Frame(root)
        frame.pack()

        for item,price in self.menu.items():
            row=tk.Frame(frame)
            row.pack(pady = 3)
            tk.Label(row,text=f"{item}(${price})",width=20,anchor="w").pack(side="left")
            entry=tk.Entry(row,width=5)
            entry.pack(side="right")
            self.entries[item]=entry

        tk.Button(root,text="Place Order",command=self.place_order).pack(pady=15)

    def place_order(self):
        total=0
        bill="Order Summary: \n"

        for item,entry in self.entries.items():
            qty = entry.get()

            if qty.isdigit():
                qty=int(qty)
                if qty > 0:
                    price = self.menu[item]
                    cost = qty * price
                    total += price
                    bill += f"{item} x {qty} = ${cost}"
            
        if total == 0:
            messagebox.showerror("Error","Please enter atleast one item")
        else:
            bill += f"\nTotal Amount: ${total}"
            messagebox.showinfo("Bill",bill)

if __name__ == "__main__":
    root = tk.Tk()
    app=restaurantApp.root()
    root.mainloop()