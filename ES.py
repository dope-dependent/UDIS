from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
# import StudentsUDIS
import Home
import sqlite3

def get_student_db_ES():
    connect_ = sqlite3.connect('Backend/UDIS.db')
    cursor_ = connect_.cursor()
    return connect_, cursor_

class ES:
    def __init__(self, root):

        # root.title("Not ERP")

        self.frame = Frame(root, bg="white")
        self.frame.grid(row=0, column=0, sticky='nsew')
        
        self.idLabel = Label(self.frame,text="User ID  ", bg='white',fg='black')
        self.idEntry = Entry(self.frame)
        

        self.pwLabel = Label(self.frame, text="Password", bg='white',fg='black')
        
        self.pwEntry = Entry(self.frame)
        

        style = ttk.Style()
        style.configure('W.TButton', font=
        ('Arial', 10),
                        background='white')

        self.submitButton = ttk.Button(self.frame, text="Login", style = 'W.TButton', command=lambda: self.login(root))

        self.idLabel.grid(row=0, column=0, sticky='se', padx=10, pady=5)
        self.idEntry.grid(row=0, column=1, sticky='sw', padx=10, pady=5)
        self.pwLabel.grid(row=1, column=0, sticky='ne', padx=10, pady=5)
        self.pwEntry.grid(row=1, column=1, sticky='nw', padx=10, pady=5)
        self.submitButton.grid(row=2, column=0, columnspan=2, sticky='n')
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=1)



    def login(self,root):
        id_ip = self.idEntry.get()
        pw_ip = self.pwEntry.get()
        # DEBUG - Comment out later
        # print(id_ip_ES)
        # print(pw_ip_ES)
        # TODO Add login functionality
        self.clear()
        Home.Home(root)

    def clear(self):
        self.frame.destroy()

if __name__ == '__main__':
    root = Tk()

    a = ES(root)
    del a
