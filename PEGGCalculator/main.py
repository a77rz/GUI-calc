from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class main:
    def __init__(self, master):

        self.master = master
        self.master.resizable()

        self.frame_1 = Frame(master)
        self.frame_1.pack()

        self.master.title("Ryerson University GPA (CGPA) Calculator - By Amir Ranjbar | Enjoy :)")
        self.master.geometry("620x540+300+40")

        self.label_1 = Label(self.frame_1, text="Current GPA (If None enter 0):", font=("Laksaman", 15))
        self.label_1.grid(row=1, column=0)
        self.entry_1 = Entry(self.frame_1)
        self.entry_1.grid(row=1, column=1)

        self.label_2 = Label(self.frame_1, text="Total Number of Courses Completed:", font=("Laksaman", 15))
        self.label_2.grid(row=2, column=0)
        self.entry_2 = Entry(self.frame_1)
        self.entry_2.grid(row=2, column=1)

        self.label_3 = Label(self.frame_1, text="Number of Courses to add (Including completed):", font=("Laksaman", 14))
        self.label_3.grid(row=3, column=0)
        self.entry_3 = Entry(self.frame_1)
        self.entry_3.grid(row=3, column=1)

        self.btn_1 = Button(master, text="Click here to add courses", font="Laksaman", command=self.add_courses)
        self.btn_1.pack(pady=8)

        self.frame_2 = Frame(master)
        self.frame_2.pack()


    def add_courses(self):
        if ((self.entry_3.get() != '') & (self.entry_3.get().isdigit())):
            self.num_courses = int(self.entry_3.get())
            self.grades_list = []
            self.weight_list = []
            self.label_weight = Label(self.frame_2, text="Course Weights:",font="Laksaman")
            self.label_weight.grid(row=0, column=0)
            self.label_grades = Label(self.frame_2, text="Grades:",font="Laksaman")
            self.label_grades.grid(row=0, column=1)
            for i in range(0, self.num_courses):
                self.weight_list.append(Spinbox(self.frame_2, values=(1.00, 2.00, 3.00, 4.00)))
                self.weight_list[i].grid(row=i + 1, column=0, padx=10, pady=10)
                self.grades_list.append(Spinbox(self.frame_2, values=("F", "D-", "D", "D+", "C-", "C", "C+", "B"
                    , "B-", "B+", "A", "A-", "A+")))
                self.grades_list[i].grid(row=i + 1, column=1, padx=10, pady=10)
            self.btn_calcCG = Button(self.master, text="Calculate GPA",font="Laksaman", command=self.calc_CG)
            self.btn_calcCG.pack(pady=8)
            self.btn_1.config(state=DISABLED)
        else:
            messagebox.showinfo("Please enter a valid value", font="Laksaman")


    def calc_CG(self):
        tc = 0
        tw = 0
        for j in range(0, self.num_courses):
            tc = tc + float(self.weight_list[j].get()) * (
                self.grade(self.grades_list[j].get()))
            tw = tw + float(self.weight_list[j].get())

        cgpa = round((tc + float(self.entry_1.get()) * int(self.entry_2.get())) / (
                    tw), 2)
        messagebox.showinfo("Your GPA is:", str(cgpa))

    def grade(self, grd):
        dict_G = {'A+': 4.33, 'A-': 4.00,'A': 3.67,'B+': 3.33,'B': 3.00,'B-': 2.67,'C+': 2.33,'C': 2.00,'C-': 1.67,'D+':
            1.33,'D': 1.00,'D-': 0.67,'F': 0}
        return dict_G[grd]


root = Tk()
RyLogo = Image.open("Ryerson-rgb.png")
photo = ImageTk.PhotoImage(RyLogo)
label = Label(image=photo)
label.image = photo
label.pack()
app = main(root)
root.mainloop()