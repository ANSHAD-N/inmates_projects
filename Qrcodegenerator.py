from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
root = Tk()

def qr():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name+".png"
    url = pyqrcode.create(link)
    url.png(file_name,scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image=image
    canvas.create_window(200,260, window=image_label)


canvas = Canvas(root, height=600, width=300)
canvas.pack()
app_label = Label(root, text="QR Code Generator", fg ='blue',font=('Arial',30) )
canvas.create_window(200, 50,window=app_label)

name_label = Label(root, text="link Name")
link_label = Label(root, text='link')
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 190, window=link_entry)

button= Button(text="Generate QR Code",command=qr)
canvas.create_window(200, 220, window=button)


root.mainloop()
