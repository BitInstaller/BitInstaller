from bitinstaller.graphics import RoundedRectangle
from bitinstaller.graphics import CleanProgressBar
from bitinstaller.diskinfo import GetDiskInfo
from bitinstaller.layout import themeConfig
from bitinstaller.layout import comboboxLayout
from bitinstaller.layout import scrollbarLayout
from bitinstaller.layout import UIRectdata
from bitinstaller.system import getFileLocation

import tkinter as tk
from tkinter import ttk, NSEW, NS, PhotoImage, Label, Frame
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import time

# Initialize The TK Window
root = tk.Tk()
root.configure(bg="#232729")

# start screen frame
startDisplayFrame = Frame(root)
startDisplayFrame.grid()
startDisplayFrame.configure(bg="#232729")

UIRectdata.update({"master": startDisplayFrame})

image = Image.open("logo.png")
resize_image = image.resize((70, 70))
img = ImageTk.PhotoImage(resize_image)



#logoImage = PhotoImage(file="logo.png")
logoImageLabel = tk.Label(startDisplayFrame, image=img, highlightthickness=0, borderwidth=0)
logoImageLabel.grid(row=0, column=1,sticky="w")

txt = Label(startDisplayFrame, text="BitInstaller v0.1-0", background="#232729")
txt.config(font=('Helvetica bold', 26))
txt.grid(row=0, column=1, sticky="e")

stl = ttk.Style()
stl.theme_use("clam")
stl.configure("TCombobox", **themeConfig["TCombobox"])
stl.configure("Horizontal.TProgressbar", **themeConfig["Horizontal.TProgressbar"])

startDisplayFrame.option_add('*TCombobox*Listbox.selectBackground' % startDisplayFrame, '#499BD8')
startDisplayFrame.option_add("*TCombobox*Listbox.background" % startDisplayFrame, "#232729")

stl.map(
    "TScrollbar",
    # Apply the same settings for normal, active, and hover states
    background=[("active", "#454545"), ("!active", "#454545")],
    arrowcolor=[("active", "#232729"), ("!active", "#232729")],
    gripcount=[("active", 0), ("!active", 0)],
    troughcolor=[("active", "#232729"), ("!active", "#232729")],
    bordercolor=[("active", "#454545"), ("!active", "#454545")],
    darkcolor=[("active", "#454545"), ("!active", "#454545")],
    lightcolor=[("active", "#454545"), ("!active", "#454545")],
)


stl.layout(*comboboxLayout)
stl.layout(*scrollbarLayout)

stl.map("TCombobox", background=[("active", "#232729")], arrowsize=[("active", 15)])

comboBoxRect = RoundedRectangle(**UIRectdata)
comboBoxRect.grid(row=1, column=0)

selectISORect = RoundedRectangle(**UIRectdata)
selectISORect.grid(row=1, column=1)

flashDiskRect = RoundedRectangle(**UIRectdata)
flashDiskRect.grid(row=1, column=2)

selectFileLabel = Label(startDisplayFrame, text="Select File", bg="#232729")
selectFileLabel.config(font=("Courier", 14))
selectFileLabel.grid(row=1, column=1)
selectFileLabel.bind("<Button-1>", lambda e: print(getFileLocation()))

flashDiskLabel = Label(startDisplayFrame, text="Flash!", bg="#232729")
flashDiskLabel.config(font=("Courier", 14))
flashDiskLabel.grid(row=1, column=2)
flashDiskLabel.bind("<Button-1>", lambda e: print("Flashing File!"))
# create listbox object
listbox = Combobox(
    startDisplayFrame,
    height=10,
    width=15,
    style="Mystyle.TCombobox",
)

listbox["values"] = tuple(GetDiskInfo().formattedDriveData)

listbox.grid(row=1, column=0)

#bar = CleanProgressBar(startDisplayFrame)

#bar.updateProgressBar(50)

startDisplayFrame.mainloop()
