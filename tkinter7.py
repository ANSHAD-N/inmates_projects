from tkinter import *
from tkinter import messagebox
root = Tk()

messagebox.showinfo('title',"this is test")
messagebox.showwarning('warning',"this is a warning")
messagebox.showerror('error',"this is an error")

messagebox.askquestion('question', "are you ok")
messagebox.askokcancel('ok', "is it ok ")
messagebox.askyesno('yn',"say yes or no")
messagebox.askretrycancel('ret',"retry?")

root.mainloop()