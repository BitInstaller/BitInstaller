from bitinstaller.configuration import TkGraphicsConfig
from bitinstaller.graphics import RoundedRectangle
from bitinstaller.diskinfo import GetDiskInfo
from bitinstaller.system import getFileLocation
from bitinstaller.layout import UIRectdata
from tkinter.ttk import Style, Combobox
from tkinter import Label, Frame


class StartupFrame(Frame):
    def __init__(self, master, pipe):
        super().__init__(master)
        self.master = master
        self.pipe = pipe
        TkGraphicsConfig(self.master, Style())
        self.packagedData = {"selectedDisk": None, "selectedISO": None}
        self.selectedISO = None
        self.configure()

    def configure(self):
        self.master.configure(bg="#232729")
        UIRectdata.update({"master": self.master})
        comboBoxRect = RoundedRectangle(**UIRectdata)
        comboBoxRect.grid(row=1, column=0)
        selectISORect = RoundedRectangle(**UIRectdata)
        selectISORect.grid(row=1, column=1)
        flashDiskRect = RoundedRectangle(**UIRectdata)
        flashDiskRect.grid(row=1, column=2)

        selectFileLabel = Label(self.master, text="Select File", bg="#232729")
        selectFileLabel.config(font=("Courier", 14))
        selectFileLabel.grid(row=1, column=1)
        selectFileLabel.bind("<Button-1>", lambda e: self.getSelectedISO(getFileLocation()))

        flashDiskLabel = Label(self.master, text="Flash!", bg="#232729")
        flashDiskLabel.config(font=("Courier", 14))
        flashDiskLabel.grid(row=1, column=2)
        flashDiskLabel.bind("<Button-1>", lambda e: self.packageData())

        self.listbox = Combobox(
            self.master,
            height=10,
            width=15,
            style="Mystyle.TCombobox",
        )
        self.listbox["values"] = tuple(GetDiskInfo().formattedDriveData)
        self.listbox.grid(row=1, column=0)

    def getSelectedISO(self, ISO):
        self.selectedISO = ISO

    def packageData(self):
        self.packagedData["selectedDisk"] = self.listbox.get()
        self.packagedData["selectedISO"] = self.selectedISO
        self.sendDataToPipe(self.packagedData)

    def sendDataToPipe(self, data):
        self.pipe(data)