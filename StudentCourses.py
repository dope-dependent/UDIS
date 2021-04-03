from tkinter import *
import ES
import StudentMain
import StudentSearch
from ScrollableFrame import ScrollableFrame
import tkinter.ttk as ttk
from tkinter import messagebox


class StudentCourses (StudentSearch.StudentSearch):
    def __init__(self, root):
        root.title('UDIS-Register Courses')
        super().__init__(root)
        root.mainloop()

    def bindingAction(self, event):
        popupCourse = Tk()
        popupCourse.eval('tk::PlaceWindow . center')
        popupCourse.config(bg='white')
        popupCourse.geometry("600x460")
        popupCourse.minsize(600, 460)
        popupCourse.maxsize(600, 460)
        rollAndName = event.widget.cget('text')
        roll = rollAndName.split(' ')
        popupCourse.title("Register courses for " + roll[0])
        connect_, cursor_ = ES.get_student_db_ES()
        roll = roll[0]
        # TODO Add register courses functionality
        cursor_.execute('''SELECT * FROM all_courses WHERE sub_code NOT IN (SELECT sub_code FROM courses_taken
                         WHERE roll=(:roll) AND grade !=(:grade))''', {'roll': roll, 'grade': 'F'})

        courses = cursor_.fetchall()

        entryframe = Frame(popupCourse)
        entryframe.grid(row=0, column=0)
        tex = Label(entryframe, text="Enter Semester", padx=5, bg='white', pady=20)
        tex.grid(row=0, column=0)
        sem = Entry(entryframe)
        entryframe.configure(bg='white')
        sem.grid(row=0, column=1)

        courseframe = ScrollableFrame(popupCourse)
        buttons = []
        Label(courseframe.frame, text="Code", padx=10, borderwidth=1, relief='solid').grid(row=0, column=0, sticky=W+E)
        Label(courseframe.frame, text="Course Name", anchor=W, padx=20, borderwidth=1, relief='solid').grid(row=0, column=1, sticky=W+E)
        Label(courseframe.frame, text="Credits", anchor=W, padx=10, borderwidth=1, relief='solid').grid(row=0, column=2, sticky=W+E)
        Label(courseframe.frame, text=" ", anchor=W, padx=10, borderwidth=1, relief='solid').grid(row=0, column=3, sticky=W+E)
        for i in range(len(courses)):
            Label(courseframe.frame, text=courses[i][0], padx=10).grid(row=i+1, column=0)
            Label(courseframe.frame, text=courses[i][1], anchor=W, padx=20).grid(row=i+1, column=1, sticky=W+E)
            Label(courseframe.frame, text=courses[i][3], padx=10).grid(row=i+1, column=2, sticky=W+E)
            buttons.append(ttk.Checkbutton(courseframe.frame,
                                           takefocus=0,
                                           var = IntVar(0)))
            buttons[i].grid(row=i+1, column=3, sticky=E+W)
            buttons[i].state(['!alternate'])

        courseframe.frame.columnconfigure(1,weight=1)
        courseframe.grid(row=1, column=0,columnspan=10,sticky=E+W)

        submitbutton = ttk.Button(master=popupCourse,
                                  text='Submit',
                                  command= lambda : self.submit(buttons, sem, courses, roll))
        submitbutton.config(padding = [5,5,5,5])
        submitbutton.grid(row=4, column=0, columnspan=10)


        popupCourse.columnconfigure(0, weight=1) # Serial Name of Course
        popupCourse.columnconfigure(1, weight=2) # Name of Course
        popupCourse.columnconfigure(2, weight=1) # Credits of the Course
        popupCourse.columnconfigure(3, weight=1)


    def submit(self, buttons_, sem, courses, roll):
        values = [button.instate(['selected']) for button in buttons_]
        x = values.count(True)

        if x > 7:
            messagebox.showwarning('Registration Error', 'A student cannot register more than 7 courses in a semester')
            return
        elif sem.get() == "":
            messagebox.showwarning('Registration Error', 'Semester column is empty')
            return
        elif sem.get()[:3] != "AUT" and sem.get()[:3] != "SPR":
            messagebox.showwarning('Registration Error', 'Semester values can only be AUT<year> or SPR<year>')
            return

        conn_, cursor_ = ES.get_student_db_ES()

        ### TODO Check the backlog situations after making interfaces in the database
        for i in range(len(values)):
            if values[i]:
                course_code = courses[i][0]
                grade = 'R'
                seme = sem.get()
                with conn_:
                    cursor_.execute("INSERT INTO courses_taken VALUES (:roll, :sub_code, :grade, :sem_taken)",
                                        {'roll': roll, 'sub_code': course_code, 'grade': grade, 'sem_taken': seme})



    def back(self, root):
        self.clear()
        root.maxsize(800, 600)
        StudentMain.StudentMain(root)


if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    StudentCourses(root)
