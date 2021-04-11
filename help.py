from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Help_Desk:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x680+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="Help Desk",
                         font=("times new roman", 35, "bold"),
                          bg="white", fg="purple")
        title_lbl.place(x=0, y=0, width=1275, height=50)

        img_left = Image.open(r"D:\py\pythonProject2\College images\help 1.jpg")
        img_left = img_left.resize((1275, 700), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=50, width=1275, height=650)

        title = Label(f_lbl,text="Email :- rpnilesh88@gmail.com",relief = RIDGE,
                      font=("times new roman", 35, "bold"),
                      fg="black")
        title.place(x=330, y=387, width=660, height=71)




if __name__ == "__main__":
    root = Tk()
    obj = Help_Desk(root)
    root.mainloop()
