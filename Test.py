from ES import ES
from tkinter import *


if __name__ == '__main__':
    root = Tk()
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.geometry('800x600')
    root.configure(background="blue")
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    ES(root)
