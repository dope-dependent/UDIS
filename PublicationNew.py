from tkinter import *
import DepartmentPublication
import sqlite3
from tkinter import messagebox
import ES


class PublicationNew:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        Label(self.frame, text='Author').grid(row=0, column=0)
        Label(self.frame, text='Name').grid(row=1, column=0)
        Label(self.frame, text='Date').grid(row=2, column=0)

        self.nameEntry = Entry(self.frame, borderwidth=1)
        self.authorEntry = Entry(self.frame, borderwidth=1)
        self.dateEntry = Entry(self.frame, borderwidth=1)

        self.nameEntry.grid(row=1, column=1)
        self.authorEntry.grid(row=0, column=1)
        self.dateEntry.grid(row=2, column=1)

        Button(self.frame, text='Submit', command=lambda:self.submit(root)).grid(row=5, column=0, columnspan=2)
        Button(self.frame, text='Exit', command=exit).grid(row=6, column=1)
        Button(self.frame, text='Back', command=lambda:self.back(root)).grid(row=6, column=0)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()

    def submit(self, root):
        name_ = self.nameEntry.get()
        author_ = self.authorEntry.get()
        date_ = self.dateEntry.get()
        connect_, cursor_ = ES.get_student_db_ES()
        with connect_:
            try:
                cursor_.execute('INSERT INTO publications VALUES (:author, :name, :date)',
                                {'author': author_, 'name': name_, 'date': date_})
            except sqlite3.IntegrityError:
                messagebox.showwarning('ERROR', 'Publication with this name already exists!!')

    def back(self, root):
        self.clear()
        DepartmentPublication.DepartmentPublication(root)

    def clear(self):
        self.frame.destroy()