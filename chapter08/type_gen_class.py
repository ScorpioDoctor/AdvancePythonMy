def create_class(name):
    if name == "Student":
        class Student:
            name="stu"
            def __init__(self):
                print("我是学生类")
        return Student
    elif name == "School":
        class School:
            def __init__(self):
                print("我是学校类")
        return School

def init(self):
    print("我是类的方法")
    return self.name

class Organization(object):
    org_name="教育机构"
    pass

# type元类 --> class类对象 --> object(实例) “a”，1，[1,2]


if __name__=="__main__":
    # 通过调用函数的方式创建动态类
    # MyClass = create_class("Student")
    # MyClass = create_class("School")
    # myobj = MyClass()
    # print(myobj)
    # print(type(MyClass))

    # 通过 type 这个元类来动态创建类
    School = type("School",(Organization,),{"name":"studyai.com","init":init})
    print(type(School))
    sch = School()
    print(type(sch))
    print(sch.name)
    print(sch.org_name)
    print(sch.init())