from tkinter import *
root = Tk()
label = Label(root, text="button").pack()
frame1 = Frame(root).pack()
but = Button(root, text="login", fg = "red", bg="blue")
but.pack()

root.mainloop()