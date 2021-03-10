from tkinter import *
import ES
from tkinter import messagebox
import StudentsUDIS

class StudentsView:
    def __init__(self, root):

        root.title('UDIS-View Student')
        self.frame = Frame(root)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.name_label_StudentsView = Label(self.frame, text='Name', fg="black")
        self.name_entry_StudentsView = Entry(self.frame, borderwidth=0)
        self.roll_label_StudentsView = Label(self.frame, text='Roll No', fg="black")
        self.roll_entry_StudentsView = Entry(self.frame, borderwidth=0)

        self.submit_button_StudentsView= Button(self.frame, text='Search', command=lambda :self.search_command_StudentsView(root))

        self.display_frame_StudentsView = Frame(self.frame)
        self.name_label_StudentsView.grid(row=2, column=0, padx=5, pady=3)
        self.name_entry_StudentsView.grid(row=2, column=1)
        self.roll_label_StudentsView.grid(row=3, column=0, padx=5, pady=3)
        self.roll_entry_StudentsView.grid(row=3, column=1)


        self.exit_button_StudentNew = Button(self.frame, text="Exit", command=exit)
        self.back_button_StudentNew = Button(self.frame, text="Back",
                                             command=lambda: self.back_command_StudentNew(root))

        self.submit_button_StudentsView.grid(row=4, column=0,columnspan=2,pady=20)
        self.display_frame_StudentsView.grid(row=5, column=0,columnspan=2)

        self.exit_button_StudentNew.grid(row=8, column=0, pady=10, sticky=S + W)
        self.back_button_StudentNew.grid(row=8, column=1, pady=10, sticky=S + E)



        # self.frame.rowconfigure(2, weight=1)
        # self.frame.rowconfigure(3, weight=1)
        #
        self.frame.rowconfigure(8, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()

    def display_students(self, root, list_):
        for i in range(len(list_)):
            print(list_[i][1])
            Label(self.display_frame_StudentsView, text=list_[i][0]).grid(row=i, column=0)
            Label(self.display_frame_StudentsView, text=list_[i][1]).grid(row=i, column=1)

    def back_command_StudentNew(self, root):
        self.clear()
        root.maxsize(800, 600)
        StudentsUDIS.StudentMainMenu(root)


    def search_command_StudentsView(self, root):
        connect_, cursor_ = ES.get_student_db_ES()
        name_ = self.name_entry_StudentsView.get()
        roll_no_ = self.roll_entry_StudentsView.get()
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
    StudentsView(root)
