from bitinstaller.configuration import TkGraphicsConfig
from bitinstaller.graphics import RoundedRectangle
from bitinstaller.diskinfo import GetDiskInfo
from bitinstaller.system import getFileLocation
from bitinstaller.layout import InvisibleUIRectdata
from tkinter.ttk import Style, Combobox
from tkinter import Label, Frame
from tkinter import StringVar


class InstallerFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.currentInstallStage = 0
        self.installMessage = StringVar()
        self.installMessage.set("")
        TkGraphicsConfig(self.master, Style())
        self.configure()

    def configure(self):
        self.master.configure(bg="#232729")
        InvisibleUIRectdata.update({"master": self.master})
        invisibleBoxOne = RoundedRectangle(**InvisibleUIRectdata)
        invisibleBoxOne.grid(row=1, column=0)
        invisibleBoxTwo = RoundedRectangle(**InvisibleUIRectdata)
        invisibleBoxTwo.grid(row=1, column=1)
        invisibleBoxThree = RoundedRectangle(**InvisibleUIRectdata)
        invisibleBoxThree.grid(row=1, column=2)

    def updateInstallMessage(self):
        if self.currentInstallStage == 0:
            installProgressLabel = Label(self.master, text="Please Wait\nInstalling your Windows ISO for you!", bg="#232729")
            installProgressLabel.config(font=("Courier", 14))
            installProgressLabel.grid(row=1, column=1)
        elif self.currentInstallStage == 1:
