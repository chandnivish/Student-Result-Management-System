import sqlite3
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Results Management System")
        self.root.geometry('1200x480+80+170')
        self.root.config(bg="white")
        self.root.focus_force()
        #===============Title===============
        title = Label(self.root, text="Add Student Result",
                     font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180,
                                                                                           height=35)

        # =====================Footer Area===================
        #footer = Label(self.root,text="SRMS-Student Result Management System",font=("goudy old Style", 12, "bold"), bg="#033054", fg="white").pack(side=BOTTOM, fill=X)

        # =====================widgets======================
        # ======================Variables===================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 15, "bold"), bg="white").place(x=50,
                                                                                                                  y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white").place(
            x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 15, "bold"), bg="white").place(x=50,
                                                                                                                  y=340)

        # =======================Entry Feilds===============
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list,
                                        font=("goudy old style", 12, "bold"), state="readonly", justify=CENTER)
        self.txt_student.place(x=200, y=100, width=100)
        self.txt_student.set("SELECT")
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f4", fg="white",
                            cursor="hand2", command=self.search).place(x=310, y=100, width=100, height=28)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightyellow",
                         state="readonly").place(x=200, y=160, width=210)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg="lightyellow",
                           state="readonly").place(x=200, y=220, width=210)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 15, "bold"),
                          bg="lightyellow").place(x=200, y=280, width=210)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 15, "bold"),
                               bg="lightyellow").place(x=200, y=340, width=210)

        # =========================Button====================
        btn_add = Button(self.root, text="Submit", font=("times new roman", 15), bg="lightgreen",activebackground="lightgreen", cursor="hand2", command=self.submit).place(x=190, y=390,
                                                                                                   width=90, height=30)
        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15), bg="lightgray",activebackground="lightgreen", cursor="hand2", command=self.clear).place(x=300, y=390, width=90, height=30)

        # =====================Images=======================
        filename = "images/result.jpg"
        self.bg_img = Image.open(filename)
        self.bg_img = self.bg_img.resize((600, 300), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl = Label(self.root, image=self.bg_img).place(x=530, y=100)

        # =====================Functions====================
    def fetch_roll(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select name,course from student where roll=?", (self.var_roll.get(),), )
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", "Error Due To {str(ex)}")

    def submit(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please First Search Student Record", parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",
                            (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Result Already Present", parent=self.root)
                else:
                    per=(int(self.var_marks.get()) * 100)/int(self.var_full_marks.get())
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfuly", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}")

    def clear(self):
        self.var_roll.set(["SELECT"]),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),

if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()