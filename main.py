import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from bitinstaller.frames.StartupFrame import StartupFrame
from bitinstaller.frames.InstallationFrame import InstallerFrame

from bitinstaller.core import InstallationEngine
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror


__author__ = "SGK"
__license__ = "MIT"
__version__ = "v0.1-0"
__status__ = "Development"

class BitInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BitInstaller " + __version__)
        self.configure(bg="#232729")
        self.geometry("867x294")

        self.selectedISO = ""
        self.selectedDrive = ""

        self.runStartupFrame()

    def runStartupFrame(self):
        self.start_display_frame = Frame(self)

        self.renderLogo(self.start_display_frame)

        #StartupFrame(self.start_display_frame, self.moveToConfirmation)
        InstallerFrame(self.start_display_frame)
        self.start_display_frame.grid()

    def runConfirmationNotification(self):
        answer = askyesno("Warning", "WARNING: ALL OF THE DATA ON THE TARGET DRIVE WILL BE DESTROYED!, ARE YOU SURE YOU WANT TO CONTENUE")
        print(answer)

        if(answer == True):
            print(self.selectedDrive)
            self.installEngine = InstallationEngine(self.selectedISO, self.selectedDrive)
            self.start_display_frame.destroy()
            # WARNING: SHOW NEW FRAME BEFORE BEGINING INSTALLATION
            

            self.installEngine.mountSelectedISO()
            self.installEngine.formatDrive()
        else:
            return


    def moveToConfirmation(self, data_pipe):  # handle inputs from hosted frame
        print("RECEIVED: ", data_pipe)

        if data_pipe["selectedDisk"] != '' and data_pipe["selectedISO"] != None:
            self.selectedDrive = data_pipe["selectedDisk"].split()
            self.selectedDrive = self.selectedDrive[0]
            self.selectedISO = data_pipe["selectedISO"]
        else:
            showerror(title="Error", message="Error, please input required information")
            return

        self.runConfirmationNotification()
        
    def renderLogo(self, master):
        image = Image.open("logo.png")
        resized_image = image.resize((70, 70))
        self.img = ImageTk.PhotoImage(resized_image)
        logo_image_label = Label(
            master, image=self.img, highlightthickness=0, borderwidth=0
        )
        logo_image_label.grid(row=0, column=1, sticky="w", pady=10)
        txt = Label(master, text="BitInstaller " + __version__, background="#232729")
        txt.config(font=("Helvetica bold", 26))
        txt.grid(row=0, column=1, sticky="e")

if __name__ == '__main__':
    BitInstaller().mainloop()
