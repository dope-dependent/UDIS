from tkinter import *
import StudentsUDIS
import Home

class StudentNew:
    def __init__(self, root):
        self.frame = Frame()

        self.frame = Frame(root, bg="white")
        # self.frame.pack(fill=BOTH, expand=True)
        self.frame.grid(row=0, column=0, sticky='nsew')
        # root.minsize(400, 300)
        # root.maxsize(800, 600)
        # root.geometry('800x600')

        self.name_label_StudentNew = Label(self.frame, text='Name')
        self.name_entry_StudentNew = Entry(self.frame)
        self.roll_label_StudentNew = Label(self.frame, text='Roll No')
        self.roll_entry_StudentNew = Entry(self.frame)
        self.address_label_StudentNew = Label(self.frame, text='Address')
        self.address_text_StudentNew = Text(self.frame, height=5, width=10)
        self.year_label_StudentNew = Label(self.frame, text='Year of Joining')
        self.year_entry_StudentNew = Entry(self.frame)

        self.course_label_StudentNew = Label(self.frame, text='Course')
        self.submit_button_StudentNew = Button(self.frame, text='Submit')
        self.exit_button_StudentNew = Button(self.frame, text="Exit", command=exit)
        self.back_button_StudentNew = Button(self.frame, text="Back",
                                                  command=lambda: self.back_command_StudentNew(root))
        self.name_label_StudentNew.grid(row=2, column=0)
        self.name_entry_StudentNew.grid(row=2, column=1, sticky=E+W)
        self.roll_label_StudentNew.grid(row=3, column=0)
        self.roll_entry_StudentNew.grid(row=3, column=1, sticky=E+W)
        self.address_label_StudentNew.grid(row=4, column=0)
        self.address_text_StudentNew.grid(row=4, column=1, rowspan=3, sticky='nsew')

        self.submit_button_StudentNew.grid(row=7, column=0, columnspan=2)

        self.exit_button_StudentNew.grid(row=8, column=0, pady=10, sticky=S)
        self.back_button_StudentNew.grid(row=8, column=1, pady=10, sticky=S)

        self.frame.rowconfigure(4, weight=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
        # for i in range(8):
        #     self.frame.rowconfigure(i, weight=1)
        #
        # for i in range(2):
        #     self.frame.columnconfigure(i, weight=1)
        #
    def back_command_StudentNew(self, root):
        self.clear()
        StudentsUDIS.StudentMainMenu(root)

    def formsubmit_command_StudentNew(self):
        self.clear()

    def clear(self):
        self.frame.destroy()

