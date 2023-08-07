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
        super().__init__()
        self.title("BitInstaller " + __version__)
        self.configure(bg="#232729")

        self.configureUI()

    def configureUI(self):
        start_display_frame = Frame(self)

        # Logo
        image = Image.open("logo.png")
        resized_image = image.resize((70, 70))
        self.img = ImageTk.PhotoImage(resized_image)
        logo_image_label = Label(
            start_display_frame, image=self.img, highlightthickness=0, borderwidth=0
        )
        logo_image_label.grid(row=0, column=1, sticky="w", pady=10)
        txt = Label(start_display_frame, text="BitInstaller " + __version__, background="#232729")
        txt.config(font=("Helvetica bold", 26))
        txt.grid(row=0, column=1, sticky="e")
        # Logo

        StartupFrame(start_display_frame, self.receiveDataFromPipe)

        start_display_frame.grid()

    def receiveDataFromPipe(self, data_pipe):  # handle inputs from hosted frame
        print("RECEIVED: ", data_pipe)

if __name__ == '__main__':
    BitInstaller().mainloop()
