from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #====icons===========
        self.main = PhotoImage(file="images/logo_p.png")

        #-------------title-------------
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT, font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #====Menu======
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=5,y=70,width=1335,height=80)

        #=====Course Button======
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2", command=self.add_course)
        btn_course.place(x=20,y=5,width=200,height=40)

        #=====Student Button======
        btn_student=Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#033054", fg="white",
                            cursor="hand2", command=self.add_student)
        btn_student.place(x=240, y=5, width=200, height=40)

        #=====Result Button=====
        btn_result=Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#033054", fg="white",
                            cursor="hand2", command=self.add_result)
        btn_result.place(x=460, y=5, width=200, height=40)

        #=====View Button=====
        btn_view=Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#033054", fg="white",
                            cursor="hand2", command=self.add_report)
        btn_view.place(x=680, y=5, width=200, height=40)

        #=====Logout Button=====
        btn_logout=Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#033054", fg="white",
                            cursor="hand2")
        btn_logout.place(x=900, y=5, width=200, height=40)

        #=====Exit Button=====
        btn_Exit=Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#033054", fg="white",
                            cursor="hand2")
        btn_Exit.place(x=1120, y=5, width=200, height=40)

        # ==================Content Window===============
        #filename = "images/bg.png"
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 360), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl = Label(self.root, image=self.bg_img).place(x=400, y=160, width=920, height=360)

        # ===================Update details==================
        self.lbl_course = Label(self.root, text="Total Course\n[0]", font=("gudy old style", 15), bd=10, relief=RIDGE,
                                bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=80)

        self.lbl_student = Label(self.root, text="Total Students\n[0]", font=("gudy old style", 15), bd=10, relief=RIDGE,
                                 bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=80)

        self.lbl_result = Label(self.root, text="Total Results\n[0]", font=("gudy old style", 15), bd=10, relief=RIDGE,
                                bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=80)


        # =========== Clock Frame=============
        self.lbl = Label(self.root, bg="white", font=("Book Antiqua", 20, "bold"), fg="blue", compound=BOTTOM, bd=0)
        self.lbl.place(x=8, y=150, height=385, width=308)
        # self.clock_img()
        #self.working()

        # =====footer=====
        footer=Label(self.root, text="SRMS-Student Result Management System\nContact us for any Technical Issue: 6267xxxxxxx8",
                      font=("goudy old style", 12), bg="#033054", fg="white").pack(side=BOTTOM, fill=X)


    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()