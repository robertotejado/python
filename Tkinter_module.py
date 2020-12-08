#print("Tkinter Module")

#import tkinter as tk # Python 3.x Version
#import Tkinter as tk # Python 2.x Version


##############################################
'''
import tkinter as tk # Python 3.x Version
root = tk.Tk()

label = tk.Label(root, text="Hello World!") # Create a text label
label.pack(padx=20, pady=20) # Pack it into the window

btn=tk.Button() 
btn.pack(padx=40, pady=40)
btn["text"]="Hello everyone!"

def click():
    print("You just clicked me!")
    btn["text"]="You just clicked me!"
btn["command"]=click 

root.mainloop()
'''

#################################################
'''

import tkinter as tk # Python 3.x Version
from tkinter import * 

root = tk.Tk()

logo = tk.PhotoImage(file="./PiLogo.gif")
w1= Label(root,root.title("Raspberry Pi"), image=logo).pack(side="left")
content = " The Raspberry Pi Foundation is a UK-based charity that works to puit the power of \ncomputing and digital making into the hands of people all over the world.We do \nthis so that more people are able to harness the power of computing and digital\n technologies for ork, to solve problems that matter to them, and to express themselves creatively."
w2=Label(root, justify=LEFT,padx=10,text=content).pack(side="right")
root.mainloop()
'''
#################################################
'''
import tkinter as tk # Python 3.x Version
from tkinter import * 

root = tk.Tk()

v=IntVar()
Label(root,root.title("Options"), text="Choose a preferred language:", justify=LEFT, padx=20).pack()

Radiobutton(root,text="Python",padx=20,variable=v,value=1).pack(anchor=W)

Radiobutton(root,text="C++",padx=20,variable=v,value=2).pack(anchor=W)

btn=tk.Button() 
btn.pack(padx=40, pady=40)
btn["text"]="Click Here!"

def click():
    print("You just clicked me!")
    btn["text"]="You just clicked me!"
btn["command"]=click 

root.mainloop()
'''

##################################################3
   

import tkinter as tk # Python 3.x Version
from tkinter import * 

root = tk.Tk()

def var_states():
    print("Warrior: %d,\nMage: %d" % (var1.get(), var2.get()))

Label(root, root.title("Adventure Game"), text=">>>>>>>>>>>>Your Adventure Role<<<<<<<<<<<<<<<<<<<<<<<<<<").grid(row=0,sticky=N)

var1= IntVar()
Checkbutton(root, text="Warrior", variable=var1).grid(row=1,sticky=W)

var2=IntVar()
Checkbutton(root, text="Mage", variable=var2).grid(row=2,sticky=W)

Button(root,text='Quit', command=root.destroy).grid(row=3,sticky=W,pady=4)

Button(root,text='Show', command=var_states).grid(row=3,sticky=E,pady=4)

root.mainloop()