from chapter04.class_method import MyDate

class Student(object):
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year

if __name__ == "__main__":
    stu = Student(MyDate(2000, 8, 19))
    print(stu.get_age())
    print(stu._Student__birthday)
    print(stu.__birthday)