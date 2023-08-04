from tkinter import IntVar, Canvas, Label
from tkinter.ttk import Progressbar
from tkinter import ARC


class RoundedRectangle(Canvas):
    def __init__(self, master, x1, y1, x2, y2, corner_radius, **kwargs):
        super().__init__(master, **kwargs)
        self.createRoundedRectangle(master, x1, y1, x2, y2, corner_radius, **kwargs)

    def createRoundedRectangle(self, master, x1, y1, x2, y2, corner_radius, **kwargs):
        self.create_arc(
            x1,
            y1,
            x1 + 2 * corner_radius,
            y1 + 2 * corner_radius,
            start=90,
            extent=90,
            style=ARC,
        )
        self.create_arc(
            x2 - 2 * corner_radius,
            y1,
            x2,
            y1 + 2 * corner_radius,
            start=0,
            extent=90,
            style=ARC,
        )
        self.create_arc(
            x1,
            y2 - 2 * corner_radius,
            x1 + 2 * corner_radius,
            y2,
            start=180,
            extent=90,
            style=ARC,
        )
        self.create_arc(
            x2 - 2 * corner_radius,
            y2 - 2 * corner_radius,
            x2,
            y2,
            start=270,
            extent=90,
            style=ARC,
        )

        self.create_line(x1 + corner_radius, y1, x2 - corner_radius, y1)
        self.create_line(x1 + corner_radius, y2, x2 - corner_radius, y2)
        self.create_line(x1, y1 + corner_radius, x1, y2 - corner_radius)
        self.create_line(x2, y1 + corner_radius, x2, y2 - corner_radius)

        return self


class CleanProgressBar(Progressbar):
    def __init__(self, master):
        super().__init__(master)
        self.progress = IntVar(value=0)
        self.percentage = Label(master, textvariable=self.progress)
        self.progressbar = Progressbar(
            master,
            orient="horizontal",
            length=400,
            mode="determinate",
            variable=self.progress,
        )
        self.configure()
        number_label = Label(master, textvariable=self.progress)
        number_label.configure(bg="#0E0E0E")
        number_label.grid(row=1, column=0, padx=0, pady=0, sticky="e")

    def configure(self):
        self.percentage.configure(bg="#0E0E0E")
        #self.percentage.pack(side='left')
        self.progressbar.grid(row=1, column=1, padx=0, pady=0)
        #self.master.place(relx=0.5, rely=1,anchor="s")
    
    def updateProgressBar(self, amount):
        self.progress.set(amount)