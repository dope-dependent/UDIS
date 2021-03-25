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
       
        root.maxsize(400, 400)
        

        self.coursecodeLabel = Label(self.frame, text='Course Code',bg="white",fg="black")
        self.coursecodeEntry = Entry(self.frame, borderwidth=0)
        
        self.coursenameLabel = Label(self.frame, text='Course Name',bg="white",fg="black")
        self.coursenameEntry = Entry(self.frame, borderwidth=0)
        
        self.creditLabel=Label(self.frame, text='Number of credits',bg="white",fg="black")
        self.creditEntry=Entry(self.frame, borderwidth=0)
        
        self.professornameLabel = Label(self.frame, text='Professor name',bg="white",fg="black")
        self.professornameEntry = Entry(self.frame, borderwidth=0)

        self.submitButton = Button(self.frame, text='Submit', command=lambda: self.submit(root))
        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame, text="Back",
                                                  command=lambda: self.back(root))
        

        self.coursecodeLabel.grid(row=2, column=0,sticky=E+S,padx=5,pady=3,)
        self.coursecodeEntry.grid(row=2, column=1, sticky=W+S+E)
        self.coursenameLabel.grid(row=3, column=0,sticky=E,padx=5,pady=3)
        self.coursenameEntry.grid(row=3, column=1, sticky=W+E)
    
        self.professornameLabel.grid(row=4,column=0,sticky=E,padx=5,pady=3)
        self.professornameEntry.grid(row=4,column=1,sticky=W+E)
        self.creditLabel.grid(row=5,column=0,sticky=E,padx=5,pady=3)
        self.creditEntry.grid(row=5,column=1,sticky=W+E)

        self.submitButton.grid(row=7, column=0, columnspan=2,pady=20)

        self.exitButton.grid(row=8, column=0, pady=10, sticky=S+W)
        self.backButton.grid(row=8, column=1, pady=10, sticky=S+E)

        self.frame.rowconfigure(2,weight=1)
        self.frame.rowconfigure(8,weight=1)
        self.frame.rowconfigure(4, weight=0)
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        
        root.mainloop()
    def back(self, root):
        self.clear()
        root.maxsize(800, 600)
        DepartmentCourses.DepartmentCourses(root)

    def submit(self, root):
        coursecode_ = self.coursecodeEntry.get().upper()
        coursename_ = self.coursenameEntry.get()
        professorname_=self.professornameEntry.get()
        credits_=self.creditEntry.get()
        

        connect_, cursor_ = ES.get_student_db_ES()
        with connect_:
            try:
                cursor_.execute("INSERT INTO all_courses VALUES (:sub_code, :course_name,:prof_name,:credits)",
                                {'sub_code': coursecode_, 'course_name':coursename_,'prof_name': professorname_,
                                'credits':credits_})
                root.maxsize(800, 600)
            except sqlite3.IntegrityError:
                messagebox.showwarning("ERROR", "Course code already exists")

            

    def clear(self):
        self.parent.destroy()

