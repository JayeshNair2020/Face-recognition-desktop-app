from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Student details")
        self.root.geometry("1366x768+0+0")

if __name__=="__main__":
    root=Tk()
    app=Attendance(root)
    root.mainloop()