from tkinter import *
import ES
import StudentsUDIS
import DepartmentUDIS

class Home:
    def __init__(self, root):

        root.title("Homepage")

        self.frame = Frame(root, bg="white")
        # self.frame.pack(fill=BOTH, expand=True)
        self.frame.grid(row=0, column=0, sticky='nsew')
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')

        self.student_button_Home = Button(self.frame, text='  Student  ', command=lambda : self.student_command_Home(root))
        self.student_button_Home.grid(row=1, column=0, sticky='nsew')

        self.department_button_Home = Button(self.frame, text='Department', command=lambda : self.department_command_Home(root))
        self.department_button_Home.grid(row=1, column=1, sticky='nsew')



        self.exit_button_Home = Button(self.frame, text="Exit", command=exit)
        self.back_button_Home = Button(self.frame, text="Back",
                                                  command=lambda: self.back_command_Home(root))

        self.exit_button_Home.grid(row=4, column=0, pady=10, sticky=S)
        self.back_button_Home.grid(row=4, column=1, pady=10, sticky=S)

        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

    def student_command_Home(self, root):
        self.clear()
        StudentsUDIS.StudentMainMenu(root)

    def department_command_Home(self, root):
        self.clear()
        DepartmentUDIS.DepartmentMainMenu(root)

    def back_command_Home(self, root):
        self.clear()
        ES.ES(root)

    def clear(self):
        self.frame.destroy()

if __name__ == '__main__':
    root = Tk()
    Home(root)
