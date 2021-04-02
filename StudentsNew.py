from tkinter import *
import StudentMain
import tkinter.ttk as ttk
import ES
import sqlite3
from tkinter import messagebox


def dropdown_defocus_StudentNew(event):
    event.widget.selection_clear()

class StudentNew:
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

        self.nameLabel = Label(self.frame, text='Name',bg="white",fg="black")
        self.nameEntry = Entry(self.frame, borderwidth=1)
        self.rollLabel = Label(self.frame, text='Roll No',bg="white",fg="black")
        self.rollEntry = Entry(self.frame, borderwidth=1)
        self.addressLabel = Label(self.frame, text='Address',bg="white",fg="black")
        self.addressText = Text(self.frame, height=5, width=7, borderwidth=1)
        self.yearLabel = Label(self.frame, text='Year of Joining',bg="white",fg="black")
        self.yearEntry = Entry(self.frame, borderwidth=1)


        self.combostyle=ttk.Style()
        self.combostyle.map('TCombobox', fieldbackground=[('readonly', 'white')])
        self.combostyle.map('TCombobox', selectbackground=[('readonly', 'white')])
        # self.combostyle.

        self.var=StringVar(self.frame)
        self.var.set("Select Course")
        self.courseLabel = Label(self.frame,text="Course",bg="white",fg="black")
        self.courseDropdown = ttk.Combobox(self.frame,foreground="black",width=27,takefocus=False,textvariable=self.var,state='readonly')
        self.courseDropdown['value']=('B.Tech',
                                                'M.Tech',
                                                'PhD',
                                                'M.Sc')
        self.courseDropdown.bind("<FocusIn>", dropdown_defocus_StudentNew)
        


        self.submitButton = Button(self.frame, text='Submit', command=lambda: self.formsubmit(root))
        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame, text="Back", command=lambda: self.back(root))
        

        self.nameLabel.grid(row=2, column=0,sticky=E+S,padx=5,pady=3,)
        self.nameEntry.grid(row=2, column=1, sticky=W+S+E)
        self.rollLabel.grid(row=3, column=0,sticky=E,padx=5,pady=3)
        self.rollEntry.grid(row=3, column=1, sticky=W+E)
        self.addressLabel.grid(row=4, column=0,sticky=E,padx=5,pady=3)
        self.addressText.grid(row=4, column=1,sticky=W+E)
        self.yearLabel.grid(row=5,column=0,sticky=E,padx=5,pady=3)
        self.yearEntry.grid(row=5,column=1,sticky=W+E)
        self.courseLabel.grid(row=6,column=0,sticky=E,padx=5,pady=3)
        self.courseDropdown.grid(row=6,column=1,sticky=W+E)


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
        StudentMain.StudentMain(root)

    def formsubmit(self, root):
        name_ = self.nameEntry.get()
        roll_no_ = self.rollEntry.get().upper()
        address_ = self.addressText.get(1.0, END).strip('\n')
        course_ = self.courseDropdown.get()
        year_ = self.yearEntry.get()
        connect_, cursor_ = ES.get_student_db_ES()
        with connect_:
            try:
                cursor_.execute("INSERT INTO student VALUES (:roll, :name, :address, :course, :joining)",
                                {'roll': roll_no_, 'name': name_, 'address': address_, 'course': course_,
                                 'joining': year_})
                root.maxsize(800, 600)
                # self.clear()
            except sqlite3.IntegrityError:
                messagebox.showwarning("ERROR", "Roll Number already exists")

            # cursor_.execute("SELECT * FROM student WHERE student_name=?", (name_,))
            # print(cursor_.fetchall())

    def clear(self):
        self.parent.destroy()

