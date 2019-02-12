#importing modules
from tkinter import *
from tkinter import ttk

#main window
root = Tk()
root.title("MWWP")

Label(root, text="Choose image to classify").grid(row=1,column=1, sticky=W, padx=5)
Button(root, text="Import").grid(row=2, column=1)

Label(root, text="Begin the process").grid(row=1, column=2, sticky=W, padx=5)
Button(root, text="Import").grid(row=2, column=2)

root.mainloop()

