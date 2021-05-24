from tkinter import *
import DepartmentAcademic
from ScrollableFrame import ScrollableFrame

class DepartmentResearch:
    def __init__(self, root):

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.newButton = Button(self.frame, text="Add...", command=lambda:self.new(root))
        self.displayAll = ScrollableFrame(self.frame)

        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame, text="Back", command=lambda: self.back(root))

        self.newButton.grid(row=1, column=0, padx=50, pady = 50, columnspan=2)
        self.displayAll.grid(row=2, column=0, columnspan=2)
        self.exitButton.grid(row=3, column=0, padx=50, pady = 50, sticky=S + W)
        self.backButton.grid(row=3, column=0, padx=50, pady = 50, sticky=S + E)

        self.frame.columnconfigure(0, weight=1)

    def bindingAction(self, event):
        pass

    def new(self, root):
        pass

    def back(self, root):
        self.clear()
        root.maxsize(1200,900)
        DepartmentAcademic.DepartmentAcademic(root)

    def clear(self):
        self.frame.destroy()

