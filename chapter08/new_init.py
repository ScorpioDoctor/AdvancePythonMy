class Student(object):
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__")
        self.name = name
        pass


# __new__是在对象生成之前调用，用来控制对象生成过程,最终要返回生成好的对象
# __init__是在对象生成以后调用来完善对象的
# 如果__new__不返回对象，就不会调用__init__

if __name__ == "__main__":
    stu = Student(name="antares")
    print(stu.name)
