import DepartmentUDIS
from tkinter import *
import AddFunds
import ES


class DepartmentAccount:
    def __init__(self, root):
        root.title('Department-Account')
        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        connect_, cursor_ = ES.get_student_db_ES()
        cursor_.execute('SELECT * FROM total')
        amount = (cursor_.fetchone())[0]

        self.addButton = Button(self.frame, text='Add Funds', anchor=W, command=lambda: self.addFunds(root))
        self.totalAmount = Label(self.frame, text='Total Amount : Rs. ' + str(amount) , anchor=W)

        self.backButton = Button(self.frame, text='Back', command=lambda: self.back(root))
        self.exitButton = Button(self.frame, text='Exit', command=exit)

        self.addButton.grid(row=0)
        self.totalAmount.grid(row=1, sticky=W)

        self.exitButton.grid(row=3, sticky=N+W)
        self.backButton.grid(row=3, sticky=N+E)

        self.frame.rowconfigure(2, weight=1)

        self.viewPassbook(root)

        self.frame.columnconfigure(0, weight=1)

        root.mainloop()

    def back(self, root):
        self.clear()
        DepartmentUDIS.DepartmentMainMenu(root)

    def clear(self):
        self.frame.destroy()

    def addFunds(self, root):
        self.clear()
        AddFunds.AddFunds(root)

    def viewPassbook(self, root):
        # Make a frame inside the self.frame in the row = 3.
        displayPassbook = Frame(self.frame)
        displayPassbook.grid(row=2, sticky=E+W+N+S)
        Label(displayPassbook, text='Organisation', relief=GROOVE).grid(row=0, column=0, sticky=E+W)
        Label(displayPassbook, text='Amount', relief=GROOVE).grid(row=0, column=1, sticky=E+W)
        Label(displayPassbook, text='Date', relief=GROOVE).grid(row=0, column=2, sticky=E+W)
        Label(displayPassbook, text='Purpose', relief=GROOVE).grid(row=0, column=3, sticky=E+W)

        connect_, cursor_ = ES.get_student_db_ES()
        cursor_.execute('SELECT * FROM transactions')

        allTransactions = cursor_.fetchall()
        allTransactions.reverse()

        for i, transaction in enumerate(allTransactions):
            if transaction[1] > 0:
                bg = '#6F6'
            else:
                bg = '#F99'
            Label(displayPassbook, text=transaction[0], bg=bg).grid(row=i + 1, column=0)
            Label(displayPassbook, text=transaction[1], bg=bg).grid(row=i + 1, column=1)
            Label(displayPassbook, text=transaction[2], bg=bg).grid(row=i + 1, column=2)
            Label(displayPassbook, text=transaction[3], bg=bg).grid(row=i + 1, column=3)

        displayPassbook.columnconfigure(0, weight=1)
        displayPassbook.columnconfigure(3, weight=2)
