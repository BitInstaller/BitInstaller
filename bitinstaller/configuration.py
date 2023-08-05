from bitinstaller.layout import themeConfig
from bitinstaller.layout import comboboxLayout
from bitinstaller.layout import scrollbarLayout

class TkGraphicsConfig:
    def __init__(self, master, style):
        style.layout(*comboboxLayout)
        style.layout(*scrollbarLayout)
        style.theme_use("clam")
        style.configure("TCombobox", **themeConfig["TCombobox"])
        style.configure(
            "Horizontal.TProgressbar", **themeConfig["Horizontal.TProgressbar"]
        )
        master.option_add("*TCombobox*Listbox.selectBackground" % master, "#499BD8")
        master.option_add("*TCombobox*Listbox.background" % master, "#232729")
        style.map(
            "TScrollbar",
            # Apply the same settings for normal, active, and hover states
            background=[("active", "#454545"), ("!active", "#454545")],
            arrowcolor=[("active", "#232729"), ("!active", "#232729")],
            gripcount=[("active", 0), ("!active", 0)],
            troughcolor=[("active", "#232729"), ("!active", "#232729")],
            bordercolor=[("active", "#454545"), ("!active", "#454545")],
            darkcolor=[("active", "#454545"), ("!active", "#454545")],
            lightcolor=[("active", "#454545"), ("!active", "#454545")],
        )
        style.map("TCombobox", background=[("active", "#232729")], arrowsize=[("active", 15)])
