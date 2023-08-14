from bitinstaller.configuration import TkGraphicsConfig
from bitinstaller.graphics import RoundedRectangle
from bitinstaller.layout import InvisibleUIRectdata
from tkinter.ttk import Style
from tkinter import Label, Frame


class InstallerFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.currentInstallStage = 0
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
        # Begining
        if self.currentInstallStage == 0:
            self.installProgressLabel = Label(self.master, text="Please Wait\nInstalling Windows for you!", bg="#232729")
            self.installProgressLabel.config(font=("Courier", 14))
            self.installProgressLabel.grid(row=1, column=1)

        # during install.wim
        elif self.currentInstallStage == 1:
            self.installProgressLabel.destroy()
            self.installProgressLabel = Label(self.master, text="Please Wait\nSplitting Wimfile", bg="#232729")
            self.installProgressLabel.config(font=("Courier", 14))
            self.installProgressLabel.grid(row=1, column=1)

    def updateInstallStage(self):
        self.currentInstallStage+=1