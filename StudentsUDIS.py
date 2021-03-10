from tkinter import *
import ES
import Home
import StudentsNew
import StudentsView

global root_

class StudentMainMenu:
    def __init__(self, root):
        root.title("UDIS - Student")
        # Only for unit testing
        #
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.add_button_StudentMainMenu = Button(self.frame, text="Add New Student",anchor=W,
                                                 command = lambda: self.add_command_StudentMainMenu(root))

        self.reg_button_StudentMainMenu = Button(self.frame, text="Register Courses",anchor=W,
                                                 command= lambda: self.add_command_StudentMainMenu(root))

        self.view_button_StudentMainMenu = Button(self.frame, text="View Student",anchor=W,
                                                 command=lambda: self.view_command_StudentMainMenu(root))

        self.grade_button_StudentMainMenu = Button(self.frame, text="Enter Student Grades",anchor=W,
                                                 command=lambda: self.add_command_StudentMainMenu(root))

        self.exit_button_StudentMainMenu = Button(self.frame, text="Exit", command=exit)
        self.back_button_StudentMainMenu = Button(self.frame, 
                                                    text="Back", 
                                                    command=lambda:self.back_command_StudentMainMenu(root))

        self.add_button_StudentMainMenu.grid(row=0, column=0, columnspan=2,sticky=E+W)
        self.reg_button_StudentMainMenu.grid(row=1, column=0, columnspan=2,sticky=E+W)
        self.view_button_StudentMainMenu.grid(row=2, column=0, columnspan=2,sticky=E+W)
        self.grade_button_StudentMainMenu.grid(row=3, column=0, columnspan=2,sticky=E+W)

        self.exit_button_StudentMainMenu.grid(row=4, column=0,pady=10,sticky=S)
        self.back_button_StudentMainMenu.grid(row=4, column=1,pady=10,sticky=S)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)
        self.frame.rowconfigure(4, weight=1)

        # root.mainloop()

    def back_command_StudentMainMenu(self,root):
        print("Back")
        self.clear()
        Home.Home(root)

    def add_command_StudentMainMenu(self, root):
        print("Add command \n")
        self.clear()
        StudentsNew.StudentNew(root)

    def view_command_StudentMainMenu(self, root):
        print("View command \n")
        self.clear()
        StudentsView.StudentsView(root)

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
    StudentMainMenu(root)