
class Student():
    def __init__(self, name):
        self.name = name
    def do_homework(self):
        print(self.name + ' do english')

student1 = Student('aaa')
student2 = Student('bbb')

student1.do_homework()
student2.do_homework()