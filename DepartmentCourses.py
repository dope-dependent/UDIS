from tkinter import *
import ES
from tkinter import messagebox
import DepartmentAcademic
import CoursesNew
from ScrollableFrame import ScrollableFrame

class DepartmentCourses:
    def __init__(self, root):

        root.title('Academics - Courses')
        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.courseLabel = Label(self.frame, text='Course Name', fg="black")
        self.courseEntry = Entry(self.frame, borderwidth=0)

        # TODO
        # Semester Based Query
        

        self.submitButton= Button(self.frame, text='Search', command=lambda :self.search(root))
        self.addcoursesButton=Button(self.frame,text='Add Courses',command=lambda:self.add(root))
        self.displayFrame = Frame(self.frame)
        self.courseLabel.grid(row=2, column=0, padx=5, pady=3)
        self.courseEntry.grid(row=2, column=1)
        
        # self.roll_label_DepartmentCourses.grid(row=3, column=0, padx=5, pady=3)
        # self.roll_entry_DepartmentCourses.grid(row=3, column=1)


        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame, text="Back",
                                             command=lambda: self.back(root))

        
        self.submitButton.grid(row=4, column=0,columnspan=2,pady=20)
        self.addcoursesButton.grid(row=6,column=0,columnspan=2,pady=20)
        self.displayFrame.grid(row=7, column=0,columnspan=2)
        

        self.exitButton.grid(row=8, column=0, pady=50, padx=50, sticky=S + W)
        self.backButton.grid(row=8, column=1, pady=50, padx=50,  sticky=S+E)

        self.frame.rowconfigure(8, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()


    def display_courses(self, root, list_):
        # TODO
        # Fix Width
        
        self.displayFrame.destroy()
        self.displayFrame = Frame(self.frame)
        self.displayScrollframe=ScrollableFrame(self.displayFrame)
        self.displayScrollframe.grid(column=0,row=0,sticky="nsew")
        self.displayFrame.grid(row=5, column=0, columnspan=2)

        self.displayScrollframe.frame.columnconfigure(1,weight=1)
        for i in range(len(list_)):
            courseserialLabel = Label(self.displayScrollframe.frame, anchor=W, text=i+1)
            courserollnameLabel = Label(self.displayScrollframe.frame, anchor=W, text=list_[i][0] + '    ' + list_[i][1])
            courseserialLabel.grid(row=i,column=0, sticky=W+E,padx=5)
            courserollnameLabel.grid(row=i,column=1, sticky=W+E)
            # studentname_Label_DepartmentCourses.bind('<Button-1>', self.viewstudentname_popup_Command_DepartmentCourses)


    def back(self, root):
        self.clear()
        root.maxsize(800, 600)
        DepartmentAcademic.DepartmentAcademic(root)


    def search(self, root):
        connect_, cursor_ = ES.get_student_db_ES()
        coursename_ = self.courseEntry.get()
    
        if coursename_ == "":
            messagebox.showwarning("ERROR", "Please enter something")
        else:
            cursor_.execute("SELECT * FROM all_courses WHERE course_name LIKE (:coursename)", {'coursename':'%'+coursename_+'%'})
        self.display_courses(root, cursor_.fetchall())

    def clear(self):
        self.frame.destroy()


    def add(self, root):
        print("Add command \n")
        self.clear()
        CoursesNew.CoursesNew(root)

if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    DepartmentCourses(root)
