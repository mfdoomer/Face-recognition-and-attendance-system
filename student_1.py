from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class student:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x680+0+0")
        self.root.title("Face Recognition System")

        # ============= Variables ==============
        self.var_Department = StringVar()
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Semester = StringVar()
        self.var_Student_ID = StringVar()
        self.var_Student_Name = StringVar()
        self.var_Class_Division = StringVar()
        self.var_Roll_no = StringVar()
        self.var_DOB = StringVar()
        self.var_Gender = StringVar()
        self.var_Email_ID = StringVar()
        self.var_Phone_No = StringVar()
        self.var_Address = StringVar()
        self.var_Teacher_Name = StringVar()
        self.var_Photo_sample = StringVar()

        # First image

        img_left = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\students1.jpg ")
        img_left = img_left.resize((1275, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1275, height=140)

        # bg image

        img2 = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\canvas.jpg")
        img2 = img2.resize((1275, 700), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=100, width=1275, height=700)

        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1275, height=50)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=50, width=1275, height=600)

        # left frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 15, "bold"))
        left_frame.place(x=5, y=0, width=600, height=550)

        # left image

        img_left = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\student2.jpg")
        img_left = img_left.resize((1275, 200), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=5, width=600, height=80)

        # department

        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 15, "bold"))
        current_course_frame.place(x=3, y=85, width=590, height=110)

        course_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Department,
                                 font=("times new roman", 12, "bold"), width=17,
                                 state="read only")
        dep_combo["values"] = (
            "Select Department", "Computer Science", "Information Technology", "Bach_of_Science", "BMS", "B.com",)
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course

        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_label = ttk.Combobox(current_course_frame, textvariable=self.var_Course,
                                    font=("times new roman", 12, "bold"), width=17,
                                    state="read only")
        course_label["values"] = ("Course", "First Year", "Second Year", "Third Year")
        course_label.current(0)
        course_label.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year

        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_label = ttk.Combobox(current_course_frame, textvariable=self.var_Year,
                                  font=("times new roman", 12, "bold"), width=17,
                                  state="read only")
        year_label["values"] = ("Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        year_label.current(0)
        year_label.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester

        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_label = ttk.Combobox(current_course_frame, textvariable=self.var_Semester,
                                      font=("times new roman", 12, "bold"), width=17,
                                      state="read only")
        semester_label["values"] = ("Semester", "I", "II", "III", "IV", "V", "VI")
        semester_label.current(0)
        semester_label.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information

        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 15, "bold"))
        class_student_frame.place(x=3, y=195, width=590, height=300)

        # student id

        student_id_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 12, "bold"),
                                 bg="white")
        student_id_label.grid(row=0, column=0, padx=3, pady=5, sticky=W)

        student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_Student_ID, width=20,
                                     font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=3, pady=5, sticky=W)

        # student name

        student_name_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"),
                                   bg="white")
        student_name_label.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_Student_Name, width=20,
                                       font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # class division

        class_division_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"),
                                     bg="white")
        class_division_label.grid(row=1, column=0, padx=3, pady=5, sticky=W)

        class_division_label = ttk.Combobox(class_student_frame, textvariable=self.var_Class_Division,
                                            font=("times new roman", 12, "bold"), width=18,
                                            state="read only")

        class_division_label["values"] = ("Select Division", "A", "B", "C", "D", "E", "F")
        class_division_label.current(0)
        class_division_label.grid(row=1, column=1, padx=3, pady=5, sticky=W)

        # roll no

        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                              bg="white")
        roll_no_label.grid(row=1, column=2, padx=3, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_Roll_no, width=20,
                                  font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=3, pady=5, sticky=W)

        # gender

        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"),
                             bg="white")
        gender_label.grid(row=2, column=0, padx=3, pady=5, sticky=W)

        gender_label = ttk.Combobox(class_student_frame, textvariable=self.var_Gender,
                                    font=("times new roman", 12, "bold"), width=18,
                                    state="read only")
        gender_label["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_label.current(0)
        gender_label.grid(row=2, column=1, padx=3, pady=5, sticky=W)

        # date of birth

        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"),
                          bg="white")
        dob_label.grid(row=2, column=2, padx=3, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_DOB, width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=3, pady=5, sticky=W)

        # email

        email_label = Label(class_student_frame, text="Email ID:", font=("times new roman", 12, "bold"),
                            bg="white")
        email_label.grid(row=3, column=0, padx=3, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_Email_ID, width=20,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=3, pady=5, sticky=W)

        # phone

        phone_no_label = Label(class_student_frame, text="Phone NO:", font=("times new roman", 12, "bold"),
                               bg="white")
        phone_no_label.grid(row=3, column=2, padx=3, pady=5, sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_Phone_No, width=20,
                                   font=("times new roman", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=3, pady=5, sticky=W)

        # Address

        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"),
                              bg="white")
        address_label.grid(row=4, column=0, padx=3, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_Address, width=20,
                                  font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=3, pady=5, sticky=W)

        # teacher

        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"),
                              bg="white")
        teacher_label.grid(row=4, column=2, padx=3, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_Teacher_Name, width=20,
                                  font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=3, pady=5, sticky=W)

        # radio button

        self.var_radio = StringVar()
        radio_button = ttk.Radiobutton(class_student_frame, variable=self.var_radio, text="Take Photo Sample",
                                       value="Yes")
        radio_button.grid(row=5, column=0)

        radio_button2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio, text="No Photo Sample",
                                        value="No")
        radio_button2.grid(row=5, column=1)

        # buttons

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=585, height=36)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=14, font=("times new roman", 13, "bold"),
                          bg="gray", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=14,
                            font=("times new roman", 13, "bold"), bg="gray",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=14,
                            font=("times new roman", 13, "bold"), bg="gray",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=14,
                           font=("times new roman", 13, "bold"), bg="gray",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        # new button due to width problem in previous button

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=585, height=36)

        take_photo_btn = Button(btn_frame1, text="Take sample Photo", command=self.generate_dataset, width=30,
                                font=("times new roman", 13, "bold"),
                                bg="gray", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo", command=self.update_data, width=30,
                                  font=("times new roman", 13, "bold"),
                                  bg="gray", fg="white")
        update_photo_btn.grid(row=1, column=1)

        # right frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 15, "bold"))
        right_frame.place(x=650, y=0, width=600, height=550)

        # right image

        img_right = Image.open(r"C:\Users\Abr79\PycharmProjects\pythonProject2\College images\student2.jpg")
        img_right = img_right.resize((1275, 200), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=5, width=600, height=80)

        # ======= search system ============

        search_system_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                         font=("times new roman", 15, "bold"))
        search_system_frame.place(x=3, y=85, width=590, height=110)

        search_label = Label(search_system_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=1, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_system_frame, font=("times new roman", 12, "bold"), width=17,
                                    state="read only")

        search_combo = ttk.Combobox(search_system_frame, font=("times new roman", 12, "bold"), width=17,
                                    state="read only")
        search_combo["values"] = ("Select", "Name", "Roll_no", "Class", "Division")
        search_combo.current(0)
        search_combo.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_system_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        search_btn = Button(search_system_frame, text="Search", width=7, font=("times new roman", 13, "bold"),
                            bg="gray", fg="white")
        search_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        show_all_btn = Button(search_system_frame, command=self.get_cursor, text="Show All", width=7,
                              font=("times new roman", 13, "bold"),
                              bg="gray", fg="white")
        show_all_btn.grid(row=0, column=5, padx=5, pady=10, sticky=W)

        # ======= table frame=============

        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=200, width=590, height=295)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Department", "Course", "Year", "Semester", "Student ID",
                                                               "Student Name", "Class Division", "Roll No", "DOB",
                                                               "Gender", "Email ID", "Phone No", "Address",
                                                               "Teacher Name", "Photo sample"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set
                                          )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student ID", text="Student ID")
        self.student_table.heading("Student Name", text="Student Name")
        self.student_table.heading("Class Division", text="Class Division")
        self.student_table.heading("Roll No", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email ID", text="Email ID")
        self.student_table.heading("Phone No", text="Phone No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher Name", text="Teacher Name")
        self.student_table.heading("Photo sample", text="Photo sample")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Student ID", width=100)
        self.student_table.column("Student Name", width=100)
        self.student_table.column("Class Division", width=100)
        self.student_table.column("Roll No", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Email ID", width=100)
        self.student_table.column("Phone No", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher Name", width=100)
        self.student_table.column("Photo sample", width=100)
        # self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):

        if self.var_Department.get() == "Select Department" or self.var_Student_Name.get() == "" or \
                self.var_Student_ID.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:

                # install mysql-connector-python

                # ============== use correct syntax of mysql==============

                conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_Department.get(),
                    self.var_Course.get(),
                    self.var_Year.get(),
                    self.var_Semester.get(),
                    self.var_Student_ID.get(),
                    self.var_Student_Name.get(),
                    self.var_Class_Division.get(),
                    self.var_Roll_no.get(),
                    self.var_Gender.get(),
                    self.var_Email_ID.get(),
                    self.var_Phone_No.get(),
                    self.var_Address.get(),
                    self.var_Teacher_Name.get(),
                    self.var_radio.get(),
                    self.var_DOB.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details has been added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

        # ============ function for fetching data==================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select Department, Course, Year, Semester, Student_ID,Student_Name,"
                          "Class_Division, Roll_No,DOB,Gender,Email_ID,"
                          "Phone_No,Address,Teacher_Name,Photo_sample from student")
        data1 = my_cursor.fetchall()

        if len(data1) > 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data1:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # =============== get cursor================

    def get_cursor(self, a):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if len(data) > 0:
            self.var_Department.set(data[0]),
            self.var_Course.set(data[1]),
            self.var_Year.set(data[2]),
            self.var_Semester.set(data[3]),
            self.var_Student_ID.set(data[4]),
            self.var_Student_Name.set(data[5]),
            self.var_Class_Division.set(data[6]),
            self.var_Roll_no.set(data[7]),
            self.var_DOB.set(data[8]),
            self.var_Gender.set(data[9]),
            self.var_Email_ID.set(data[10]),
            self.var_Phone_No.set(data[11]),
            self.var_Address.set(data[12]),
            self.var_Teacher_Name.set(data[13]),
            self.var_radio.set(data[14])

        # =============== update button =======================

    def update_data(self):

        if self.var_Department.get() == "Select Department" or self.var_Student_Name.get() == "" or \
                self.var_Student_ID.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update the data", parent=self.root)

                if update > 0:

                    conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,"
                                      "Student_Name=%s,Class_Division=%s,Roll_No=%s,Gender=%s,Email_ID=%s,"
                                      "Phone_No=%s,Address=%s,Teacher_Name=%s,Photo_sample=%s,DOB=%s"
                                      " where Student_ID=%s",
                                      (
                                          self.var_Department.get(),
                                          self.var_Course.get(),
                                          self.var_Year.get(),
                                          self.var_Semester.get(),
                                          self.var_Student_Name.get(),
                                          self.var_Class_Division.get(),
                                          self.var_Roll_no.get(),
                                          self.var_Gender.get(),
                                          self.var_Email_ID.get(),
                                          self.var_Phone_No.get(),
                                          self.var_Address.get(),
                                          self.var_Teacher_Name.get(),
                                          self.var_radio.get(),
                                          self.var_DOB.get(),
                                          self.var_Student_ID.get()
                                      ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details has been successfully updated",
                                        parent=self.root)
                else:
                    if not update:
                        return

            except Exception as es:
                messagebox.showerror("Error", f" Due to:{str(es)}", parent=self.root)

    # ============ delete function ===============

    def delete_data(self):
        if self.var_Student_ID.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Data", "Do you want to Delete this Data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_ID=%s"
                    val = (self.var_Student_ID.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student data has been successfully deleted",
                                        parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error", f" Due to:{str(es)}", parent=self.root)

    # ============ rest function ========================

    def reset_data(self):
        self.var_Department.set("Select semester"),
        self.var_Course.set("Select Course"),
        self.var_Year.set("Select Year"),
        self.var_Semester.set("Select Semester"),
        self.var_Student_ID.set(""),
        self.var_Student_Name.set(""),
        self.var_Class_Division.set("Select Division"),
        self.var_Roll_no.set(""),
        self.var_Gender.set("Select Gender"),
        self.var_Email_ID.set(""),
        self.var_Phone_No.set(""),
        self.var_Address.set(""),
        self.var_Teacher_Name.set(""),
        self.var_radio.set(""),
        self.var_DOB.set("")

    # =============== data set or take photo samples ===================

    def generate_dataset(self):
        if self.var_Department.get() == "Select Department" or self.var_Student_Name.get() == "" or \
                self.var_Student_ID.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,"
                                  "Student_Name=%s,Class_Division=%s,Roll_No=%s,Gender=%s,Email_ID=%s,"
                                  "Phone_No=%s,Address=%s,Teacher_Name=%s,Photo_sample=%s,DOB=%s"
                                  " where Student_ID=%s",
                                  (
                                      self.var_Department.get(),
                                      self.var_Course.get(),
                                      self.var_Year.get(),
                                      self.var_Semester.get(),
                                      self.var_Student_Name.get(),
                                      self.var_Class_Division.get(),
                                      self.var_Roll_no.get(),
                                      self.var_Gender.get(),
                                      self.var_Email_ID.get(),
                                      self.var_Phone_No.get(),
                                      self.var_Address.get(),
                                      self.var_Teacher_Name.get(),
                                      self.var_radio.get(),
                                      self.var_DOB.get(),
                                      self.var_Student_ID.get() == id + 1
                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # =========== face detection ===================

                face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_data.detectMultiScale(gray, 1.3, 10)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, frame_1 = cap.read()
                    if face_cropped(frame_1) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(frame_1), (800, 600))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "img data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Faces", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Results", "Generating data set!!")

            except Exception as es:
                messagebox.showerror("Error", f" Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
