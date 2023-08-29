import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from bitinstaller.frames.StartupFrame import StartupFrame
from bitinstaller.frames.InstallationFrame import InstallerFrame
from bitinstaller.frames.finalFrame import InstalledFrame

from bitinstaller.core import InstallationEngine
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
import threading
import os
from subprocess import Popen, PIPE

__author__ = "SGK"
__license__ = "MIT"
__version__ = "v0.1-1"
__status__ = "Development"


class BitInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BitInstaller " + __version__)
        self.configure(bg="#232729")
        self.geometry("867x294")
        self.resizable(False, False)

        self.selectedISO = ""
        self.selectedDrive = ""

        baseDir = os.path.dirname(__file__)
        self.file_path = os.path.join(baseDir, "./logo.png")

        self.runStartupFrame()

    def runStartupFrame(self):
        self.start_display_frame = Frame(self)
        self.renderLogo(self.start_display_frame)

        StartupFrame(self.start_display_frame, self.moveToConfirmation)

        self.start_display_frame.grid()

    def runConfirmationNotification(self):
        try:
            command = Popen(["wimlib-imagex", "--version"], stdout=PIPE)
        except Exception:
            showerror(
                "Error",
                "package 'wimlib-imagex' was not found!, try running brew install wimlib",
            )
            return

        answer = askyesno(
            "Warning",
            "WARNING: ALL OF THE DATA ON THE TARGET DRIVE WILL BE DESTROYED!, ARE YOU SURE YOU WANT TO CONTENUE",
        )
        print(answer)

        if answer == True:
            installerThread = threading.Thread(target=self.beginInstallation)
            installerThread.start()
            return

        else:
            return

    def beginInstallation(self):
        print(self.selectedDrive)
        self.installEngine = InstallationEngine(self.selectedISO, self.selectedDrive)
        self.start_display_frame.destroy()
        # WARNING: SHOW NEW FRAME BEFORE BEGINING INSTALLATION

        self.installingFrame = Frame(self)
        self.renderLogo(self.installingFrame)

        self.installFrame = InstallerFrame(self.installingFrame)
        self.installFrame.updateInstallMessage()
        self.installingFrame.grid()

        # REAL INSTALLATION PART

        self.installEngine.mountSelectedISO()
        print(self.installEngine.mountedISO + "/*")

        self.installEngine.formatDrive()
        self.installEngine.copyISOFiles()
        self.installFrame.updateInstallStage()
        self.installFrame.updateInstallMessage()
        self.installEngine.splitWimfile()

        self.installFrame.destroy()

        InstalledFrame(self.installingFrame)

    def moveToConfirmation(self, data_pipe):  # handle inputs from hosted frame
        print("RECEIVED: ", data_pipe)

        if data_pipe["selectedDisk"] != "" and data_pipe["selectedISO"] != None:
            self.selectedDrive = data_pipe["selectedDisk"].split()
            self.selectedDrive = self.selectedDrive[0]
            self.selectedISO = data_pipe["selectedISO"]
        else:
            showerror(title="Error", message="Error, please input required information")
            return

        self.runConfirmationNotification()

    def renderLogo(self, master):
        image = Image.open(self.file_path)
        resized_image = image.resize((70, 70))
        self.img = ImageTk.PhotoImage(resized_image)
        logo_image_label = Label(
            master, image=self.img, highlightthickness=0, borderwidth=0
        )
        logo_image_label.grid(row=0, column=1, sticky="w", pady=10)
        txt = Label(master, text="BitInstaller " + __version__, background="#232729")
        txt.config(font=("Helvetica bold", 26))
        txt.grid(row=0, column=1, sticky="e")

    def setInstallStage(self):
        self.installFrame.updateInstallStage()


if __name__ == "__main__":
    BitInstaller().mainloop()
