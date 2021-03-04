from tkinter import *
import ES

global root_

class StudentMainMenu:
    def __init__(self, root):
        root.title("UDIS - Student")


        # Only for unit testing
        #
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')
        global root_
        root_ = root

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.add_button_StudentMainMenu = Button(self.frame, text="Add New Student",
                                                 command = self.add_command_StudentMainMenu)

        self.reg_button_StudentMainMenu = Button(self.frame, text="Register Courses",
                                                 command=self.add_command_StudentMainMenu)

        self.view_button_StudentMainMenu = Button(self.frame, text="View Student",
                                                 command=self.add_command_StudentMainMenu)

        self.grade_button_StudentMainMenu = Button(self.frame, text="Enter Student Grades",
                                                 command=self.add_command_StudentMainMenu)

        self.exit_button_StudentMainMenu = Button(self.frame, text="Exit", command=exit)
        self.back_button_StudentMainMenu = Button(self.frame, text="Back", command=self.back_command_StudentMainMenu)

        self.add_button_StudentMainMenu.grid(row=0, column=0, columnspan=2)
        self.reg_button_StudentMainMenu.grid(row=1, column=0, columnspan=2)
        self.view_button_StudentMainMenu.grid(row=2, column=0, columnspan=2)
        self.grade_button_StudentMainMenu.grid(row=3, column=0, columnspan=2)

        self.exit_button_StudentMainMenu.grid(row=4, column=0)
        self.back_button_StudentMainMenu.grid(row=4, column=1)

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)

        root.mainloop()

    def back_command_StudentMainMenu(self):
        print("Back")
        self.clear()

    def add_command_StudentMainMenu(self):
        print("Add command \n")

    def clear(self):
        global root_
        self.frame.destroy()
        # self.add_button_StudentMainMenu.destroy()
        # self.reg_button_StudentMainMenu.destroy()
        # self.view_button_StudentMainMenu.destroy()
        # self.grade_button_StudentMainMenu.destroy()
        # self.exit_button_StudentMainMenu.destroy()
        # self.back_button_StudentMainMenu.destroy()
        ES.ES(root_)

if __name__ == '__main__':
    root = Tk()
    StudentMainMenu(root)