import tkinter
from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
from student_1 import student
from train import Train_Data
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help_Desk
from developer import Developer
import os


class face_recognition_system:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        # First image

        img = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\crowd.png")
        img = img.resize((1275, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1275, height=200)

        # bg image

        img2 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\wallpaper.jpg")
        img2 = img2.resize((1275, 500), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=200, width=1275, height=500)

        title_lbl = Label(bg_img, text="Face Recognition Attandance System", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1275, height=50)

        # student detail button

        img3 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\student.jpg")
        img3 = img3.resize((170, 100), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img, command=self.student_details, image=self.photoimg3, cursor="hand2")
        b1.place(x=50, y=50, width=170, height=100)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=50, y=148, width=170, height=30)

        # face detect button

        img4 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\facial recognition.jpg")
        img4 = img4.resize((170, 100), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command = self.Face_Recognition, cursor="hand2")
        b1.place(x=300, y=50, width=170, height=100)

        b1_1 = Button(bg_img, text="Face Detect", cursor="hand2",command = self.Face_Recognition,
                      font=("times new roman", 15, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=300, y=148, width=170, height=30)

        # attandance button

        img5 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\attendance.jpg")
        img5 = img5.resize((170, 100), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,command = self.Attendance, cursor="hand2")
        b1.place(x=550, y=50, width=170, height=100)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command = self.Attendance,
                      font=("times new roman", 15, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=550, y=148, width=170, height=30)

        # help face button

        img6 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\help desk.png")
        img6 = img6.resize((170, 100), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,command = self.Help_Desk, cursor="hand2")
        b1.place(x=800, y=50, width=170, height=100)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command = self.Help_Desk,
                      font=("times new roman", 15, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=800, y=148, width=170, height=30)

        # train face data desk button

        img7 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\train data.jpg")
        img7 = img7.resize((170, 100), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,command = self.Train_data, cursor="hand2")
        b1.place(x=1050, y=50, width=170, height=100)

        b1_1 = Button(bg_img, text="Train Data Face",command = self.Train_data, cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=1050, y=149, width=170, height=30)

        # photos buttons

        img8 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\photo data.png")
        img8 = img8.resize((170, 100), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, command=self.open_img, cursor="hand2")
        b1.place(x=200, y=300, width=170, height=100)

        b1_1 = Button(bg_img, text="Photos Data", cursor="hand2", command=self.open_img,
                      font=("times new roman", 15, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=200, y=400, width=170, height=30)

        # developer button

        img9 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\developer.jpg")
        img9 = img9.resize((170, 100), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,command = self.Developer, cursor="hand2")
        b1.place(x=500, y=300, width=170, height=100)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command = self.Developer,
                      font=("times new roman", 15, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=500, y=400, width=170, height=30)

        # exit button

        img10 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\exit.png")
        img10 = img10.resize((170, 100), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,command = self.Exit, cursor="hand2")
        b1.place(x=800, y=300, width=170, height=100)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command = self.Exit,
                      font=("times new roman", 15, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=800, y=400, width=170, height=30)

    def open_img(self):
        os.startfile("img data")

        # ========= function button to call on main window =============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def Train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train_Data(self.new_window)

    def Face_Recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Help_Desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_Desk(self.new_window)

    def Developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def Exit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
