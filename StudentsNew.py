from tkinter import *
import StudentMain
import tkinter.ttk as ttk
import ES
import sqlite3
from tkinter import messagebox
import re


def dropdown_defocus_StudentNew(event):
    event.widget.selection_clear()

class StudentNew:
    def __init__(self, root):
        root.title("Add new student")
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

        self.nameLabel = Label(self.frame, text='Name',bg="white",fg="black")
        self.nameEntry = Entry(self.frame, borderwidth=1)
        self.rollLabel = Label(self.frame, text='Roll No',bg="white",fg="black")
        self.rollEntry = Entry(self.frame, borderwidth=1)
        self.addressLabel = Label(self.frame, text='Address',bg="white",fg="black")
        self.addressText = Text(self.frame, height=5, width=7, borderwidth=1)
        self.yearLabel = Label(self.frame, text='Year of Joining',bg="white",fg="black")
        self.yearEntry = Entry(self.frame, borderwidth=1)


        self.combostyle=ttk.Style()
        self.combostyle.map('TCombobox', fieldbackground=[('readonly', 'white')])
        self.combostyle.map('TCombobox', selectbackground=[('readonly', 'white')])
        

        self.var=StringVar(self.frame)
        self.var.set("Select Course")
        self.courseLabel = Label(self.frame,text="Course",bg="white",fg="black")
        self.courseDropdown = ttk.Combobox(self.frame,foreground="black",width=27,takefocus=False,textvariable=self.var,state='readonly')
        self.courseDropdown['value']=('B.Tech',
                                                'M.Tech',
                                                'PhD',
                                                'M.Sc')
        self.courseDropdown.bind("<FocusIn>", dropdown_defocus_StudentNew)
        


        self.submitButton = Button(self.frame,
                                   text='Submit',
                                   command=lambda: self.submit(root,
                                                                   self.nameEntry.get(),
                                                                   self.rollEntry.get().upper(),
                                                                   self.addressText.get(1.0, END).strip('\n'),
                                                                   self.courseDropdown.get(),
                                                                   self.yearEntry.get()))

        self.exitButton = Button(self.frame, text="Exit", command=exit)
        self.backButton = Button(self.frame, text="Back", command=lambda: self.back(root))
        

        self.nameLabel.grid(row=2, column=0,sticky=E+S,padx=5,pady=3,)
        self.nameEntry.grid(row=2, column=1, sticky=W+S+E)
        self.rollLabel.grid(row=3, column=0,sticky=E,padx=5,pady=3)
        self.rollEntry.grid(row=3, column=1, sticky=W+E)
        self.addressLabel.grid(row=4, column=0,sticky=E,padx=5,pady=3)
        self.addressText.grid(row=4, column=1,sticky=W+E)
        self.yearLabel.grid(row=5,column=0,sticky=E,padx=5,pady=3)
        self.yearEntry.grid(row=5,column=1,sticky=W+E)
        self.courseLabel.grid(row=6,column=0,sticky=E,padx=5,pady=3)
        self.courseDropdown.grid(row=6,column=1,sticky=W+E)


        self.submitButton.grid(row=7, column=0, columnspan=2,pady=20)

        self.exitButton.grid(row=8, column=0, pady=10, sticky=S+W)
        self.backButton.grid(row=8, column=1, pady=10, sticky=S+E)

        self.frame.rowconfigure(2,weight=1)
        self.frame.rowconfigure(8,weight=1)
        self.frame.rowconfigure(4, weight=0)
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        
        root.geometry("400x400")
        root.minsize(400,400)
        root.maxsize(400,400)

    def back(self, root):
        self.clear()
        root.maxsize(800, 600)
        StudentMain.StudentMain(root)

    def submit(self, root, name, roll, address, course, year):
        try:
            self.formsubmit(name, roll, address, course, year)
            messagebox.showinfo('Add New Student', 'Student added successfully')
            root.maxsize(800, 600)
            self.clear()
            StudentMain.StudentMain(root)
        except Exception as e:
            messagebox.showwarning("Adding new student", e)

    @staticmethod
    def formsubmit(name, roll, address, course, year):
        lengths = [len(i) for i in [name, roll, address, course, year]]

        connect_, cursor_ = ES.get_student_db_ES()

        roll_f_exception = Exception('''Roll Number should be of the form [2 year digits]
            [2 dep digits][course identifier][4 serial number digits]''')

        if 0 in lengths:
            raise Exception('One or more of the fields are blank')
        elif len(year) != 4 or not re.compile('\d\d\d\d').search(year):
            raise Exception('Year pattern incorrect, should be a 4-digit number')
        elif len(roll) != 9:
            raise Exception('Roll Number has incorrect length')
        elif year[2:4] != roll[0:2]:
            raise roll_f_exception
        elif not re.compile('[A-Z][A-Z]').search(roll[2:4]):
            raise roll_f_exception
        elif not re.compile('\d\d\d\d').search(roll[5:9]):
            raise roll_f_exception
        elif course == "Select Course":
            raise Exception("Please select the course")
        else:
            digit = roll[4]
            exc = Exception('Course Identifer digit is invalid')
            if digit not in ['1', '2', '3', '6']:

                raise exc
            elif digit == '1' and course != 'B.Tech':
                raise exc
            elif digit == '3' and course != 'M.Tech':
                raise exc
            elif digit == '6' and course != 'PhD':
                raise exc
            elif digit == '2' and course != 'M.Sc':
                raise exc

        with connect_:
            try:
                cursor_.execute("INSERT INTO student VALUES (:roll, :name, :address, :course, :joining)",
                    {'roll': roll, 'name': name, 'address': address, 'course': course, 'joining': year})

            except sqlite3.IntegrityError:
                raise Exception('Roll No already exists')

    def clear(self):
        self.parent.destroy()

    @staticmethod
    def test():
        print('Unit Test for the StudentsNew Class\n')
        success = 0
        fail = 0
        print('a. Roll number format checking')
        try :
            StudentNew.formsubmit('Kal El','21DCSYNDER','Krypton\nDC Extended Universe','PhD','2021')
            fail+=1
            print('\tFAIL')
        except Exception:
            print('\tPASS')
            success+=1

        try :
            StudentNew.formsubmit('Kal El','23CS10001','Krypton\nDC Extended Universe','PhD','2021')
            fail+=1
            print('\tFAIL')
        except Exception:
            print('\tPASS')
            success+=1

        print("b. Year of admission checking")
        try :
            StudentNew.formsubmit('Kal El','23CS10001','Krypton\nDC Extended Universe','PhD','202b1')
            fail+=1
            print('\tFAIL')
        except Exception:
            print('\tPASS')
            success+=1

        print("c. Duplicate Roll No checking")
        try :
            StudentNew.formsubmit('Kal El','19CS10055','Krypton\nDC Extended Universe','B.Tech','2019')
            fail+=1
            print('\tFAIL')
        except Exception:
            print('\tPASS')
            success+=1

        print("d. Blank field testing")
        try :
            StudentNew.formsubmit('','19CS10001','Hyderabad\nTelangana\nIndia','B.Tech','2019')
            fail+=1
            print('\tFAIL')
        except Exception:
            print('\tPASS')
            success+=1

        try :
            StudentNew.formsubmit('A Ashwin Sai','19CS10001','Hyderabad\nTelangana\nIndia','B.Tech','')
            fail+=1
            print('\tFAIL')
        except Exception:
            print('\tPASS')
            success+=1

        print("e. Course Identifier Testing")
        try :
            StudentNew.formsubmit('Kal El','19CS10075','Krypton\nDC Extended Universe','PhD','2019')
            fail+=1
            print('\tFAIL')
        except Exception:
            print('\tPASS')
            success+=1

        print('f. Happy Path test')
        try :
            StudentNew.formsubmit('Kal El','19CS10075','Krypton\nDC Extended Universe','B.Tech','2019')
            print('\tPASS')
            success+=1
        except Exception:
            print('\tFAIL')
            fail+=1

        print(f'Test cases passed {success}/{success+fail}')
        print(f'Percentage = {(success/(success+fail))*100}')

        
if __name__ == '__main__':
    StudentNew.test()