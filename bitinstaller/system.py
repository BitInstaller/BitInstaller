from tkinter.filedialog import askopenfile


def getFileLocation():
    return askopenfile(mode="r", title="Select ISO").name
