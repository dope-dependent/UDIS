from tkinter import *
import ES


class StudentsView:
    def __init__(self, root):

        root.title('UDIS-View Student')
        self.frame = Frame(root)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.name_label_StudentsView = Label(self.frame, text='Name', fg="black")
        self.name_entry_StudentsView = Entry(self.frame, borderwidth=0)
        self.roll_label_StudentsView = Label(self.frame, text='Roll No', fg="black")
        self.roll_entry_StudentsView = Entry(self.frame, borderwidth=0)

        self.submit_button_StudentsView= Button(self.frame, text='Search')

        self.name_label_StudentsView.grid(row=2, column=0, padx=5, pady=3)
        self.name_entry_StudentsView.grid(row=2, column=1)
        self.roll_label_StudentsView.grid(row=3, column=0, padx=5, pady=3)
        self.roll_entry_StudentsView.grid(row=3, column=1)

        self.submit_button_StudentsView.grid(row=4, column=0,columnspan=2,pady=20)

        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        root.mainloop()

    def clear(self):
        self.frame.destroy()




if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    StudentsView(root)
