import tkinter

GRADES = ["A","B","C","D","F"]

class Course(object):


    def __init__(self, root, course_id):
        # Store Course ID
        self.course_id = course_id
        # Create Frame
        self.frame = tkinter.Frame(root)
        # Create Label
        self.label = tkinter.Label(self.frame, text = ('Class %d:' % course_id), fg = 'black')
        self.label.pack(side = 'left')
        # Create Credit Hours Entry
        self.hours = tkinter.Entry(self.frame)
        self.hours.pack(side = 'left')
        # Create Grade Dropdown
        self.grade = tkinter.StringVar(root)
        self.grade.set("  ")
        self.gopt = tkinter.OptionMenu(self.frame, self.grade, *GRADES, command=self.dd_cb)
        self.gopt.pack(side = 'left')

    def dd_cb(self, selected):
        print("Course %d Dropdown Event: %s" % (self.course_id, selected))

    def pack(self):
        self.frame.pack()
