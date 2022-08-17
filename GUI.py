from tkinter import *
master = Tk()
def close_window():
    exit()
for i in range(0,5):
    for j in range(0,5):
        button = Button(master, text = 'Click me', command = close_window)
button.pack()
mainloop()