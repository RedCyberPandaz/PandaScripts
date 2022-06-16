import subprocess
import sys
import PySimpleGUI as sg
import tkinter as tk
from tkinter import ttk
from tkinter import * 



root = Tk()
#this is the declaration of the variable associated with the checkbox
var1 = tk.IntVar()



# this is the function that increases the progress bar value
def makeProgress():
	Workin['value']=Workin['value'] + 1
	root.update_idletasks()

# this line prepares the dothething button to be loaded after you check the box.
def cangetthething():
	Button(root, text='Do the thing', bg='#BB0000', font=('arial', 12, 'normal'), command=dothething).place(x=110, y=265)


# this is the section of code that creates a checkbox
CheckBoxOne=Checkbutton(root, text='Promise not to sue me?', variable=var1, onvalue=1, offvalue=0, command=cangetthething, bg='#FFFF00', font=('arial', 12, 'normal'))
CheckBoxOne.place(x=203, y=47)



# This is the section of code that creates the main window
root.geometry('735x457')
root.configure(background='#FF0000')
root.title('Doin a thing')



# this is a function to check the status of the checkbox
def getCheckboxValue():
	checkedOrNot = var1
	print(checkedOrNot)


# this is the function called when dothething is clicked ie the main script
def dothething():
	subprocess.Popen("ls /usr/share/vulkan/icd.d/",shell=True)


# this is the function called when dontdothething is clicked
def dontdothething():
	exit()



# this is the section of code that gives the progress bar a color
Workin_style = ttk.Style()
Workin_style.theme_use('clam')
Workin_style.configure('Workin.Horizontal.TProgressbar', foreground='#FF0000', background='#FF0000')


# this is the section of code that creates a progress bar
Workin=ttk.Progressbar(root, style='Workin.Horizontal.TProgressbar', orient='horizontal', length=640, mode='determinate', maximum=100, value=1)
Workin.place(x=72, y=127)


# this is the section of code that creates a button
Button(root, text='Nah this is sketchy.', bg='#44f700', font=('arial', 12, 'normal'), command=dontdothething).place(x=421, y=331, height=150, width=300)



root.mainloop()
