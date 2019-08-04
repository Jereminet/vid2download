from tkinter import *

root = Tk()

one = Label(root, text="Option", bg="red", fg="blue")
one.grid(row=0)

entry1 = Entry(root)
entry1.grid(row=1,column=1)

root.mainloop()