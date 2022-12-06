from tkinter import *
root = Tk()

my_menu = Menu(root)
root.config(menu=my_menu)

menu1 = Menu(my_menu)
my_menu.add_cascade(label="file", menu=menu1)
menu1.add_command(label="help")

toolbar = Frame(root, bg="pink")
inbutton = Button(toolbar, text="crop")
inbutton.pack(side="left", padx=2, pady=2)
toolbar.pack(side="top", fill=X)

statusbar = Label(root, text="this is a statusbar", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
