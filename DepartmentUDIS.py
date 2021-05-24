from tkinter import *
import ES
import Home
import DepartmentAcademic
import DepartmentAccount
import DepartmentInventory

global root_

class DepartmentMainMenu:
    def __init__(self, root):
        root.title("UDIS - Department")
        root.geometry('800x600')
        root.minsize(800, 600)
        root.maxsize(800, 600)

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.inventoryButton = Button(self.frame, text="Manage Inventory",anchor=W,
                                                 command = lambda: self.inventory(root))

        self.academicsButton = Button(self.frame, text="Academic Section",anchor=W,
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
        self.frame.rowconfigure(3, weight=1)

        root.mainloop()

    def back(self,root):
        self.clear()
        Home.Home(root)

    def inventory(self, root):
        self.clear()
        DepartmentInventory.DepartmentInventory(root)
        

    def academics(self, root):
        self.clear()
        DepartmentAcademic.DepartmentAcademic(root)

    def accounts(self, root):
        self.clear()
        DepartmentAccount.DepartmentAccount(root)

    def clear(self):
        self.frame.destroy()
       
if __name__ == '__main__':
    root = Tk()
    DepartmentMainMenu(root)