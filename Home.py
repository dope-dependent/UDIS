from tkinter import *
import ES
import StudentMain
import DepartmentUDIS

class Home:
    def __init__(self, root):

        root.title("UDIS - Homepage")
        self.frame = Frame(root, bg="white")

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.studentButton = Button(self.frame, text='  Student  ', command=lambda : self.student(root))
        self.studentButton.grid(row=1, column=0, sticky='nsew')

        self.departmentButton = Button(self.frame, text='Department', command=lambda : self.department(root))
        self.departmentButton.grid(row=1, column=1, sticky='nsew')

        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame, text="Back", command=lambda: self.back(root))

        self.exitButton.grid(row=4, column=0, pady=10, sticky=S)
        self.backButton.grid(row=4, column=1, pady=10, sticky=S)

        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

    def student(self, root):
        self.clear()
        StudentMain.StudentMain(root)

    def department(self, root):
        self.clear()
        DepartmentUDIS.DepartmentMainMenu(root)

    def back(self, root):
        self.clear()
        ES.ES(root)

    def clear(self):
        self.frame.destroy()

if __name__ == '__main__':
    root = Tk()
    Home(root)
