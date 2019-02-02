import numbers
from datetime import date, datetime


class Student(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 10  #内部属性
    # def get_age(self):
    #     return datetime.now().year-stu.birthday.year
    @property
    def age(self):
        self._age = datetime.now().year-stu.birthday.year
        return self._age

    @age.setter
    def age(self,value):
        if isinstance(value,numbers.Integral):
            self._age = value
        else:
            raise ValueError("年龄必须是Ingeral类型！")

# stu = Student("antares", date(year=2000, month=9, day=19))
# print(stu.birthday)
# print(__name__)

if __name__ == "__main__":
    stu = Student("antares", date(year=2000, month=9, day=19))
    print(stu.name)
    print(stu.age)
    stu.name = "张三疯"
    stu.age = "abc19"
    print(stu._age)
    # print(stu.get_age())
