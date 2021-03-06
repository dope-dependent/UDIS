from tkinter import *
import StudentsUDIS
import Home
import tkinter.ttk as ttk

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

        self.name_label_StudentNew = Label(self.frame, text='Name',bg="white",fg="black")
        self.name_entry_StudentNew = Entry(self.frame)
        self.roll_label_StudentNew = Label(self.frame, text='Roll No',bg="white",fg="black")
        self.roll_entry_StudentNew = Entry(self.frame)
        self.address_label_StudentNew = Label(self.frame, text='Address',bg="white",fg="black")
        self.address_text_StudentNew = Text(self.frame, height=5, width=7)
        self.year_label_StudentNew = Label(self.frame, text='Year of Joining',bg="white",fg="black")
        self.year_entry_StudentNew = Entry(self.frame)


        self.combostyle=ttk.Style()
        self.combostyle.map('TCombobox', fieldbackground=[('readonly', 'white')])
        self.combostyle.map('TCombobox', selectbackground=[('readonly', 'white')])
        # self.combostyle.

        self.var=StringVar(self.frame)
        self.var.set("Select Course")
        self.course_label_StudentNew=Label(self.frame,text="Course",bg="white",fg="black")
        self.course_dropdown_StudentNew=ttk.Combobox(self.frame,foreground="black",width=27,takefocus=False,textvariable=self.var,state='readonly')
        self.course_dropdown_StudentNew['value']=('B.Tech',
                                                'M.Tech',
                                                'PhD',
                                                'M.Sc')
        self.course_dropdown_StudentNew.bind("<FocusIn>", dropdown_defocus_StudentNew)
        


        self.submit_button_StudentNew = Button(self.frame, text='Submit')
        self.exit_button_StudentNew = Button(self.frame, text="Exit", command=exit)
        self.back_button_StudentNew = Button(self.frame, text="Back",
                                                  command=lambda: self.back_command_StudentNew(root))
        

        self.name_label_StudentNew.grid(row=2, column=0,sticky=E+S,padx=5,pady=3,)
        self.name_entry_StudentNew.grid(row=2, column=1, sticky=W+S+E)
        self.roll_label_StudentNew.grid(row=3, column=0,sticky=E,padx=5,pady=3)
        self.roll_entry_StudentNew.grid(row=3, column=1, sticky=W+E)
        self.address_label_StudentNew.grid(row=4, column=0,sticky=E,padx=5,pady=3)
        self.address_text_StudentNew.grid(row=4, column=1,sticky=W+E)
        self.year_label_StudentNew.grid(row=5,column=0,sticky=E,padx=5,pady=3)
        self.year_entry_StudentNew.grid(row=5,column=1,sticky=W+E)
        self.course_label_StudentNew.grid(row=6,column=0,sticky=E,padx=5,pady=3)
        self.course_dropdown_StudentNew.grid(row=6,column=1,sticky=W+E)


        self.submit_button_StudentNew.grid(row=7, column=0, columnspan=2,pady=20)

        self.exit_button_StudentNew.grid(row=8, column=0, pady=10, sticky=S+W)
        self.back_button_StudentNew.grid(row=8, column=1, pady=10, sticky=S+E)

        self.frame.rowconfigure(2,weight=1)
        self.frame.rowconfigure(8,weight=1)
        self.frame.rowconfigure(4, weight=0)
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        
        root.mainloop()
    def back_command_StudentNew(self, root):
        self.clear()
        root.maxsize(800, 600)
        StudentsUDIS.StudentMainMenu(root)

    def formsubmit_command_StudentNew(self):
        root.maxsize(800, 600)
        self.clear()

    def clear(self):
        self.parent.destroy()

