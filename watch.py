#!/usr/bin/python2.7
"""Blank Python 2.7 file"""
from Tkinter import *
from time import strftime

root = Tk()

time_var = StringVar()

def set_time():
    time_var.set(strftime('%H:%M:%S'))
    root.after(1000, set_time)

Label(root, bd=11, textvariable=time_var).pack()
set_time()
root.mainloop()