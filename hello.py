from tkinter import *

import tkinter.ttk as ttk


def defocus(event):
    event.widget.master.focus_set()
    event.widget.selection_clear()

root = Tk()

comboBox = ttk.Combobox(root, state="readonly", values=("a", "b", "c"))
comboBox.grid()
comboBox.set("a")
comboBox.bind("<FocusIn>", defocus)
# comboBox.bind('<<ComboboxSelected>>', conversion)
mainloop()