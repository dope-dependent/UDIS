from tkinter import *
import ES
import Home
import DepartmentUDIS
import DepartmentCourses
import DepartmentProject
import DepartmentPublication

global root_

class DepartmentAcademic:
    def __init__(self, root):
        root.title("Department - Academics")
        # Only for unit testing
        #
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.projectButton = Button(self.frame, text="Research Projects",anchor=W,
                                                 command = lambda: self.project(root))

        self.publicationsButton = Button(self.frame, text="Research Publications",anchor=W,
                                                 command= lambda: self.publications(root))

        self.coursesButton = Button(self.frame, text="Courses Offered",anchor=W,
                                                 command=lambda: self.courses(root))

        self.facultyButton = Button(self.frame, text="Our ""ESTEEMED"" xD Faculty", anchor=W,
                                                             command=lambda: self.faculty(
                                                                 root))

        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame,
                                                    text="Back",
                                                    command=lambda:self.back(root))

        self.projectButton.grid(row=0, column=0, columnspan=2,sticky=E+W)
        self.publicationsButton.grid(row=1, column=0, columnspan=2,sticky=E+W)
        self.coursesButton.grid(row=2, column=0, columnspan=2,sticky=E+W)
        self.facultyButton.grid(row=3, column=0, columnspan=2, sticky=E+W)

        self.exitButton.grid(row=4, column=0,pady=10,sticky=S)
        self.backButton.grid(row=4, column=1,pady=10,sticky=S)
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)
        self.frame.rowconfigure(4, weight=0)

        # root.mainloop()

    def back(self,root):
        print("Back")
        self.clear()
        DepartmentUDIS.DepartmentMainMenu(root)

    def project(self, root):
        print("Project command")
        self.clear()
        DepartmentProject.DepartmentProject(root)

    def publications(self, root):
        print("Publication command")
        self.clear()
        DepartmentPublication.DepartmentPublication(root)

    def courses(self, root):
        print("Courses command")
        self.clear()
        DepartmentCourses.DepartmentCourses(root)

    def faculty(self, root):
        print("Faculty command")
        # self.clear()


    def clear(self):
        self.frame.destroy()

if __name__ == '__main__':
    root = Tk()
    DepartmentAcademic(root)