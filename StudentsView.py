from tkinter import *
import ES
import StudentMain
import StudentSearch

class StudentsView (StudentSearch.StudentSearch):
    def __init__(self, root):
        root.title('UDIS-View Student')
        super().__init__(root)
        root.mainloop()

    def bindingAction(self, event):
        popupStudent = Tk()
        popupStudent.geometry("400x300")
        rollAndName = event.widget.cget('text')
        roll = rollAndName.split(' ')
        popupStudent.title(roll[0])
        connect_, cursor_ = ES.get_student_db_ES()
        roll = roll[0]
        cursor_.execute('SELECT * FROM student WHERE roll=(:roll)', {'roll':roll})
        student = cursor_.fetchone()
        Label(popupStudent, text='Roll No.').grid(row=1, column=0, sticky=W, padx=10)
        Label(popupStudent, text='Name').grid(row=2, column=0, sticky = W, padx=10)
        Label(popupStudent, text='Address').grid(row=3, column=0, sticky = W, padx=10)
        Label(popupStudent, text='Course').grid(row=4, column=0, sticky = W, padx=10)
        Label(popupStudent, text='Joining Year').grid(row=5, column=0, sticky = W, padx=10)
        Label(popupStudent, text=student[0]).grid(row=1, column=1, sticky = W)
        Label(popupStudent, text=student[1]).grid(row=2, column=1, sticky = W)
        Label(popupStudent, text=student[2], anchor=W, justify='left').grid(row=3, column=1, sticky = W)
        Label(popupStudent, text=student[3]).grid(row=4, column=1, sticky = W)
        Label(popupStudent, text=student[4]).grid(row=5, column=1, sticky = W)
        popupStudent.columnconfigure(0, weight=1)
        popupStudent.columnconfigure(1, weight=2)
        popupStudent.rowconfigure(0, weight=1)
        popupStudent.rowconfigure(6, weight=2)

    def back(self, root):
        self.clear()
        root.maxsize(800, 600)
        StudentMain.StudentMain(root)


if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    StudentsView(root)
