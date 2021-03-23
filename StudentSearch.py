from tkinter import *
import ES
from tkinter import messagebox
import StudentsUDIS
from ScrollableFrame import ScrollableFrame

class StudentSearch:
    def __init__(self, root):

        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.name_label_StudentSearch = Label(self.frame, text='Name', fg="black")
        self.name_entry_StudentSearch = Entry(self.frame, borderwidth=0)
        self.roll_label_StudentSearch = Label(self.frame, text='Roll No', fg="black")
        self.roll_entry_StudentSearch = Entry(self.frame, borderwidth=0)

        self.submit_button_StudentSearch = Button(self.frame, text='Search', command=lambda :self.search_command_StudentSearch(root))

        self.display_frame_StudentSearch = Frame(self.frame)
        self.name_label_StudentSearch.grid(row=2, column=0, padx=5, pady=3)
        self.name_entry_StudentSearch.grid(row=2, column=1)
        self.roll_label_StudentSearch.grid(row=3, column=0, padx=5, pady=3)
        self.roll_entry_StudentSearch.grid(row=3, column=1)


        self.exit_button_StudentSearch = Button(self.frame, text="Exit", command=exit)
        self.back_button_StudentSearch = Button(self.frame, text="Back",
                                             command=lambda: self.back_command(root))

        self.submit_button_StudentSearch.grid(row=4, column=0,columnspan=2,pady=20)
        self.display_frame_StudentSearch.grid(row=5, column=0,columnspan=2)

        self.exit_button_StudentSearch.grid(row=8, column=0, padx=50, pady=50, sticky=S + W)
        self.back_button_StudentSearch.grid(row=8, column=1, padx=50, pady=50, sticky=S + E)

        self.frame.rowconfigure(8, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()

    def binding_action_StudentSearch(self, event):
        pass

    def display_students(self, root, list_):
        self.display_frame_StudentSearch.destroy()
        self.display_frame_StudentSearch = Frame(self.frame)
        self.display_scrollframe_StudentSearch=ScrollableFrame(self.display_frame_StudentSearch)
        self.display_scrollframe_StudentSearch.grid(column=0,row=0,sticky="nsew")

        self.display_frame_StudentSearch.grid(row=5, column=0, columnspan=2)
        for i in range(len(list_)):
            studentserial_Label_StudentSearch = Label(self.display_scrollframe_StudentSearch.scrollable_frame, anchor=W, text=i+1)
            studentrollname_Label_StudentSearch = Label(self.display_scrollframe_StudentSearch.scrollable_frame, anchor=W, text=list_[i][0] + '    ' + list_[i][1])
            studentserial_Label_StudentSearch.grid(row=i, column=0, sticky=W)
            studentrollname_Label_StudentSearch.grid(row=i, column=1, sticky=W)
            studentrollname_Label_StudentSearch.bind('<Button-1>', self.binding_action_StudentSearch)

    def back_command(self, root):
        pass

    def search_command_StudentSearch(self, root):
        connect_, cursor_ = ES.get_student_db_ES()
        name_ = self.name_entry_StudentSearch.get()
        roll_no_ = self.roll_entry_StudentSearch.get()
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
    StudentSearch(root)
