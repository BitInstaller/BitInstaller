themeConfig = {
    "TCombobox": {
        "fieldbackground": "#0E0E0E",
        "foreground": "white",
        "background": "#0E0E0E",
        "focusfill": "#0E0E0E",
        "arrowcolor": "white",
        "darkcolor": "#0E0E0E",
        "selectbackground": "#0E0E0E",
        "lightcolor": "#0E0E0E",
        "bordercolor": "#0E0E0E",
    }
}

UIRectdata = {
    "x1": 60,
    "y1": 80,
    "x2": 230,
    "y2": 120,
    "corner_radius": 7,
    "bg":"#0E0E0E",
    "highlightbackground":"#0E0E0E",
    "highlightcolor":"#0E0E0E",
}


themeLayout = (
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

