
# q1

import tkinter as tk
from tkinter import *
r=tk.Tk()
r.title("info")
dict={'name':'isha','mobile_number':9815039634}
scrollbar=Scrollbar(r)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(r,yscrollcommand= scrollbar.set)
for key in dict.__iter__():
        mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def quit():
    r.quit()
b=Button(r,text="enter",command=quit)
b.pack()
r.mainloop()


#question2

def update():
    dict.update({"age":21})
    print(dict)
button1=Button(r,text='good',command=update())
button1.pack()
r.mainloop()