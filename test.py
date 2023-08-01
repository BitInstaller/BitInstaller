import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.geometry("300x200")

# Create a custom style for the Combobox
style = ttk.Style()
style.theme_use("clam")
style.theme_create("my_custom_style", parent="alt", settings={
    "TCombobox": {
        "configure": {"selectbackground": "#0E0E0E", "fieldbackground": "#0E0E0E"},
        "map": {
            "background": [("readonly", "#0E0E0E"), ("!disabled", "#0E0E0E")],
            "foreground": [("readonly", "#0E0E0E"), ("!disabled", "#0E0E0E")]
        }
    },
    "TScrollbar": {
        "configure": {"troughcolor": "#0E0E0E", "bordercolor": "#0E0E0E", "background": "#0E0E0E"}
    }
})
style.theme_use("my_custom_style")


# Create a Combobox using the custom style
listbox = ttk.Combobox(
    root,
    height=10,
    width=15,
    style="TCombobox",
)
listbox.pack()

# Add some items to the Combobox
listbox["values"] = ("Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 5", "Item 5", "Item 5", "Item 5", "Item 5", "Item 5", "Item 5", "Item 5")

root.mainloop()
