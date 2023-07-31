import tkinter as tk
from tkinter import ttk, NSEW, NS, PhotoImage
from tkinter.ttk import Combobox
import time


root = tk.Tk()
root.configure(bg="#0E0E0E")

stl = ttk.Style()

# standerd theme
stl.theme_use("clam")
stl.configure(
    "TCombobox",
    fieldbackground="#0E0E0E",
    foreground="white",
    background="#0E0E0E",
    focusfill="#0E0E0E",
    arrowcolor="white",
    darkcolor="#414141",
    selectbackground="#0E0E0E",
    lightcolor="#414141",
    bordercolor="lime",

)

stl.layout(
    'Mystyle.TCombobox', [(
        'Combobox.field', {
            'sticky': 'NSEW',
            'children': [(
                'Mystyle.TCombobox.downarrow', {
                    'side': 'right',
                    'sticky': 'NS',
                }
            ), (
                'Combobox.padding', {
                    'expand': '1',
                    'sticky': 'NSEW',
                    'children': [(
                        'Combobox.textarea', {
                            'sticky': 'NSEW'
                        }
                    )]
                }
            )]
        }
    )]
)


stl.map("TCombobox", background=[("active", "#0E0E0E")], arrowsize=[("active", 15)])


root.option_add("*TCombobox*Listbox.selectBackground", "#0E0E0E")

# Create a Frame to hold the progress bar
frame = tk.Frame(root)
frame.configure(bg="#0E0E0E")
frame.pack(side="bottom")

# create listbox object
listbox = Combobox(
    root,
    height=10,
    width=15,
    style='Mystyle.TCombobox',
)

root.option_add("*TCombobox*Listbox.background", "#0E0E0E")

listbox.configure(background="#0E0E0E")

listbox["values"] = (
    " January",
    " February",
    " March",
    " April",
    " May",
    " June",
    " July",
    " August",
    " September",
    " October",
    " November",
    " December",
)
listbox.current()

listbox.pack()

root.mainloop()
