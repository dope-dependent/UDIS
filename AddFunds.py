import DepartmentAccount
import ES
from tkinter import *
from tkinter import messagebox
import datetime

class AddFunds:
    def __init__(self, root):
        root.title('Add Funds')
        self.frame = Frame(root, bg='white')
        self.frame.grid(row=0, column=0, sticky='nsew')

        root.geometry('400x400')
        root.minsize(400, 400)
        root.maxsize(400, 400)

        Label(self.frame, text='Donor', anchor='w', bg='white').grid(row=1, column=0)
        Label(self.frame, text='Amount', anchor='w', bg='white').grid(row=2, column=0)
        Label(self.frame, text='Date', anchor='w', bg='white').grid(row=3, column=0)
        Label(self.frame, text='Purpose', anchor='w', bg='white').grid(row=4, column=0)

        self.donorEntry = Entry(self.frame)
        self.amountEntry = Entry(self.frame)
        self.dateEntry = Entry(self.frame)
        self.purposeEntry = Entry(self.frame)

        self.donorEntry.grid(row=1, column=1)
        self.amountEntry.grid(row=2, column=1)
        self.dateEntry.grid(row=3, column=1)
        self.purposeEntry.grid(row=4, column=1)

        self.submitButton = Button(self.frame, text='Add Funds', anchor=W, command=lambda: self.submit(root))

        self.backButton = Button(self.frame, text='Back', command=lambda: self.back(root))
        self.exitButton = Button(self.frame, text='Exit', command=exit)

        self.submitButton.grid(row=5, columnspan=2, pady=50)

        self.exitButton.grid(row=7, column=0, sticky=N + W, padx=50, pady=50)
        self.backButton.grid(row=7, column=1, sticky=N + E, padx=50, pady=50)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)

        root.mainloop()

    def submit(self, root):
        donor_ = self.donorEntry.get()
        amount_ = self.amountEntry.get()
        date_ = self.dateEntry.get()
        purpose_ = self.purposeEntry.get()
        try:
            AddFunds.addfunds(donor_, amount_, date_, purpose_)
            messagebox.showinfo('Funds', 'Added successfully')
            self.clear()
            DepartmentAccount.DepartmentAccount(root)
        except Exception as e:
            messagebox.showwarning('Adding Funds', e)

    @staticmethod
    def addfunds(donor_, amount_, date_, purpose_):
        lengths = [len(i) for i in [donor_, amount_, date_, purpose_]]
        if 0 in lengths:
            raise Exception('One or more fields left blank')

        connect_, cursor_ = ES.get_student_db_ES()
        try:
            amount_ = int(amount_)
        except ValueError:
            raise Exception('Amount is not a valid number')
        if not amount_ > 0:
            raise Exception('Amount is not a positive number')

        try:
            datetime.datetime.strptime(date_, '%d/%m/%Y')
        except ValueError:
            raise Exception('Incorrect Date Format')

        with connect_:
            cursor_.execute('INSERT INTO transactions VALUES (:donor, :amount, :date, :purpose)',
                            {'donor': donor_, 'amount': amount_, 'date': date_, 'purpose': purpose_})

            cursor_.execute('SELECT * from total')
            amount = (cursor_.fetchone())[0]
            cursor_.execute('UPDATE total SET amount=(:n_amt) WHERE amount=(:o_amt)',
                            {'n_amt': amount + amount_, 'o_amt': amount})

    def back(self, root):
        self.clear()
        DepartmentAccount.DepartmentAccount(root)

    def clear(self):
        self.frame.destroy()