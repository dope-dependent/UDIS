from tkinter import *
import ES
import Home
import DepartmentUDIS
import DepartmentCourses

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

        self.project_button_DepartmentAcademics = Button(self.frame, text="Research Projects",anchor=W,
                                                 command = lambda: self.project_command_DepartmentAcademics(root))

        self.publications_button_DepartmentAcademics = Button(self.frame, text="Research Publications",anchor=W,
                                                 command= lambda: self.publications_command_DepartmentAcademics(root))

        self.courses_offered_button_DepartmentAcademics = Button(self.frame, text="Courses Offered",anchor=W,
                                                 command=lambda: self.courses_offered_command_DepartmentAcademics(root))

        self.faculty_button_DepartmentAcademics = Button(self.frame, text="Our ""ESTEEMED"" xD Faculty", anchor=W,
                                                             command=lambda: self.faculty_command_DepartmentAcademics(
                                                                 root))

        self.exit_button_DepartmentAcademics = Button(self.frame, text="Exit", command=exit)
        self.back_button_DepartmentAcademics = Button(self.frame,
                                                    text="Back",
                                                    command=lambda:self.back_command_DepartmentAcademics(root))

        self.project_button_DepartmentAcademics.grid(row=0, column=0, columnspan=2,sticky=E+W)
        self.publications_button_DepartmentAcademics.grid(row=1, column=0, columnspan=2,sticky=E+W)
        self.courses_offered_button_DepartmentAcademics.grid(row=2, column=0, columnspan=2,sticky=E+W)
        self.faculty_button_DepartmentAcademics.grid(row=3, column=0, columnspan=2, sticky=E+W)

        self.exit_button_DepartmentAcademics.grid(row=4, column=0,pady=10,sticky=S)
        self.back_button_DepartmentAcademics.grid(row=4, column=1,pady=10,sticky=S)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)
        self.frame.rowconfigure(4, weight=0)

        # root.mainloop()

    def back_command_DepartmentAcademics(self,root):
        print("Back")
        self.clear()
        DepartmentUDIS.DepartmentMainMenu(root)

    def project_command_DepartmentAcademics(self, root):
        print("Project command")
        # self.clear()
        # StudentsNew.StudentNew(root)

    def publications_command_DepartmentAcademics(self, root):
        print("Publication command \n")
        # self.clear()
        # StudentsView.StudentsView(root)

    def courses_offered_command_DepartmentAcademics(self, root):
        print("Courses command \n")
        self.clear()
        DepartmentCourses.DepartmentCoursesView(root)

    def faculty_command_DepartmentAcademics(self, root):
        print("Faculty command \n")
        # self.clear()
        # StudentsView.StudentsView(root)

    def clear(self):
        global root_
        self.frame.destroy()

if __name__ == '__main__':
    root = Tk()
    DepartmentAcademic(root)