from tkinter import *
import ES
from tkinter import messagebox
import DepartmentAcademic

class DepartmentCoursesView:
    def __init__(self, root):

        root.title('Academics - Courses')
        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.course_label_DepartmentCourses = Label(self.frame, text='Course Name', fg="black")
        self.course_entry_DepartmentCourses = Entry(self.frame, borderwidth=0)

        # TODO
        # Semester Based Query
        # self.roll_label_DepartmentCourses = Label(self.frame, text='Roll No', fg="black")
        # self.roll_entry_DepartmentCourses = Entry(self.frame, borderwidth=0)

        self.submit_button_DepartmentCourses= Button(self.frame, text='Search', command=lambda :self.search_command_DepartmentCourses(root))

        self.display_frame_CourseView = Frame(self.frame)
        self.course_label_DepartmentCourses.grid(row=2, column=0, padx=5, pady=3)
        self.course_entry_DepartmentCourses.grid(row=2, column=1)
        # self.roll_label_DepartmentCourses.grid(row=3, column=0, padx=5, pady=3)
        # self.roll_entry_DepartmentCourses.grid(row=3, column=1)


        self.exit_button_Department = Button(self.frame, text="Exit", command=exit)
        self.back_button_Department = Button(self.frame, text="Back",
                                             command=lambda: self.back_command_DepartmentCourses(root))

        self.submit_button_DepartmentCourses.grid(row=4, column=0,columnspan=2,pady=20)
        self.display_frame_CourseView.grid(row=5, column=0,columnspan=2)

        self.exit_button_Department.grid(row=8, column=0, pady=50, padx=50, sticky=S + W)
        self.back_button_Department.grid(row=8, column=1, pady=50, padx=50,  sticky=S + E)



        # self.frame.rowconfigure(2, weight=1)
        # self.frame.rowconfigure(3, weight=1)
        #
        self.frame.rowconfigure(8, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()


    def display_students(self, root, list_):
        # TODO
        # Add scroll bar
        # Fix Width
        # Fix exit and back button
        # textbox_text_StudentView = Text(self.display_frame_DepartmentCourses)
        # textbox_text_StudentView.grid(row=1, column=0)
        self.display_frame_DepartmentCourses.destroy()
        self.display_frame_DepartmentCourses = Frame(self.frame)
        self.display_frame_DepartmentCourses.grid(row=5, column=0, columnspan=2)
        for i in range(len(list_)):
            studentserial_Label_DepartmentCourses = Label(self.display_frame_DepartmentCourses, anchor=W, text=i+1)
            studentrollname_Label_DepartmentCourses = Label(self.display_frame_DepartmentCourses, anchor=W, text=list_[i][0] + '    ' + list_[i][1])
            studentserial_Label_DepartmentCourses.grid(row=i,column=0, sticky=W)
            studentrollname_Label_DepartmentCourses.grid(row=i,column=1, sticky=W)
            studentrollname_Label_DepartmentCourses.bind('<Button-1>', self.viewstudentroll_popup_Command_DepartmentCourses)
            # studentname_Label_DepartmentCourses.bind('<Button-1>', self.viewstudentname_popup_Command_DepartmentCourses)


    def back_command_DepartmentCourses(self, root):
        self.clear()
        root.maxsize(800, 600)
        DepartmentAcademic.DepartmentAcademic(root)


    def search_command_DepartmentCourses(self, root):
        connect_, cursor_ = ES.get_student_db_ES()
        name_ = self.name_entry_DepartmentCourses.get()
        roll_no_ = self.roll_entry_DepartmentCourses.get()
        if name_ == "" and roll_no_ == "":
            messagebox.showwarning("ERROR", "Please enter something")
        elif roll_no_ == "":
            cursor_.execute("SELECT * FROM student WHERE student_name LIKE (:name)",{'name':'%'+name_+'%'})
        elif name_ == "":
            cursor_.execute("SELECT * FROM student WHERE roll LIKE (:roll)", {'roll':'%'+roll_no_+'%'})
        else:
            cursor_.execute("SELECT * FROM student WHERE student_name LIKE (:name) AND roll LIKE (:roll)", {'name':'%'+name_+'%', 'roll':'%'+roll_no_+'%'})
        self.display_students(root, cursor_.fetchall())

    def clear(self):
        self.frame.destroy()




if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    DepartmentCoursesView(root)