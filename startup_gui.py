from bitinstaller.graphics import RoundedRectangle
from bitinstaller.layout import themeConfig
from bitinstaller.layout import comboboxLayout
from bitinstaller.layout import scrollbarLayout
from bitinstaller.layout import UIRectdata

import tkinter as tk
from tkinter import ttk, NSEW, NS, PhotoImage, Label
from tkinter.ttk import Combobox
import time

# Initialize The TK Window
root = tk.Tk()
root.configure(bg="#0E0E0E")
UIRectdata.update({"master": root})

stl = ttk.Style()
stl.theme_use("clam")
stl.configure("TCombobox", **themeConfig["TCombobox"])
stl.map("TScrollbar",
          # Apply the same settings for normal, active, and hover states
          background=[('active', '#454545'), ('!active', '#454545')],
          arrowcolor=[('active', '#0E0E0E'), ('!active', '#0E0E0E')],
          gripcount=[('active', 0), ('!active', 0)],
          troughcolor=[('active', '#0E0E0E'), ('!active', '#0E0E0E')],
          bordercolor=[('active', '#454545'), ('!active', '#454545')],
          darkcolor=[('active', '#454545'), ('!active', '#454545')],
          lightcolor=[('active', '#454545'), ('!active', '#454545')],
          )

root.option_add('*TCombobox*Listbox.background' % root, '#0E0E0E')

stl.layout(*comboboxLayout)
stl.layout(*scrollbarLayout)

stl.map("TCombobox", background=[("active", "#0E0E0E")], arrowsize=[("active", 15)])

comboBoxRect = RoundedRectangle(**UIRectdata)
comboBoxRect.grid(row=0, column=0)

selectISORect = RoundedRectangle(**UIRectdata)
selectISORect.grid(row=0, column=1)

flashDiskRect = RoundedRectangle(**UIRectdata)
flashDiskRect.grid(row=0, column=2)

selectFileLabel = Label(root, text="Select File", bg="#0E0E0E")
selectFileLabel.config(font=("Courier", 14))
selectFileLabel.grid(row=0, column=1)

flashDiskLabel = Label(root, text="Flash!", bg="#0E0E0E")
flashDiskLabel.config(font=("Courier", 14))
flashDiskLabel.grid(row=0, column=2)

# create listbox object
listbox = Combobox(
    root,
    height=10,
    width=15,
    style="Mystyle.TCombobox",
)

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

listbox.grid(row=0, column=0)

root.mainloop()
