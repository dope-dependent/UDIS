from tkinter import *
import ES
import Home
import StudentsNew
import StudentsView
import StudentCourses

class StudentMain:
    def __init__(self, root):
        root.title("UDIS - Student")
        # Only for unit testing
        #
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.newButton = Button(self.frame, text="Add New Student", anchor=W,
                                                 command=lambda: self.new(root))
        self.courseButton = Button(self.frame, text="Register Courses", anchor=W,
                                                 command=lambda: self.course(root))
        self.viewButton = Button(self.frame, text="View Student", anchor=W,
                                                  command=lambda: self.view(root))
        self.gradeButton = Button(self.frame, text="Enter Student Grades", anchor=W,
                                                   command=lambda: self.new(root))
        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame, text="Back", command=lambda: self.back(root))

        self.newButton.grid(row=0, column=0, columnspan=2, sticky=E + W)
        self.courseButton.grid(row=1, column=0, columnspan=2, sticky=E + W)
        self.viewButton.grid(row=2, column=0, columnspan=2, sticky=E + W)
        self.gradeButton.grid(row=3, column=0, columnspan=2, sticky=E + W)
        self.exitButton.grid(row=4, column=0, pady=10, sticky=S)
        self.backButton.grid(row=4, column=1, pady=10, sticky=S)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)
        self.frame.rowconfigure(4, weight=1)

    def back(self, root):
        print("Back")
        self.clear()
        Home.Home(root)

    def new(self, root):
        print("Add command \n")
        self.clear()
        StudentsNew.StudentNew(root)

    def view(self, root):
        print("View command \n")
        self.clear()
        StudentsView.StudentsView(root)

    def course(self, root):
        self.clear()
        StudentCourses.StudentCourses(root)

    def clear(self):
        self.frame.destroy()



if __name__ == '__main__':
    root = Tk()
    StudentMain(root)