import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.configure(bg="#0E0E0E")

# Create a Frame to hold the progress bar
frame = tk.Frame(root)
frame.configure(bg="#0E0E0E")
frame.pack(side="bottom")

stl = ttk.Style()
# standerd theme
stl.theme_use("clam")

stl.configure(
    "Horizontal.TProgressbar",
    troughcolor="#0E0E0E",
    background="#1E90FF",
    bordercolor="#0E0E0E",
    lightcolor="#0E0E0E",
    darkcolor="#0E0E0E",
)

var_5 = tk.IntVar(value=0)

progressbar = ttk.Progressbar(
    frame,
    orient="horizontal",
    length=400,
    mode="determinate",
    variable=var_5,
)

number_label = tk.Label(frame, textvariable=var_5)

number_label.configure(bg="#0E0E0E")

number_label.pack(side='left')

progressbar.pack(ipady=10)

frame.place(relx=0.5, rely=1,anchor="s")


def update_progress_bar():
    x = var_5.get()
    if x < 100:
        var_5.set(x+1)
        root.after(50, update_progress_bar)
    else:
        print("Complete")

update_progress_bar()


root.mainloop()
