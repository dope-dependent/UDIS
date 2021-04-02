from tkinter import *
import DepartmentResearch
from ScrollableFrame import ScrollableFrame
import ES
import ProjectNew

class DepartmentProject(DepartmentResearch.DepartmentResearch):
    def __init__(self, root):
        root.title('UDIS-Department-Academics-Projects')
        super().__init__(root)
        self.display()
        root.mainloop()

    def display(self):
        self.displayAll.destroy()
        self.displayAll = ScrollableFrame(self.frame)
        self.displayAll.grid(row=0, column=0, padx=30, sticky=N+S+E+W)
        connect_, cursor_ = ES.get_student_db_ES()
        cursor_.execute('SELECT * FROM projects')
        allProjects = cursor_.fetchall()
        Label(self.displayAll.frame, text='Sr. No.', relief=GROOVE).grid(row=0, column=0, sticky=E+W)
        Label(self.displayAll.frame, text='Organisation', relief=GROOVE).grid(row=0, column=1, sticky=E+W)
        Label(self.displayAll.frame, text='Incharge', relief=GROOVE).grid(row=0, column=2, sticky=E+W)
        Label(self.displayAll.frame, text='Duration', relief=GROOVE).grid(row=0, column=3, sticky=E+W)
        Label(self.displayAll.frame, text='Status', relief=GROOVE).grid(row=0, column=4, sticky=E+W)
        Label(self.displayAll.frame, text='Name', relief=GROOVE).grid(row=0, column=5, sticky=E+W)

        for i in range(len(allProjects)):
            Label(self.displayAll.frame, anchor=W, text=i+1).grid(row=i+1, column=0)
            Label(self.displayAll.frame, anchor=W, text=allProjects[i][0]).grid(row=i+1, column=1)
            Label(self.displayAll.frame, anchor=W, text=allProjects[i][1]).grid(row=i+1, column=2)
            Label(self.displayAll.frame, anchor=W, text=allProjects[i][2]).grid(row=i+1, column=3)
            Label(self.displayAll.frame, anchor=W, text=allProjects[i][3]).grid(row=i+1, column=4)
            projectName = Label(self.displayAll.frame, anchor=W, text=allProjects[i][4])
            projectName.grid(row=i+1, column=5, sticky=W+E)
            projectName.bind('<Button-1>', self.bindingAction)

        self.displayAll.frame.columnconfigure(1, weight=1)
        self.displayAll.frame.columnconfigure(2, weight=1)
        self.displayAll.frame.columnconfigure(5, weight=3)


    def bindingAction(self, event):
        popupProject = Tk()
        popupProject.geometry('400x300')
        projectName = event.widget.cget('text')
        popupProject.title(projectName)
        connect_, cursor_ = ES.get_student_db_ES()
        cursor_.execute('SELECT * FROM projects WHERE name=(:name)', {'name':projectName})
        project = cursor_.fetchone()

        Label(popupProject, text='Organisation').grid(row=1, column=0, sticky=W, padx=10)
        Label(popupProject, text='Incharge').grid(row=2, column=0, sticky=W, padx=10)
        Label(popupProject, text='Duration').grid(row=3, column=0, sticky=W, padx=10)
        Label(popupProject, text='Status').grid(row=4, column=0, sticky=W, padx=10)
        Label(popupProject, text='Name').grid(row=5, column=0, sticky=W, padx=10)

        Label(popupProject, text=project[0]).grid(row=1, column=1, sticky=W)
        Label(popupProject, text=project[1]).grid(row=2, column=1, sticky=W)
        Label(popupProject, text=project[2]).grid(row=3, column=1, sticky=W)
        Label(popupProject, text=project[3]).grid(row=4, column=1, sticky=W)
        Label(popupProject, text=project[4], anchor=W, justify='left').grid(row=5, column=1, sticky=W)



    def new(self, root):
        self.clear()
        ProjectNew.ProjectNew(root)


if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    DepartmentProject(root)