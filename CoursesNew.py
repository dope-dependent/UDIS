from tkinter import *
import DepartmentCourses
import Home
import tkinter.ttk as ttk
import ES
import sqlite3
from tkinter import messagebox

def dropdown_defocus_CoursesNew(event):
    event.widget.selection_clear()


class CoursesNew:
    def __init__(self, root):
               
        self.parent = Frame(root)
        self.parent.grid(row=0, column=0, sticky='nsew')
       
        self.rightpad = Frame(self.parent, bg="white")
        self.leftpad = Frame(self.parent, bg="white")
        self.bottomholder=Frame(self.parent, bg="white")
        self.frame = Frame(self.parent,bg="white")

        self.rightpad.grid(row=0,column=0,sticky='nsew',rowspan=2)
        self.leftpad.grid(row=0,column=2,sticky='nsew',rowspan=2)
        self.bottomholder.grid(row=1,column=1,columnspan=3,sticky='nsew')
        self.frame.grid(row=0, column=1, sticky='nsew')
        
        self.parent.rowconfigure(0,weight=1)
        self.parent.columnconfigure(0,weight=1)
        self.parent.columnconfigure(2,weight=1)
        # root.minsize(400, 300)
        root.maxsize(400, 400)
        # root.geometry('800x600')

        self.coursecode_label_CoursesNew = Label(self.frame, text='Course Code',bg="white",fg="black")
        self.coursecode_entry_CoursesNew = Entry(self.frame, borderwidth=0)
        self.coursename_label_CoursesNew = Label(self.frame, text='Course Name',bg="white",fg="black")
        self.coursename_entry_CoursesNew = Entry(self.frame, borderwidth=0)
        self.credit_label_CoursesNew=Label(self.frame, text='Number of credits',bg="white",fg="black")
        self.credit_entry_CoursesNew=Entry(self.frame, borderwidth=0)
        
        self.professorname_label_CoursesNew = Label(self.frame, text='Professor name',bg="white",fg="black")
        self.professorname_entry_CoursesNew = Entry(self.frame, borderwidth=0)


        self.combostyle=ttk.Style()
        self.combostyle.map('TCombobox', fieldbackground=[('readonly', 'white')])
        self.combostyle.map('TCombobox', selectbackground=[('readonly', 'white')])
        # self.combostyle.

        self.var=StringVar(self.frame)
        self.var.set("Select Semester")
        # self.course_label_CoursesNew=Label(self.frame,text="Course",bg="white",fg="black")
        # self.course_dropdown_CoursesNew=ttk.Combobox(self.frame,foreground="black",width=27,takefocus=False,textvariable=self.var,state='readonly')
        # self.course_dropdown_CoursesNew['value']=('Autumn',
        #                                         'Spring',
        #                                         'Both')
        # self.course_dropdown_CoursesNew.bind("<FocusIn>", dropdown_defocus_CoursesNew)
        


        self.submit_button_CoursesNew = Button(self.frame, text='Submit', command=lambda: self.formsubmit_command_CoursesNew(root))
        self.exit_button_CoursesNew = Button(self.frame, text="Exit", command=exit)
        self.back_button_CoursesNew = Button(self.frame, text="Back",
                                                  command=lambda: self.back_command_CoursesNew(root))
        

        self.coursecode_label_CoursesNew.grid(row=2, column=0,sticky=E+S,padx=5,pady=3,)
        self.coursecode_entry_CoursesNew.grid(row=2, column=1, sticky=W+S+E)
        self.coursename_label_CoursesNew.grid(row=3, column=0,sticky=E,padx=5,pady=3)
        self.coursename_entry_CoursesNew.grid(row=3, column=1, sticky=W+E)
    
        self.professorname_label_CoursesNew.grid(row=4,column=0,sticky=E,padx=5,pady=3)
        self.professorname_entry_CoursesNew.grid(row=4,column=1,sticky=W+E)
        self.credit_label_CoursesNew.grid(row=5,column=0,sticky=E,padx=5,pady=3)
        self.credit_entry_CoursesNew.grid(row=5,column=1,sticky=W+E)
        # self.course_label_CoursesNew.grid(row=5,column=0,sticky=E,padx=5,pady=3)
        # self.course_dropdown_CoursesNew.grid(row=5,column=1,sticky=W+E)


        self.submit_button_CoursesNew.grid(row=7, column=0, columnspan=2,pady=20)

        self.exit_button_CoursesNew.grid(row=8, column=0, pady=10, sticky=S+W)
        self.back_button_CoursesNew.grid(row=8, column=1, pady=10, sticky=S+E)

        self.frame.rowconfigure(2,weight=1)
        self.frame.rowconfigure(8,weight=1)
        self.frame.rowconfigure(4, weight=0)
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        
        root.mainloop()
    def back_command_CoursesNew(self, root):
        self.clear()
        root.maxsize(800, 600)
        DepartmentCourses.DepartmentCoursesView(root)

    def formsubmit_command_CoursesNew(self, root):
        coursecode_ = self.coursecode_entry_CoursesNew.get().upper()
        coursename_ = self.coursename_entry_CoursesNew.get()
        professorname_=self.professorname_entry_CoursesNew.get()
        credits_=self.credit_entry_CoursesNew.get()
        

        connect_, cursor_ = ES.get_student_db_ES()
        with connect_:
            try:
                cursor_.execute("INSERT INTO all_courses VALUES (:sub_code, :course_name,:prof_name,:credits)",
                                {'sub_code': coursecode_, 'course_name':coursename_,'prof_name': professorname_,
                                'credits':credits_})
                root.maxsize(800, 600)
                # self.clear()
            except sqlite3.IntegrityError:
                messagebox.showwarning("ERROR", "Course code already exists")

            # cursor_.execute("SELECT * FROM Courses WHERE Courses_name=?", (name_,))
            # print(cursor_.fetchall())

    def clear(self):
        self.parent.destroy()

