from tkinter.ttk import Style, Combobox
from tkinter import Label
from bitinstaller.configuration import TkGraphicsConfig
from bitinstaller.layout import UIRectdata
from PIL import Image, ImageTk
from bitinstaller.graphics import RoundedRectangle
from bitinstaller.diskinfo import GetDiskInfo
from bitinstaller.system import getFileLocation



class StartupFrame:
    def __init__(self, master):
        self.master = master
        
        self.master.configure(bg="#232729")
        UIRectdata.update({"master": self.master})
        self.style = Style()
        TkGraphicsConfig(self.master, self.style)
        self.configure()

    def configure(self):
        comboBoxRect = RoundedRectangle(**UIRectdata)
        comboBoxRect.grid(row=1, column=0)
        selectISORect = RoundedRectangle(**UIRectdata)
        selectISORect.grid(row=1, column=1)
        flashDiskRect = RoundedRectangle(**UIRectdata)
        flashDiskRect.grid(row=1, column=2)
        selectFileLabel = Label(self.master, text="Select File", bg="#232729")
        selectFileLabel.config(font=("Courier", 14))
        selectFileLabel.grid(row=1, column=1)
        selectFileLabel.bind("<Button-1>", lambda e: print(getFileLocation()))
        flashDiskLabel = Label(self.master, text="Flash!", bg="#232729")
        flashDiskLabel.config(font=("Courier", 14))
        flashDiskLabel.grid(row=1, column=2)
        flashDiskLabel.bind("<Button-1>", lambda e: print("Flashing File!"))
        listbox = Combobox(
            self.master,
            height=10,
            width=15,
            style="Mystyle.TCombobox",
        )
        listbox["values"] = tuple(GetDiskInfo().formattedDriveData)
        listbox.grid(row=1, column=0)
