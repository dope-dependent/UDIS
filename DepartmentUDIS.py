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

        self.inventory_button_StudentMainMenu = Button(self.frame, text="Manage Inventory",anchor=W,
                                                 command = lambda: self.inventory_command_StudentMainMenu(root))

        self.academics_button_StudentMainMenu = Button(self.frame, text="Academic Sexon",anchor=W,
                                                 command= lambda: self.academics_command_StudentMainMenu(root))

        self.accounts_button_StudentMainMenu = Button(self.frame, text="Account Details",anchor=W,
                                                 command=lambda: self.accounts_command_StudentMainMenu(root))

        self.exit_button_StudentMainMenu = Button(self.frame, text="Exit", command=exit)
        self.back_button_StudentMainMenu = Button(self.frame,
                                                    text="Back",
                                                    command=lambda:self.back_command_DepartmentMainMenu(root))

        self.inventory_button_StudentMainMenu.grid(row=0, column=0, columnspan=2,sticky=E+W)
        self.academics_button_StudentMainMenu.grid(row=1, column=0, columnspan=2,sticky=E+W)
        self.accounts_button_StudentMainMenu.grid(row=2, column=0, columnspan=2,sticky=E+W)

        self.exit_button_StudentMainMenu.grid(row=3, column=0,pady=10,sticky=S)
        self.back_button_StudentMainMenu.grid(row=3, column=1,pady=10,sticky=S)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)

        root.mainloop()

    def back_command_DepartmentMainMenu(self,root):
        print("Back")
        self.clear()
        Home.Home(root)

    def inventory_command_StudentMainMenu(self, root):
        print("Inventory command")
        self.clear()
        # StudentsNew.StudentNew(root)

    def academics_command_StudentMainMenu(self, root):
        print("Academics command \n")
        self.clear()
        DepartmentAcademic.DepartmentAcademic(root)

    def accounts_command_StudentMainMenu(self, root):
        print("Account command \n")
        self.clear()
        # StudentsView.StudentsView(root)

    def clear(self):
        global root_
        self.frame.destroy()
        # self.add_button_StudentMainMenu.destroy()
        # self.reg_button_StudentMainMenu.destroy()
        # self.view_button_StudentMainMenu.destroy()
        # self.grade_button_StudentMainMenu.destroy()
        # self.exit_button_StudentMainMenu.destroy()
        # self.back_button_StudentMainMenu.destroy()

if __name__ == '__main__':
    root = Tk()
    DepartmentMainMenu(root)