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

    def viewstudentroll_popup_Command_StudentsView(self, event):
        popup_StudentsView = Tk()
        popup_StudentsView.geometry("400x300")
        popup_StudentsView.title(event.widget.cget('text'))
        connect_, cursor_ = ES.get_student_db_ES()
        cursor_.execute('SELECT * FROM student WHERE roll=(:roll)', {'roll':event.widget.cget('text')})
        student = cursor_.fetchone()
        studentroll_title_Label_StudentsView = Label(popup_StudentsView, text='Roll No.')
        studentroll_title_Label_StudentsView.grid(row=1, column=0, sticky=W, padx=10)
        studentname_title_Label_StudentsView = Label(popup_StudentsView, text='Name')
        studentname_title_Label_StudentsView.grid(row=2, column=0, sticky = W, padx=10)
        studentaddress_title_Label_StudentsView = Label(popup_StudentsView, text='Address')
        studentaddress_title_Label_StudentsView.grid(row=3, column=0, sticky = W, padx=10)
        studentcourse_title_Label_StudentsView = Label(popup_StudentsView, text='Course')
        studentcourse_title_Label_StudentsView.grid(row=4, column=0, sticky = W, padx=10)
        studentyear_title_Label_StudentsView = Label(popup_StudentsView, text='Joining Year')
        studentyear_title_Label_StudentsView.grid(row=5, column=0, sticky = W, padx=10)
        studentroll_Label_StudentsView = Label(popup_StudentsView, text=student[0])
        studentroll_Label_StudentsView.grid(row=1, column=1, sticky = W)
        studentname_Label_StudentsView = Label(popup_StudentsView, text=student[1])
        studentname_Label_StudentsView.grid(row=2, column=1, sticky = W)
        studentaddress_Label_StudentsView = Label(popup_StudentsView, text=student[2], anchor=W, justify='left')
        studentaddress_Label_StudentsView.grid(row=3, column=1, sticky = W)
        studentcourse_Label_StudentsView = Label(popup_StudentsView, text=student[3])
        studentcourse_Label_StudentsView.grid(row=4, column=1, sticky = W)
        studentyear_Label_StudentsView = Label(popup_StudentsView, text=student[4])
        studentyear_Label_StudentsView.grid(row=5, column=1, sticky = W)
        popup_StudentsView.columnconfigure(0, weight=1)
        popup_StudentsView.columnconfigure(1, weight=2)
        popup_StudentsView.rowconfigure(0, weight=1)
        popup_StudentsView.rowconfigure(6, weight=2)


    # def viewstudentname_popup_Command_StudentsView(self, event):
    #     pop_StudentsView = Tk()
    #     popup_Students


    def display_students(self, root, list_):
        # textbox_text_StudentView = Text(self.display_frame_StudentsView)
        # textbox_text_StudentView.grid(row=1, column=0)
        for i in range(len(list_)):
            studentroll_Label_StudentsView = Label(self.display_frame_StudentsView, text=list_[i][0])
            studentname_Label_StudentsView = Label(self.display_frame_StudentsView, text=list_[i][1])
            studentroll_Label_StudentsView.grid(row=i,column=0)
            studentname_Label_StudentsView.grid(row=i,column=1)
            studentroll_Label_StudentsView.bind('<Button-1>', self.viewstudentroll_popup_Command_StudentsView)
            # studentname_Label_StudentsView.bind('<Button-1>', self.viewstudentname_popup_Command_StudentsView)


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