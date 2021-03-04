from tkinter import *
from tkinter import messagebox
import StudentsUDIS

global root_

class ES:
    def __init__(self, root):
        global root_
        root_ = root
        root.title("Not ERP")

        self.frame = Frame(root)
        # self.frame.pack(fill=BOTH, expand=True)
        self.frame.grid(row=0, column=0, sticky='nsew')
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')

        self.id_label_ES = Label(self.frame,text="User ID  ")
        self.id_label_ES.grid(row=0, column=0, sticky='se', padx=10, pady=5)

        self.id_entry_ES = Entry(self.frame)
        self.id_entry_ES.grid(row=0, column=1, sticky='sw', padx=10, pady=5)

        self.password_label_ES = Label(self.frame, text="Password")
        self.password_label_ES.grid(row=1, column=0, sticky='ne', padx=10, pady=5)
        self.password_entry_ES = Entry(self.frame)
        self.password_entry_ES.grid(row=1, column=1, sticky='nw', padx=10, pady=5)

        self.submit_entry_ES = Button(self.frame,text="Login", command=lambda: self.login_ES())
        self.submit_entry_ES.grid(row=2, column=0, columnspan=2, sticky='n')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=1)
        self.frame.mainloop()


    def login_ES(self):
        global root_
        id_input_ES = self.id_entry_ES.get()
        password_input_ES = self.password_entry_ES.get()
        print(id_input_ES)
        print(password_input_ES)
        if id_input_ES == "admin" and password_input_ES == "1234":
            print('Success')
            self.clear()
            StudentsUDIS.StudentMainMenu(root_)
        else:
            messagebox.askretrycancel("Login ERROR", "Invalid credentials")

    def clear(self):
        self.frame.destroy()
        # self.id_entry_ES.destroy()
        # self.id_label_ES.destroy()
        # self.password_entry_ES.destroy()
        # self.password_label_ES.destroy()
        # self.submit_entry_ES.destroy()


if __name__ == '__main__':
    root = Tk()
    a = ES(root)
    del a
