themeConfig = {
    "TCombobox": {
        "fieldbackground": "#232729",
        "foreground": "white",
        "background": "#232729",
        "focusfill": "#232729",
        "arrowcolor": "white",
        "darkcolor": "#232729",
        "selectbackground": "#232729",
        "lightcolor": "#232729",
        "bordercolor": "#232729",
    },
    "TScrollbar": {
        "troughcolor": "#232729",
        "bordercolor": "#232729",
        "background": "#232729",
        "arrowcolor": "#232729",
        "gripcount": 0,
        "bordercolor": "#232729",
        "darkcolor": "#232729",
        "lightcolor": "#232729",
    },
    "Horizontal.TProgressbar": {
        "troughcolor": "#232729",
        "background": "#1E90FF",
        "bordercolor": "#232729",
        "lightcolor": "#232729",
        "darkcolor": "#232729",
    },
}

UIRectdata = {
    "x1": 60,
    "y1": 80,
    "x2": 230,
    "y2": 120,
    "corner_radius": 7,
    "bg": "#232729",
    "highlightbackground": "#232729",
    "highlightcolor": "#232729",
    "outline": "#499BD8"
}

InvisibleUIRectdata = {
    "x1": 60,
    "y1": 80,
    "x2": 230,
    "y2": 120,
    "corner_radius": 7,
    "bg": "#232729",
    "highlightbackground": "#232729",
    "highlightcolor": "#232729",
    "outline": "#232729"
}

scrollbarLayout = (
    "TScrollbar",
    [
        (
            "Scrollbar.trough",
            {
                "children": [("Scrollbar.thumb", {"expand": "1", "sticky": "nswe"})],
                "sticky": "nswe",
            },
        )
    ],
)

comboboxLayout = (
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
