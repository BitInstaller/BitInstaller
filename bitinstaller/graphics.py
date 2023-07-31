from tkinter import Canvas
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