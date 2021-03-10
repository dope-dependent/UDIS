from ES import ES
import StudentsNew as SN
from tkinter import *
import os
from sqlite3 import *
import StudentsView


def init_sql():
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
                        (sub_code text UNIQUE, course_name text, prof_name text)""")
    else:
        connect_ = connect(file_name)
        cursor_ = connect_.cursor()

    return connect_, cursor_


if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    root.configure(background="blue")
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    connect_, cursor_ = init_sql()
    # SN.StudentNew(root)
    StudentsView.StudentsView(root)
