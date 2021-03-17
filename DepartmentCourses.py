from tkinter import *
import ES
from tkinter import messagebox
import DepartmentAcademic
import CoursesNew
from ScrollableFrame import ScrollableFrame

class DepartmentCoursesView:
    def __init__(self, root):

        root.title('Academics - Courses')
        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.course_label_DepartmentCourses = Label(self.frame, text='Course Name', fg="black")
        self.course_entry_DepartmentCourses = Entry(self.frame, borderwidth=0)

        # TODO
        # Semester Based Query
        

        self.submit_button_DepartmentCourses= Button(self.frame, text='Search', command=lambda :self.search_command_DepartmentCourses(root))
        self.add_courses_button_DepartmentCourses=Button(self.frame,text='Add Courses',command=lambda:self.add_command_DepartmentCourses(root))
        self.display_frame_DepartmentCourses = Frame(self.frame)
        self.course_label_DepartmentCourses.grid(row=2, column=0, padx=5, pady=3)
        self.course_entry_DepartmentCourses.grid(row=2, column=1)
        
        # self.roll_label_DepartmentCourses.grid(row=3, column=0, padx=5, pady=3)
        # self.roll_entry_DepartmentCourses.grid(row=3, column=1)


        self.exit_button_Department = Button(self.frame, text="Exit", command=exit)
        self.back_button_Department = Button(self.frame, text="Back",
                                             command=lambda: self.back_command_DepartmentCourses(root))

        
        self.submit_button_DepartmentCourses.grid(row=4, column=0,columnspan=2,pady=20)
        self.add_courses_button_DepartmentCourses.grid(row=6,column=0,columnspan=2,pady=20)
        self.display_frame_DepartmentCourses.grid(row=7, column=0,columnspan=2)
        

        self.exit_button_Department.grid(row=8, column=0, pady=50, padx=50, sticky=S + W)
        self.back_button_Department.grid(row=8, column=1, pady=50, padx=50,  sticky=S + E)



        # self.frame.rowconfigure(2, weight=1)
        # self.frame.rowconfigure(3, weight=1)
        #
        self.frame.rowconfigure(8, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()


    def display_courses(self, root, list_):
        # TODO
        # Add scroll bar
        # Fix Width
        # Fix exit and back button
        # textbox_text_StudentView = Text(self.display_frame_DepartmentCourses)
        # textbox_text_StudentView.grid(row=1, column=0)
        self.display_frame_DepartmentCourses.destroy()
        self.display_frame_DepartmentCourses = Frame(self.frame)
        self.display_scrollframe_DepartmentCourses=ScrollableFrame(self.display_frame_DepartmentCourses)
        self.display_scrollframe_DepartmentCourses.grid(column=0,row=0,sticky="nsew")
        self.display_frame_DepartmentCourses.grid(row=5, column=0, columnspan=2)
        for i in range(len(list_)):
            courseserial_Label_DepartmentCourses = Label(self.display_scrollframe_DepartmentCourses.scrollable_frame, anchor=W, text=i+1)
            courserollname_Label_DepartmentCourses = Label(self.display_scrollframe_DepartmentCourses.scrollable_frame, anchor=W, text=list_[i][0] + '    ' + list_[i][1])
            courseserial_Label_DepartmentCourses.grid(row=i,column=0, sticky=W)
            courserollname_Label_DepartmentCourses.grid(row=i,column=1, sticky=W)
            # studentname_Label_DepartmentCourses.bind('<Button-1>', self.viewstudentname_popup_Command_DepartmentCourses)


    def back_command_DepartmentCourses(self, root):
        self.clear()
        root.maxsize(800, 600)
        DepartmentAcademic.DepartmentAcademic(root)


    def search_command_DepartmentCourses(self, root):
        connect_, cursor_ = ES.get_student_db_ES()
        coursename_ = self.course_entry_DepartmentCourses.get()
    
        if coursename_ == "":
            messagebox.showwarning("ERROR", "Please enter something")
        else:
            cursor_.execute("SELECT * FROM all_courses WHERE course_name LIKE (:coursename)", {'coursename':'%'+coursename_+'%'})
        self.display_courses(root, cursor_.fetchall())

    def clear(self):
        self.frame.destroy()


    def add_command_DepartmentCourses(self, root):
        print("Add command \n")
        self.clear()
        CoursesNew.CoursesNew(root)

if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    DepartmentCoursesView(root)
