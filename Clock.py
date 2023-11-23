import tkinter as tk
import time
import math 

class Clock(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.label = tk.Label(self, font=("Arial", 24), background="black", foreground="white")
        self.label.pack(anchor="center")

        self.update()

    def update(self):
        now = time.strftime("%H:%M:%S")
        self.label.config(text=now)
        self.after(1000, self.update)

root = tk.Tk()
root.title("Clock")
root.geometry("200x200")
root.configure(background="black")

clock = Clock(root)

root.mainloop()