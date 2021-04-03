import DepartmentAccount
import ES
from tkinter import *


class AddFunds:
    def __init__(self, root):
        root.title('Add Funds')
        print('account')
        self.frame = Frame(root)
        self.frame.grid(row=0, column=0, sticky='nsew')

        Label(self.frame, text='Donor', anchor='w').grid(row=0, column=0)
        Label(self.frame, text='Amount', anchor='w').grid(row=1, column=0)
        Label(self.frame, text='Date', anchor='w').grid(row=2, column=0)
        Label(self.frame, text='Purpose', anchor='w').grid(row=3, column=0)

        self.donorEntry = Entry(self.frame)
        self.amountEntry = Entry(self.frame)
        self.dateEntry = Entry(self.frame)
        self.purposeEntry = Entry(self.frame)

        self.donorEntry.grid(row=0, column=1)
        self.amountEntry.grid(row=1, column=1)
        self.dateEntry.grid(row=2, column=1)
        self.purposeEntry.grid(row=3, column=1)

        self.submitButton = Button(self.frame, text='Add Funds', anchor=W, command=lambda: self.submit(root))

        self.backButton = Button(self.frame, text='Back', command=lambda: self.back(root))
        self.exitButton = Button(self.frame, text='Exit', command=exit)

        self.submitButton.grid(row=5, columnspan=2)

        self.exitButton.grid(row=7, column=0, sticky=N + E)
        self.backButton.grid(row=7, column=1, sticky=N + W)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(6, weight=1)

        print(3)
        root.mainloop()

    def submit(self, root):
        connect_, cursor_ = ES.get_student_db_ES()
        donor_ = self.donorEntry.get()
        amount_ = int(self.amountEntry.get())
        date_ = self.dateEntry.get()
        purpose_ = self.purposeEntry.get()

        with connect_:
            cursor_.execute('INSERT INTO transactions VALUES (:donor, :amount, :date, :purpose)',
                            {'donor': donor_, 'amount': amount_, 'date': date_, 'purpose': purpose_})

            cursor_.execute('SELECT * from total')
            amount = (cursor_.fetchone())[0]
            print(type(amount))
            cursor_.execute('UPDATE total SET amount=(:n_amt) WHERE amount=(:o_amt)',
                            {'n_amt': amount + amount_, 'o_amt': amount})

    def back(self, root):
        self.clear()
        DepartmentAccount.DepartmentAccount(root)

    def clear(self):
        self.frame.destroy()