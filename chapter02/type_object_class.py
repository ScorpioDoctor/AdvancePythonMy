a = 3.9
b = "qaz"
c = [1, 2, 3, 'abc']
print(type(a))
print(type(int))
print(type(b))
print(type(str))
print(type(c))
print(type(list))
# type 类 --> builtin classes (python 内置类型)  -->  1, 2.3,"asd",[1,23],{1:'a',}
class Student(object):
    pass
stu = Student()
print(type(stu))
print(type(Student))
# type 类 --> custom classes (自定义类型)  -->  stu
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(type.__bases__)
# object 是所有类的基类：list,int ,float,str,type,Student
print(object.__bases__)
print(type(object))
# type 类 --> object类对象
# type 类 --> type类对象