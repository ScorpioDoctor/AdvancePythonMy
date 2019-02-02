class Student(object):
    gender = '男'
    def __init__(self):
        self.gender = "女"

stu = Student()
print(stu.gender)

class D(object):
    pass
class E(object):
    pass
class B(D):
    pass
class C(E):
    pass
class A(B,C):
    pass

print(A.__mro__)