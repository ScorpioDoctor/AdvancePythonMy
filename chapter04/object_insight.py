class Student(object):
    """这是学生类"""
    vv="xx"
    def __init__(self,name, gender):
        self.gender = gender
        self.name = name
    def get_gender(self):
        return self.gender
    def __str__(self):
        return "{0}的性别是{1}".format(self.name,self.gender)

class Doctor(Student):
    """博士生"""
    def __init__(self):
        pass

if __name__ == "__main__":
    stu = Student("貂蝉","女")
    print(stu.__dict__)
    print(stu.__dict__['name'])
    stu.__dict__["level"]="博士"
    print(stu.level)
    print(Student.__dict__)
    print(Doctor.__dict__)
    print(dir(stu))
    print(dir(Student))