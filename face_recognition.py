from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x680+0+0")
        self.root.title("Face Recognition System")

        # ================== tite displaying on frame ================

        title_lbl = Label(self.root, text="Face Recognition",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="grey")
        title_lbl.place(x=0, y=0, width=1275, height=47)

        # ================= img in left side ============================

        img_face = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\fce1.jpg")
        img_face = img_face.resize((650, 650), Image.ANTIALIAS)
        self.photoimg_face = ImageTk.PhotoImage(img_face)

        f_lbl = Label(self.root, image=self.photoimg_face)
        f_lbl.place(x=0, y=50, width=650, height=650)

        # ================== img in right side ===========================

        img_face1 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\fce2.jpg")
        img_face1 = img_face1.resize((750, 650), Image.ANTIALIAS)
        self.photoimg_face1 = ImageTk.PhotoImage(img_face1)

        f_lbl = Label(self.root, image=self.photoimg_face1)
        f_lbl.place(x=650, y=50, width=750, height=650)

        # ============== button on image ========================

        btn = Button(self.root, text="Face Detect", cursor="hand2",
                     command=self.face_recognition, width=30,
                     font=("times new roman", 15, "bold"), bg="gray", fg="darkblue")
        btn.place(x=960, y=625, width=130, height=35)

    # =================== Attendance system =========================

    def mark_attendance(self, s, r, n, d):
        with open("Attendancesheet_1.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if (s not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{n},{r},{d},{dtString},{d1},Present")

    # =================== creating a function ====================

    def face_recognition(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((500 * (1 - predict / 100)))
                print(confidence)

                conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                               database="face_recognition")
                my_cursor = conn.cursor()

                # ============== to get data from database ====================

                my_cursor.execute("select Student_Name from student where Student_ID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll_No from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Department from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                s = my_cursor.fetchone()
                s = "+".join(s)

                if confidence > 100:
                    cv2.putText(img, f"Student_ID:{s}", (x, y - 110), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 1)
                    cv2.putText(img, f"Roll_No:{r}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 1)
                    cv2.putText(img, f"Student_Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (250, 255, 0), 1)
                    cv2.putText(img, f"Department:{d}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 240), 1)
                    self.mark_attendance(s, r, n, d)


                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, "Unknown face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)

                coord = [x, y, w, y]

            return coord

        def face_rec(img, clf, facecascade):
            coord = draw_boundary(img, facecascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = face_rec(img, clf, facecascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
