from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np

myData = []


class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x680+0+0")
        self.root.title("Face Recognition System")

        # ============== variables ====================

        self.var_Student_ID = StringVar()
        self.var_Roll_no = StringVar()
        self.var_Name = StringVar()
        self.var_Department = StringVar()
        self.var_Time = StringVar()
        self.var_Date = StringVar()
        self.var_Status = StringVar()

        # First image

        img_left = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\Attendance3.png")
        img_left = img_left.resize((1275, 220), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1275, height=190)

        # bg image

        img2 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\canvas.jpg")
        img2 = img2.resize((1275, 700), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=100, width=1275, height=700)

        title_lbl = Label(bg_img, text="Student Attendance Details", font=("times new roman", 30, "bold"),
                          bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1275, height=50)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=50, width=1275, height=600)

        # left frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 15, "bold"))
        left_frame.place(x=5, y=0, width=620, height=550)

        img_left = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\attendance3.png")
        img_left = img_left.resize((660, 200), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=5, width=620, height=80)

        # ============= left inside frame ==========================

        left_frame1 = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                 font=("times new roman", 15, "bold"))
        left_frame1.place(x=10, y=110, width=610, height=400)

        # ============== Attendance id ==========================

        Attendnce_label = Label(left_frame1, text="Student ID:", font=("times new roman", 12, "bold"),
                                bg="white")
        Attendnce_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        Attendance_entry = ttk.Entry(left_frame1, width=20, textvariable=self.var_Student_ID,
                                     font=("times new roman", 12, "bold"))
        Attendance_entry.grid(row=0, column=1, padx=3, pady=3, sticky=W)

        # ================= Roll no ===========================

        roll_label = Label(left_frame1, text="Roll No:", font=("times new roman", 12, "bold"),
                           bg="white")
        roll_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_frame1, width=20, textvariable=self.var_Roll_no,
                               font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=3, pady=3, sticky=W)

        # ================= name =============================

        name_label = Label(left_frame1, text="Name:", font=("times new roman", 13, "bold"),
                           bg="white")
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        name_entry = ttk.Entry(left_frame1, width=20, textvariable=self.var_Name,
                               font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=3, pady=3, sticky=W)

        # ==================== Department ==========================

        dep_label = Label(left_frame1, text="Department:", font=("times new roman", 12, "bold"),
                          bg="white")
        dep_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        dep_entry = ttk.Entry(left_frame1, width=20, textvariable=self.var_Department,
                              font=("times new roman", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=3, pady=3, sticky=W)

        # ================ Time ==========================

        time_label = Label(left_frame1, text="Time:", font=("times new roman", 12, "bold"),
                           bg="white")
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        time_entry = ttk.Entry(left_frame1, width=20, textvariable=self.var_Time,
                               font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=3, pady=3, sticky=W)

        # ================ Date =======================

        date_label = Label(left_frame1, text="Date:", font=("times new roman", 12, "bold"),
                           bg="white")
        date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        date_entry = ttk.Entry(left_frame1, width=20, textvariable=self.var_Date,
                               font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=3, pady=3, sticky=W)

        # ============= Attendance status =========================

        status_label = Label(left_frame1, text="Attendance Status:", font=("times new roman", 12, "bold"),
                             bg="white")
        status_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        status_label = ttk.Combobox(left_frame1,
                                    font=("times new roman", 12, "bold"), width=18,
                                    textvariable=self.var_Status,
                                    state="read only")
        status_label["values"] = ("Select Status", "Present", "Absent")
        status_label.current(0)
        status_label.grid(row=3, column=1, padx=3, pady=3, sticky=W)

        # ============ buttons ========================

        btn_frame = Frame(left_frame1, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=337, width=605, height=36)

        import_btn = Button(btn_frame, text="Import csv", command=self.importcsv, width=20,
                            font=("times new roman", 13, "bold"),
                            bg="gray", fg="white")
        import_btn.grid(row=4, column=0)

        export_btn = Button(btn_frame, text="Export csv", width=20, command=self.export,
                            font=("times new roman", 13, "bold"), bg="gray",
                            fg="white")
        export_btn.grid(row=4, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=20, command=self.reset,
                            font=("times new roman", 13, "bold"), bg="gray",
                            fg="white")
        delete_btn.grid(row=4, column=2)

        # ====================== right frame ==========================

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Database",
                                 font=("times new roman", 15, "bold"))
        right_frame.place(x=650, y=0, width=600, height=550)

        # right image

        img_right = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\attendance3.png")
        img_right = img_right.resize((640, 200), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=5, width=600, height=80)

        # ====================== table frame ============================

        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=90, width=590, height=405)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("Student ID", "Student Name", "Roll No",
                                                                       "Department", "Time",
                                                                       "Date", "Status"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set
                                                  )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Student ID", text="Student ID")
        self.AttendanceReportTable.heading("Student Name", text="Student Name")
        self.AttendanceReportTable.heading("Roll No", text="Roll No")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Status", text="Status")
        self.AttendanceReportTable["show"] = "headings"

        # =================== columns =========================

        self.AttendanceReportTable.column("Student ID", width=100, anchor="center")
        self.AttendanceReportTable.column("Student Name", width=100, anchor="center")
        self.AttendanceReportTable.column("Roll No", width=100, anchor="center")
        self.AttendanceReportTable.column("Department", width=150, anchor="center")
        self.AttendanceReportTable.column("Time", width=100, anchor="center")
        self.AttendanceReportTable.column("Date", width=100, anchor="center")
        self.AttendanceReportTable.column("Status", width=100, anchor="center")

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # self.student_table.bind("<ButtonRelease>", self.get_cursor)

    # ================ fetch data =====================

    def fetchdata(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # ================= import function ================

    def importcsv(self):

        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)

        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchdata(myData)

    # ======================= export function ===========================

    def export(self):
        try:
            if len(myData) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save csv",
                                               filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Data Successfully Exported")

        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content['values']
        self.var_Student_ID.set(row[0])
        self.var_Name.set(row[1])
        self.var_Roll_no.set(row[2])
        self.var_Department.set(row[3])
        self.var_Time.set(row[4])
        self.var_Date.set(row[5])
        self.var_Status.set(row[6])

    def reset(self):
        self.var_Student_ID.set("")
        self.var_Name.set("")
        self.var_Roll_no.set("")
        self.var_Department.set("")
        self.var_Time.set("")
        self.var_Date.set("")
        self.var_Status.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
