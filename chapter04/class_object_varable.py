class Student(object):
    gender = "男"
    def __init__(self, age, name):
        self.age = age
        self.name = name

stu = Student(20, "antares")
print(stu.name)
print(stu.age)
print(stu.gender)
print(Student.gender)
# stu.gender = "女"
Student.gender = "女"
print(stu.gender)
print(Student.gender)
print(id(stu),id(Student))
print(id(stu.gender),id(Student.gender))