from tkinter import *
from playsound import playsound
import os
from datetime import datetime

#creating instance of tk
root = Tk()

root.configure(background = "White")

def function1():
    os.system("python datasetCapture.py")

def function2():
    os.system("python trainingDataset.py")

def function3():
    os.system("python recognizer.py")
    playsound("sound.mp3")

def attend():
    os.startfile(os.getcwd()+"\\attendance_files\\attendance"+str(datetime.now().date())+'.xls')


def function4():
    root.destroy()

#title for the window
root.title("BOIMETRIC ATTENDANCE USING FACE RECOGNITION")

#creating a text label
Label(root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg='white',bg="blue",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#3e4e66",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#3e4e66",fg="white",command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="#3e4e66",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#3e4e66",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


# Exit
Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function4).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
