import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def button_clicked():
    print('Button clicked')

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

def select(option):
    print(option)

def callbackFunc1(s):
    print('Callback Function 1: Length of the text file is : ', s)

def callbackFunc2(s):
    print('Callback Function 2: Length of the text file is : ', s)

def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)

ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()

root.mainloop()

if __name__ == '__main__':
    printFileLength("sample.txt", callbackFunc1)
    printFileLength("sample.txt", callbackFunc2)