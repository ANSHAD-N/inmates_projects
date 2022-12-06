from tkinter import *
root = Tk()
label1 = Label(root, text="User name")
label2 = Label(root, text="Enter mobile number")
label3 = Label(root, text="Enter email")
label4 = Label(root, text="Enter age")
label5 = Label(root, text="Enter Password")
label6 = Label(root, text="confirm Password")

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)

button1 = Button(root, text="Login", bg="green")
button2 = Button(root, text="Cancel", bg="red")

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

label3.grid(row = 2,column=0)
entry3.grid(row = 2, column=1)

label4.grid(row = 3,column=0)
entry4.grid(row = 3, column=1)

label5.grid(row = 4,column = 0)
entry5.grid(row = 4, column = 1)

label6.grid(row = 5,column = 0)
entry6.grid(row = 5, column = 1)

button1.grid(row = 6,column = 0)
button2.grid(row = 6, column = 1)


root.mainloop()