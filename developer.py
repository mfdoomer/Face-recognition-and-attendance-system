from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Developer:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x680+0+0")
        self.root.title("Face Recognition System")

        right_frame = LabelFrame(self.root, bd=2, bg="white", relief=RIDGE,
                                 font=("times new roman", 15, "bold"))
        right_frame.place(x=0, y=0, width=1275, height=152)

        title_lbl = Label(right_frame,text="Developer Name :- Nilesh Rajpurohit",
                         anchor=CENTER,
                         font=("times new roman", 30, "bold"),
                         bg="white", fg="gray")
        title_lbl.place(x=23, y=0, width=1275, height=70)

        title_lbl = Label(right_frame,text="Contact info :- 809799352",
                          anchor=CENTER,
                          font=("times new roman", 30, "bold"),
                          bg="white", fg="gray")
        title_lbl.place(x=0, y=65, width=1275, height=70)

        img_left = Image.open(r"D:\py\pythonProject2\College images\dev.jpg")
        img_left = img_left.resize((1275, 645), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=150, width=1275, height=650)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
