from tkinter import *
import DepartmentProject
import sqlite3
from tkinter import messagebox
import ES


class ProjectNew:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        Label(self.frame, text='Name').grid(row=0, column=0)
        Label(self.frame, text='Organisation').grid(row=1, column=0)
        Label(self.frame, text='Incharge').grid(row=2, column=0)
        Label(self.frame, text='Duration').grid(row=3, column=0)

        self.nameEntry = Entry(self.frame, borderwidth=1)
        self.orgEntry = Entry(self.frame, borderwidth=1)
        self.inchargeEntry = Entry(self.frame, borderwidth=1)
        self.durationEntry = Entry(self.frame, borderwidth=1)

        self.nameEntry.grid(row=0, column=1)
        self.orgEntry.grid(row=1, column=1)
        self.inchargeEntry.grid(row=2, column=1)
        self.durationEntry.grid(row=3, column=1)

        Button(self.frame, text='Submit', command=lambda:self.submit(root)).grid(row=5, column=0, columnspan=2)
        Button(self.frame, text='Exit', command=exit).grid(row=6, column=1)
        Button(self.frame, text='Back', command=lambda:self.back(root)).grid(row=6, column=0)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()

    def submit(self, root):
        name_ = self.nameEntry.get()
        org_ = self.orgEntry.get()
        incharge_ = self.inchargeEntry.get()
        duration_ = self.durationEntry.get()
        connect_, cursor_ = ES.get_student_db_ES()
        with connect_:
            try:
                cursor_.execute('INSERT INTO projects VALUES (:org, :inc, :dur, :status, :name)',
                                {'org': org_, 'inc': incharge_, 'dur': duration_, 'status': 'Ongoing', 'name': name_})
            except sqlite3.IntegrityError:
                messagebox.showwarning('ERROR', 'Project with this name already exists!!')

    def back(self, root):
        self.clear()
        DepartmentProject.DepartmentProject(root)

    def clear(self):
        self.frame.destroy()