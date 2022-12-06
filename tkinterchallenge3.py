from tkinter import *
from tkinter import messagebox

class mex:
    def __init__(self,root1):
        frame = Frame(root1)
        frame.pack()

        self.label1 = Label(frame, text="Ok",bg = "green")
        self.label1.pack(fill=X)
        self.button1 = Button(frame, text="clicked", command = self.ok)
        self.button1.pack()

        self.label2 = Label(frame, text="Cancel", bg="yellow").pack(fill=X)
        self.button2 = Button(frame, text="Cancel", command = self.cancel)
        self.button2.pack()

        self.label3 = Label(frame, text="Exit", bg="red").pack(fill=X)
        self.button3 = Button(frame, text="Exit", command=frame.quit)
        self.button3.pack()

    def ok(self):
        messagebox.showinfo('ok',"Clicked")

    def cancel(self):
        messagebox.showwarning('cancel',"Canceled")

root = Tk()
obj = mex(root)
root.mainloop()

