import tkinter as tk
from tkinter import ttk, NSEW, NS, PhotoImage, Label
from tkinter.ttk import Combobox
import time

root = tk.Tk()
root.configure(bg="#0E0E0E")


class RoundedRectangle(tk.Canvas):
    def __init__(self, master, x1, y1, x2, y2, corner_radius, **kwargs):
        super().__init__(master, **kwargs)

        self.create_arc(
            x1,
            y1,
            x1 + 2 * corner_radius,
            y1 + 2 * corner_radius,
            start=90,
            extent=90,
            style=tk.ARC,
        )
        self.create_arc(
            x2 - 2 * corner_radius,
            y1,
            x2,
            y1 + 2 * corner_radius,
            start=0,
            extent=90,
            style=tk.ARC,
        )
        self.create_arc(
            x1,
            y2 - 2 * corner_radius,
            x1 + 2 * corner_radius,
            y2,
            start=180,
            extent=90,
            style=tk.ARC,
        )
        self.create_arc(
            x2 - 2 * corner_radius,
            y2 - 2 * corner_radius,
            x2,
            y2,
            start=270,
            extent=90,
            style=tk.ARC,
        )

        self.create_line(x1 + corner_radius, y1, x2 - corner_radius, y1)
        self.create_line(x1 + corner_radius, y2, x2 - corner_radius, y2)
        self.create_line(x1, y1 + corner_radius, x1, y2 - corner_radius)
        self.create_line(x2, y1 + corner_radius, x2, y2 - corner_radius)

        self.grid(row=0, column=0)


rounded_rect = RoundedRectangle(
    root,
    60,
    80,
    230,
    120,
    7,
    bg="#0E0E0E",
    highlightbackground="#0E0E0E",
    highlightcolor="#0E0E0E",
)
rounded_rect.grid(row=0, column=0)


select_rect = RoundedRectangle(
    root,
    60,
    80,
    230,
    120,
    7,
    bg="#0E0E0E",
    highlightbackground="#0E0E0E",
    highlightcolor="#0E0E0E",
)
select_rect.grid(row=0, column=1)
l = Label(root, text = "Select File", bg="#0E0E0E")
l.config(font =("Courier", 14))
l.grid(row=0, column=1)

flash_rect = RoundedRectangle(
    root,
    60,
    80,
    230,
    120,
    7,
    bg="#0E0E0E",
    highlightbackground="#0E0E0E",
    highlightcolor="#0E0E0E",
)
flash_rect.grid(row=0, column=2)
ll = Label(root, text = "Flash!", bg="#0E0E0E")
ll.config(font =("Courier", 14))
ll.grid(row=0, column=2)

stl = ttk.Style()

# standerd theme
stl.theme_use("clam")
stl.configure(
    "TCombobox",
    fieldbackground="#0E0E0E",
    foreground="white",
    background="#0E0E0E",
    focusfill="#0E0E0E",
    arrowcolor="white",
    darkcolor="#0E0E0E",
    selectbackground="#0E0E0E",
    lightcolor="#0E0E0E",
    bordercolor="#0E0E0E",
)

stl.layout(
    "Mystyle.TCombobox",
    [
        (
            "Combobox.field",
            {
                "sticky": "NSEW",
                "children": [
                    (
                        "Mystyle.TCombobox.downarrow",
                        {
                            "side": "right",
                            "sticky": "",
                        },
                    ),
                    (
                        "Combobox.padding",
                        {
                            "expand": "1",
                            "sticky": "NSEW",
                            "children": [
                                (
                                    "Combobox.textarea",
                                    {
                                        "sticky": "NSEW",
                                    },
                                ),
                            ],
                        },
                    ),
                ],
            },
        ),
    ],
)


stl.map("TCombobox", background=[("active", "#0E0E0E")], arrowsize=[("active", 15)])


root.option_add("*TCombobox*Listbox.selectBackground", "#0E0E0E")

# create listbox object
listbox = Combobox(
    root,
    height=10,
    width=15,
    style="Mystyle.TCombobox",
)

root.option_add("*TCombobox*Listbox.background", "#0E0E0E")

listbox.configure(background="#0E0E0E")

listbox["values"] = (
    " January",
    " February",
    " March",
    " April",
    " May",
    " June",
    " July",
    " August",
    " September",
    " October",
    " November",
    " December",
)
listbox.current()

listbox.grid(row=0, column=0)

root.mainloop()
