# 自定义可迭代对象：实现可迭代对象的协议
class School(object):
    def __init__(self,teachers):
        self.teachers = teachers
    def __iter__(self):
        return MyIterator(self.teachers)
    # def __getitem__(self, item):
    #     return self.teachers[item]

# 自定义迭代器的第一种方法:实现迭代器协议
class MyIterator(object):
    def __init__(self,iter_list):
        self.iter_list = iter_list
        self.index = -1
    def __next__(self):
        # 在这个魔法函数内部需要真正的返回迭代值
        self.index += 1
        try:
            value = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        else:
            return value
    def __iter__(self):
        return self

# 自定义迭代器的第二种方法：继承迭代器的抽象基类 Iterator
from collections import Iterator
class MyIterator2(Iterator):
    def __init__(self,iter_list):
        self.iter_list = iter_list
        self.index = -1
    def __next__(self):
        # 在这个魔法函数内部需要真正的返回迭代值
        self.index += 1
        try:
            value = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        else:
            return value

if __name__=="__main__":
    sch = School(teachers=["孙悟空","猪八戒","唐三藏"])
    # iter是个全局内置函数，智能的：先找__iter__,如果找不到，退化去找__getitem__
    my_itor = iter(sch)
    while True:
        try:
            print(next(my_itor)) # next 是全局函数，会调用对应的迭代器的__next__魔法函数
        except StopIteration:
            break
    for teacher in sch:
        print(teacher)