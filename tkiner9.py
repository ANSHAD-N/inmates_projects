from tkinter import *
root = Tk()

my_menu = Menu(root) #initializing menu
root.config(menu=my_menu) #configure menu

sub_menu = Menu(my_menu)#create menu
my_menu.add_cascade(label="file", menu= sub_menu) #for menu label
sub_menu.add_command(label="save") #for submenu label
sub_menu.add_separator() #for seperator
sub_menu.add_command(label="quit") #for submenu label


new_menu = Menu(my_menu)

my_menu.add_cascade(label="edit", menu = new_menu)
new_menu.add_command(label="undo")


root.mainloop()