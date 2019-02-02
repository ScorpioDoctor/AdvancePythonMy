def add(a, b):
    a += b
    return a

class School(object):
    def __init__(self,name,teachers=[]):
        self.name = name
        self.teachers = teachers
    def add(self,teach_name):
        self.teachers.append(teach_name)
    def remove(self,teach_name):
        self.teachers.remove(teach_name)

if __name__ == "__main__":
    # a = 1
    # b = 2
    # a = 'aaa'
    # b = 'bbb'
    # a = ['a', 'b', 'c']
    # b = ['d', 'e']
    # a = ('a', 'b', 'c')
    # b = ('d', 'e')
    # c = add(a, b)
    # print(c)
    # print(a, b)
    sch = School("studyai.com",["antares","xjtu"])
    sch.add("李太白")
    print(sch.teachers)
    sch.remove("xjtu")
    print(sch.teachers)

    sch2 = School("aistudy")
    sch2.add("刘玄德")
    sch2.add("曹孟德")
    print("sch2: ",sch2.teachers)

    sch3 = School("ai")
    sch3.add("孙悟空")
    sch3.add("猪八戒")
    print("sch3: ", sch3.teachers)
    sch3.remove("曹孟德")
    print("sch2: ", sch2.teachers)

    print(sch2.teachers is sch3.teachers)