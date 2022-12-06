from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas = Canvas(root, height=400, width=200)
canvas.pack()
def texttospeach():
    text = open('demo.txt', 'r').read()
    output = gTTS(text=text, lang='en', slow=False)
    output.save("output.mp3")
    os.system('start output.mp3')


entry = Entry(root)
canvas.create_window(180, 120, window=entry)
button = Button(text='start', command=texttospeach)
canvas.create_window(200, 140, window=button)
root.mainloop()


