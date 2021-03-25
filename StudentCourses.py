from tkinter import *
import ES
import StudentMain
import StudentSearch


class StudentCourses (StudentSearch.StudentSearch):
    def __init__(self, root):
        root.title('UDIS-Register Courses')
        super().__init__(root)
        root.mainloop()

    def bindingAction(self, event):
        popupCourse = Tk()
        popupCourse.geometry("400x300")
        rollAndName = event.widget.cget('text')
        roll = rollAndName.split(' ')
        popupCourse.title(roll[0])
        connect_, cursor_ = ES.get_student_db_ES()
        roll = roll[0]
        # TODO Add register courses functionality
        cursor_.execute('''SELECT * FROM all_courses WHERE sub_code != (SELECT sub_code FROM courses_taken
                         WHERE roll=(:roll) AND grade !=(:grade))''', {'roll': roll, 'grade': 'F'})

        courses = cursor_.fetchall()
        for count, course in enumerate(courses):
            # TODO Add the checkbox thingy here.
            print(1)
        popupCourse.columnconfigure(0, weight=1) # Serial Name of Course
        popupCourse.columnconfigure(1, weight=2) # Name of Course
        popupCourse.columnconfigure(2, weight=1) # Register Button

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
