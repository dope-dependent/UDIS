from tkinter import *
import os
from sqlite3 import *
import ES


# def get_student_db_ES():
#     connect_ = sqlite3.connect('Backend/UDIS.db')
#     cursor_ = connect_.cursor()
#     return connect_, cursor_


class Main():
    def __init__(self):
        self.root = Tk()
        self.root.minsize(400, 300)
        self.root.maxsize(800, 600)
        self.root.geometry('800x600')
        self.root.configure(background="blue")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def init_sql(self):
        file_name = 'Backend/UDIS.db'
        if not os.path.exists(file_name):
            connect_ = connect(file_name)
            cursor_ = connect_.cursor()
            with connect_:
                cursor_.execute("""
                                CREATE TABLE student 
                                    (roll text UNIQUE, student_name text, address text, course text, joining text)""")
                cursor_.execute("""
                                CREATE TABLE courses_taken
                                    (roll text, sub_code text, grade text, sem_taken text)""")

                cursor_.execute("""
                                CREATE TABLE all_courses
                                    (sub_code text UNIQUE, course_name text, prof_name text, credits int)""")
        else:
            connect_ = connect(file_name)
            cursor_ = connect_.cursor()

        return connect_, cursor_

    def get_root(self):
        return self.root

if __name__ == '__main__':
    a = Main()
    connect_, cursor_ = a.init_sql()
    ES.ES(a.get_root())
    a.root.mainloop()


