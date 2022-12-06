from tkinter import *

root = Tk()

def fun():
    print("Have some fun")

button1 = Button(root,text="Ok",command = fun).pack()


root.mainloop()
