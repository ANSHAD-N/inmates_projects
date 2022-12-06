from tkinter import *

class my_fun:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.pbutton = Button(frame,text="click", command= self.pmsg)
        self.pbutton.pack()

        self.qbutton = Button(frame,text= "quit", command = frame.quit)
        self.qbutton.pack(side= "left")

    def pmsg(self):
        print("clicked")

root = Tk()
obj = my_fun(root)
root.mainloop()


