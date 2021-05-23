import glob
import os
import shutil
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from pathlib import Path

root = Tk()
root.title('Clean Desk')
root.geometry("500x200")

lbl1 = Label(root, text='Select the Source folder').place(x=50, y=50)
btn1 = Button(root, text='Proceed', command=lambda: openfunc(source1))
btn1.place(x=375, y=75)
source1 = tk.Entry(root)
source1.place(x=50, y=100)


#    global chg
#    source = filedialog.askdirectory(parent=root, title='Select folder')

def openfunc(source1):
    source = source1.get()
    print(source)
    for(path, dirs, files) in os.walk(source):
        for file in files:
            filetype = file.split('.')[1]
            print(filetype)
            if os.path.exists(source + "\\" + filetype) == True:
                print(source + filetype + 'yay')
                if file.endswith(filetype):
                    shutil.move(file, source + '\\' + filetype)
            else:
                print(source + filetype + 'no')
                os.mkdir(source + '\\' + filetype)
                shutil.move(file, source + '\\' + filetype)


root.mainloop()
# command=lambda: openfunc())
