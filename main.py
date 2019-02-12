#Importing modules
from tkinter import *
from tkinter import ttk

#Main Window
root = Tk()
root.title("MWWP")

frame = Frame(root)
labelText = StringVar()

label = Label(frame, textvariable=labelText)
button = Button(frame, text="Import")

labelText.set("Choose image to classify")

#Geometry manager, defines how your components are arranged
label.pack()
button.pack()
frame.pack()

root.mainloop()
