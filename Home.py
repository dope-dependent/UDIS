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

        self.student_b_Home = Button(self.frame, text='  Student  ', command=lambda : self.student_command_Home(root))
        self.student_b_Home.grid(row=1, column=0, sticky='nsew')

        self.dep_b_Home = Button(self.frame, text='Department', command=lambda : self.dep_command_Home(root))
        self.dep_b_Home.grid(row=1, column=1, sticky='nsew')



        self.exit_b_Home = Button(self.frame, text="Exit", command=exit)
        self.back_b_Home = Button(self.frame, text="Back",
                                                  command=lambda: self.back_command_Home(root))

        self.exit_b_Home.grid(row=4, column=0, pady=10, sticky=S)
        self.back_b_Home.grid(row=4, column=1, pady=10, sticky=S)

        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

    def student_command_Home(self, root):
        self.clear()
        StudentsUDIS.StudentMainMenu(root)

    def dep_command_Home(self, root):
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
