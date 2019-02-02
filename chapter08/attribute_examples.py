from datetime import date, datetime

# __getattr__:只有在查找不到属性的时候才会被调用
#__getattribute__：不管发生什么情况都会被优先调用

class Student(object):
    def __init__(self,info={}):
        self.info = info
    def __getattr__(self, item):
        print("__getattr__: ", item)
        return self.info.get(item,"antares")
    # def __getattribute__(self, item):
    #     print("__getattribute__: ", item)
    #     return item

if __name__ == "__main__":
    stu = Student(info={"name":"antares", "birthday":date(year=2000, month=9, day=19),
                        "gender":"男","school":"studyai"})
    print(stu.info["name"])
    print(stu.gender)
    print(stu.school)
    print(stu.birthday)
