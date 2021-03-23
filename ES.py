from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import StudentsUDIS
import Home
import sqlite3

global root_

def get_student_db_ES():
    connect_ = sqlite3.connect('Backend/UDIS.db')
    print(type(connect_))
    cursor_ = connect_.cursor()
    return connect_, cursor_

class ES:
    def __init__(self, root):
        global root_
        root_ = root
        root.title("Not ERP")

        self.frame = Frame(root, bg="white")
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.id_l_ES = Label(self.frame,text="User ID  ", bg='white',fg='black')
        self.id_l_ES.grid(row=0, column=0, sticky='se', padx=10, pady=5)

        self.id_e_ES = Entry(self.frame)
        self.id_e_ES.grid(row=0, column=1, sticky='sw', padx=10, pady=5)

        self.pw_l_ES = Label(self.frame, text="Password", bg='white',fg='black')
        self.pw_l_ES.grid(row=1, column=0, sticky='ne', padx=10, pady=5)
        self.pw_e_ES = Entry(self.frame)
        self.pw_e_ES.grid(row=1, column=1, sticky='nw', padx=10, pady=5)

        style = ttk.Style()
        style.configure('W.TButton', font=
        ('calibri light', 10, 'underline'),
                        foreground='red',
                        background='white')

        self.submit_e_ES = ttk.Button(self.frame, text="Login", style = 'W.TButton', command=lambda: self.login_ES())
        self.submit_e_ES.grid(row=2, column=0, columnspan=2, sticky='n')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=1)
        self.frame.mainloop()


    def login_ES(self):
        global root_
        id_ip_ES = self.id_e_ES.get()
        pw_ip_ES = self.pw_e_ES.get()
        # DEBUG - Comment out later
        print(id_ip_ES)
        print(pw_ip_ES)
        # TODO Add login functionality
        self.clear()
        Home.Home(root_)

    def clear(self):
        self.frame.destroy()

if __name__ == '__main__':
    root = Tk()
    a = ES(root)
    del a
