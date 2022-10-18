# %%
from tkinter import *
win = Tk()
win.title('Choosing with Radiobutton')
win.geometry('280x70')


def show():
    select = word.get()
    label.config(text='I love ' + select + '.')


word = StringVar()
radio1 = Radiobutton(win, text='Java', variable=word,
                     value='coding in Java', command=show)
radio1.select()
radio2 = Radiobutton(win, text='Python', variable=word,
                     value='coding in Python', command=show)
label = Label(win)
radio1.pack()
radio2.pack()
label.pack()
win.mainloop()
