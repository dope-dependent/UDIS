from tkinter import *
import DepartmentInventory
import ES

def dropdown_defocus(event):
    event.widget.selection_clear()

class DepartmentPurchase:
    def __init__(self,root):
        root.maxsize(400,400)

        self.frame=Frame(root)
        self.frame.grid(row=0,column=0,sticky="nsew")

        self.nameLabel= Label(self.frame,text="Name")
        self.typeLabel= Label(self.frame,text="Type")
        self.quantityLabel= Label(self.frame,text="Quantity")
        self.totpriceLabel= Label(self.frame,text="Total Price")
        self.dateLabel= Label(self.frame,text="Date of purchase")
        self.locationLabel= Label(self.frame,text="Location")

        self.nameEntry = Entry(self.frame,borderwidth=0)

        self.combostyle=ttk.Style()
        self.combostyle.map('TCombobox', fieldbackground=[('readonly', 'white')])
        self.combostyle.map('TCombobox', selectbackground=[('readonly', 'white')])

        self.var=StringVar(self.frame)
        self.var.set("Miscellaneous")
        self.typeDropdown = ttk.Combobox(self.frame,foreground="black",width=27,takefocus=False,textvariable=self.var,state='readonly')
        self.typeDropdown['value']=('Miscellaneous',
                                        'Computers',
                                        'Furniture',
                                        'Stationery')
        self.typeDropdown.bind("<FocusIn>", dropdown_defocus)

        self.quantityEntry = Entry(self.frame,borderwidth=0)
        self.totpriceEntry = Entry(self.frame,borderwidth=0)
        self.dateEntry = Entry(self.frame,borderwidth=0)
        self.locationEntry = Entry(self.frame,borderwidth=0)

        self.nameLabel.grid(row=0,column=0,sticky=E+S,padx=5,pady=3)
        self.typeLabel.grid(row=1,column=0,sticky=E,padx=5,pady=3)
        self.quantityLabel.grid(row=2,column=0,sticky=E,padx=5,pady=3)
        self.totpriceLabel.grid(row=3,column=0,sticky=E,padx=5,pady=3)
        self.dateLabel.grid(row=4,column=0,sticky=E,padx=5,pady=3)
        self.locationLabel.grid(row=5,column=0,sticky=E,padx=5,pady=3)

        self.purchaseButton=Button(self.frame,text="Purchase",command=lambda:self.purchase())
        self.backButton=Button(self.frame,text="Back",command=lambda:self.back(root))
        self.exitButton=Button(self.frame,text="Exit",command=exit)

        self.nameEntry.grid(row=0,column=1,sticky=W+S+E,padx=5,pady=3)
        self.typeDropdown.grid(row=1,column=1,sticky=W+E,padx=5,pady=3)
        self.quantityEntry.grid(row=2,column=1,sticky=W+E,padx=5,pady=3)
        self.totpriceEntry.grid(row=3,column=1,sticky=W+E,padx=5,pady=3)
        self.dateEntry.grid(row=4,column=1,sticky=W+E,padx=5,pady=3)
        self.locationEntry.grid(row=5,column=1,sticky=E+W,padx=5,pady=3)

        self.purchaseButton.grid(row=6,columnspan=2,column=0,pady=10)
        self.backButton.grid(row=7,columnspan=2,column=0,sticky=E,padx=50,pady=50)
        self.exitButton.grid(row=7,columnspan=2,column=0,sticky=W,padx=50,pady=50)

        self.frame.rowconfigure(0,weight=1)
        self.frame.rowconfigure(7,weight=1)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=2)

    def purchase(self):
        name_=self.nameEntry.get()
        type_=self.typeDropdown.get()
        quantity_=self.quantityEntry.get()
        price_=int(self.totpriceEntry.get())
        date_=self.dateEntry.get()
        location_=self.locationEntry.get()

        connect_,cursor_=ES.get_student_db_ES()
        with connect_:
            cursor_.execute("INSERT INTO inventory VALUES (:name,:location,:quantity,:type,:price)",
                    {'name':name_,'location':location_,'quantity':quantity_,'type':type_,'price':price_})
            cursor_.execute("INSERT INTO transactions VALUES (:organisation,:amount,:date,:purpose)",
                    {'organisation':'Self','amount':-price_,'date':date_,'purpose':'Purchased '+name_})

            cursor_.execute('SELECT * from total')
            amount = (cursor_.fetchone())[0]
            if amount < price_:
                print("insufficient funds")
            cursor_.execute('UPDATE total SET amount=(:n_amt) WHERE amount=(:o_amt)',
                            {'n_amt': amount - price_, 'o_amt': amount})

            cursor_.execute('SELECT * from total')
            amount = (cursor_.fetchone())[0]
            print(amount)

    def back(self,root):
        self.clear()
        root.minsize(800,600)
        DepartmentInventory.DepartmentInventory(root)

    def clear(self):
        self.frame.destroy()