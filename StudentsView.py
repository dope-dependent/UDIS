from tkinter import *
import ES
import StudentsUDIS
import StudentSearch

class StudentsView (StudentSearch.StudentSearch):
    def __init__(self, root):
        root.title('UDIS-View Student')
        super().__init__(root)
        root.mainloop()

    def binding_action_StudentSearch(self, event):
        popup_StudentsView = Tk()
        popup_StudentsView.geometry("400x300")
        rollname = event.widget.cget('text')
        roll = rollname.split(' ')
        popup_StudentsView.title(roll[0])
        connect_, cursor_ = ES.get_student_db_ES()
        roll = roll[0]
        cursor_.execute('SELECT * FROM student WHERE roll=(:roll)', {'roll':roll})
        student = cursor_.fetchone()
        Label(popup_StudentsView, text='Roll No.').grid(row=1, column=0, sticky=W, padx=10)
        Label(popup_StudentsView, text='Name').grid(row=2, column=0, sticky = W, padx=10)
        Label(popup_StudentsView, text='Address').grid(row=3, column=0, sticky = W, padx=10)
        Label(popup_StudentsView, text='Course').grid(row=4, column=0, sticky = W, padx=10)
        Label(popup_StudentsView, text='Joining Year').grid(row=5, column=0, sticky = W, padx=10)
        Label(popup_StudentsView, text=student[0]).grid(row=1, column=1, sticky = W)
        Label(popup_StudentsView, text=student[1]).grid(row=2, column=1, sticky = W)
        Label(popup_StudentsView, text=student[2], anchor=W, justify='left').grid(row=3, column=1, sticky = W)
        Label(popup_StudentsView, text=student[3]).grid(row=4, column=1, sticky = W)
        Label(popup_StudentsView, text=student[4]).grid(row=5, column=1, sticky = W)
        popup_StudentsView.columnconfigure(0, weight=1)
        popup_StudentsView.columnconfigure(1, weight=2)
        popup_StudentsView.rowconfigure(0, weight=1)
        popup_StudentsView.rowconfigure(6, weight=2)

    def back_command(self, root):
        self.clear()
        root.maxsize(800, 600)
        StudentsUDIS.StudentMainMenu(root)


if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    StudentsView(root)
