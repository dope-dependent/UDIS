from tkinter import *
import ES
import Home
import DepartmentAcademic

global root_

class DepartmentMainMenu:
    def __init__(self, root):
        root.title("UDIS - Department")
        # Only for unit testing
        #
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.inventoryButton = Button(self.frame, text="Manage Inventory",anchor=W,
                                                 command = lambda: self.inventory(root))

        self.academicsButton = Button(self.frame, text="Academic Sexon",anchor=W,
                                                 command= lambda: self.academics(root))

        self.accountsButton = Button(self.frame, text="Account Details",anchor=W,
                                                 command=lambda: self.accounts(root))

        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame,
                                                    text="Back",
                                                    command=lambda:self.back(root))

        self.inventoryButton.grid(row=0, column=0, columnspan=2,sticky=E+W)
        self.academicsButton.grid(row=1, column=0, columnspan=2,sticky=E+W)
        self.accountsButton.grid(row=2, column=0, columnspan=2,sticky=E+W)

        self.exitButton.grid(row=3, column=0,pady=10,sticky=S)
        self.backButton.grid(row=3, column=1,pady=10,sticky=S)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)

        root.mainloop()

    def back(self,root):
        self.clear()
        Home.Home(root)

    def inventory(self, root):
        print("Inventory command")
        self.clear()
        

    def academics(self, root):
        self.clear()
        DepartmentAcademic.DepartmentAcademic(root)

    def accounts(self, root):
        print("Account command \n")
        self.clear()
        

    def clear(self):
        self.frame.destroy()
       
if __name__ == '__main__':
    root = Tk()
    DepartmentMainMenu(root)