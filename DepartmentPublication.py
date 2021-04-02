from tkinter import *
import DepartmentResearch
from ScrollableFrame import ScrollableFrame
import ES
import PublicationNew

class DepartmentPublication(DepartmentResearch.DepartmentResearch):
    def __init__(self, root):
        root.title('UDIS-Department-Academics-Publications')
        super().__init__(root)
        self.display()
        root.mainloop()

    def display(self):
        self.displayAll.destroy()
        self.displayAll = ScrollableFrame(self.frame)
        self.displayAll.grid(row=0, column=0, padx=30, sticky=N+S+E+W)
        connect_, cursor_ = ES.get_student_db_ES()
        cursor_.execute('SELECT * FROM publications')
        allPublications = cursor_.fetchall()
        Label(self.displayAll.frame, text='Sr. No.').grid(row=0, column=0)
        Label(self.displayAll.frame, text='Author').grid(row=0, column=1)
        Label(self.displayAll.frame, text='Name').grid(row=0, column=2)
        Label(self.displayAll.frame, text='Date').grid(row=0, column=3)

        for i in range(len(allPublications)):
            Label(self.displayAll.frame, anchor=W, text=i+1).grid(row=i+1, column=0)
            Label(self.displayAll.frame, anchor=W, text=allPublications[i][0]).grid(row=i+1, column=1)
            publicationName = Label(self.displayAll.frame, anchor=W, text=allPublications[i][1])
            publicationName.grid(row=i+1, column=2)
            Label(self.displayAll.frame, anchor=W, text=allPublications[i][2]).grid(row=i+1, column=3)
            publicationName.bind('<Button-1>', self.bindingAction)

        self.displayAll.frame.columnconfigure(2, weight=2)
        self.displayAll.frame.columnconfigure(1, weight=1)

    def bindingAction(self, event):
        popupPublication = Tk()
        popupPublication.geometry('400x300')
        publicationName = event.widget.cget('text')
        popupPublication.title(publicationName)
        connect_, cursor_ = ES.get_student_db_ES()
        cursor_.execute('SELECT * FROM publications WHERE pub_name=(:name)', {'name':publicationName})
        publication = cursor_.fetchone()

        Label(popupPublication, text='Author').grid(row=1, column=0, sticky=W, padx=10)
        Label(popupPublication, text='Name').grid(row=2, column=0, sticky=W, padx=10)
        Label(popupPublication, text='Date').grid(row=3, column=0, sticky=W, padx=10)

        Label(popupPublication, text=publication[0]).grid(row=1, column=1, sticky=W)
        Label(popupPublication, text=publication[1]).grid(row=2, column=1, sticky=W)
        Label(popupPublication, text=publication[2]).grid(row=3, column=1, sticky=W)

    def new(self, root):
        self.clear()
        PublicationNew.PublicationNew(root)


if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    DepartmentPublication(root)