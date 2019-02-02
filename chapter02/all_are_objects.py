def hello(name='antares'):
    print("hello! ", name)
    return 'func-->' + name
class Student(object):
    def __init__(self):
        print("classs-->studyai.com")
    def __str__(self):
        return 'i am studyai.com!'

def printType(obj):
    print(type(obj))

def decorator_func():
    print("decorator:studyai.com")
    return Student

myfunc = decorator_func()
print(myfunc())
# printType(hello)
# printType(hello())
# printType(Student)
# printType(Student())

# objects = []
# objects.append(hello)
# objects.append(Student)
# # objects.append("123")
# for obj in objects:
#     print(obj())

# hello("xjtu")
# hello_func = hello()
# hello_func = hello
# hello_func("studyai.com")
# s1 = Student
# s2 = s1
# s3 = s2()
