import parser
from tkinter import *

root = Tk()
root.title("calculator")
display=Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)
#get the user input and place it in display area
i=0
def get_variable(num):
    global i
    display.insert(i, num)
    i+=1


#clear user input
def clear_all():
    display.delete(0, END)


def delete():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0, "Error")


#get operator function
def get_operator(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i+=length


def calculate():
    entire_string = display.get()
    try:
        a= parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

#adding button
Button(root, text="1", command=lambda :get_variable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda :get_variable(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda :get_variable(3)).grid(row=2, column=2)
Button(root, text="4", command=lambda :get_variable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda :get_variable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda :get_variable(6)).grid(row=3, column=2)
Button(root, text="7", command=lambda :get_variable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda :get_variable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda :get_variable(9)).grid(row=4, column=2)
Button(root, text="0", command=lambda : get_variable(0)).grid(row=5, column=0)
Button(root, text="AC", command=lambda :clear_all()).grid(row=5, column=1)
Button(root, text="->", command=lambda :delete()).grid(row=5, column=3)
Button(root, text="=", command=lambda :calculate()).grid(row=5, column=2)
Button(root, text="+", command=lambda :get_operator('+')).grid(row=6, column=0)
Button(root, text="-", command=lambda :get_operator('-')).grid(row=6, column=1)
Button(root, text=".", command=lambda :get_operator('.')).grid(row=6, column=2)
Button(root, text="*", command=lambda :get_operator('*')).grid(row=7, column=0)
Button(root, text="%", command=lambda :get_operator('%')).grid(row=7, column=1)
Button(root, text="^2", command=lambda :get_operator('**2')).grid(row=7, column=2)
Button(root, text="pi", command=lambda :get_operator('*3.14')).grid(row=8, column=0)
Button(root, text="(", command=lambda :get_operator('(')).grid(row=8, column=1)
Button(root, text=")", command=lambda :get_operator(')')).grid(row=8, column=2)
Button(root, text="exp", command=lambda :get_operator('**')).grid(row=9, column=0)
Button(root, text="!").grid(row=9, column=1)




root.mainloop()