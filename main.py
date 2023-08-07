import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from bitinstaller.frames.StartupFrame import StartupFrame

__author__ = "SGK"
__license__ = "MIT"
__version__ = "v0.1-0"
__status__ = "Development"

class BitInstaller(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        super().__init__()
        self.title("BitInstaller " + __version__)
        self.configure(bg="#232729")
        startDisplayFrame = Frame(self)

        exportedData = {}

        # Logo
        image = Image.open("logo.png")
        resize_image = image.resize((70, 70))
        img = ImageTk.PhotoImage(resize_image)
        logoImageLabel = Label(
            startDisplayFrame, image=img, highlightthickness=0, borderwidth=0
        )
        logoImageLabel.grid(row=0, column=1, sticky="w", pady=10)
        txt = Label(startDisplayFrame, text="BitInstaller " + __version__, background="#232729")
        txt.config(font=("Helvetica bold", 26))
        txt.grid(row=0, column=1, sticky="e")
        # Logo


        x = StartupFrame(startDisplayFrame, self.receiveExportData)

        startDisplayFrame.grid()

        startDisplayFrame.mainloop()

    def receiveExportData(data):
        print("RECEVED: " + data)

if __name__ == '__main__':
    BitInstaller()