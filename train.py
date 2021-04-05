from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train_Data:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x680+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1275, height=50)

        img_top = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\train data 1.jpg")
        img_top = img_top.resize((1290, 255), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1290, height=255)

        btn = Button(self.root, text="Train Data", command=self.train_classifier, width=30,
                     font=("times new roman", 30, "bold"), bg="gray", fg="darkblue")
        btn.place(x=0, y=300, width=1275, height=90)

        img_top1 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\train data 2.jpg")
        img_top1 = img_top1.resize((1275, 455), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=0, y=390, width=1275, height=455)

    def train_classifier(self):
        data_dir = "img data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # gray scale conversion
            imgnp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imgnp)
            ids.append(id)
            cv2.imshow("Training", imgnp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ============= train the classifier ==================

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data set completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train_Data(root)
    root.mainloop()
