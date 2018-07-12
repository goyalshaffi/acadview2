# q1
'''

import tkinter as tk
from tkinter import *
def hello():
    print("hello world")
def close_window():
    r.destroy()
r=tk.Tk()
r.title('counting seconds')
button=tk.Button(r,text='stop',width=25,command=hello)
button.pack(side=tk.LEFT)
button=tk.Button(r,text='exit',width=25,command=close_window)
button.pack(side=tk.LEFT)
r.mainloop()


# q2
import tkinter as tk
from tkinter import *
def hello():
    print("hello world")
def close_window():
    r.destroy()
def write_text():
    print("hello friends")
r=tk.Tk()
r.title('counting seconds')
button=tk.Button(r,text='stop',width=25,command=hello)
button.pack(side=tk.LEFT)
button=tk.Button(r,text='exit',width=25,command=close_window)
button.pack(side=tk.LEFT)
button=tk.Button(r,text='action',width=25,command=write_text)
button.pack(side=tk.BOTTOM)
r.mainloop()


# q3
import tkinter as tk
from tkinter import *
def close_window():
    r.destroy()
r=Tk()
frame=Frame(r)
frame.pack()
bottomframe=Frame(r)
bottomframe.pack(side=BOTTOM)
var=StringVar()
label=Label(r,text='unchanged')
def change():
    label.config(text="changed")
label.pack(side=LEFT)
button=tk.Button(r,text='exit',width=25,command=close_window)
button.pack(side=tk.LEFT)
button=tk.Button(r,text='update',width=25,command=change)
button.pack(side=tk.LEFT)
r.mainloop()

'''

# q4

import tkinter as tk
from tkinter import *
r=Tk()
l1=Label(r,text="first name").grid(row=0)
l2=Label(r,text="second name").grid(row=1)
e1=Entry(r)
e2=Entry(r)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
r.mainloop()



