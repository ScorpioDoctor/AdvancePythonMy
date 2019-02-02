import numbers

class IntegralField(object):
    """data descriptor:数据描述符"""
    def __init__(self):
        self.valuexx = 0
    def __get__(self, instance, owner):
        print("__get__",instance)
        return self.valuexx
    def __set__(self, instance, value):
        # print("__set__",instance,value)
        if isinstance(value,numbers.Integral):
            print("属性的数值合法")
            self.valuexx = value
        else:
            raise ValueError("属性必须是Ingeral类型！")
    def __delete__(self, instance):
        print("__delete__")

class NonIntegralField(object):
    """non-data descriptor:非数据描述符"""
    def __init__(self):
        self.valuexx = 0
    def __get__(self, instance, owner):
        print("__get__",instance)
        return self.valuexx

class Student(object):
    # age = IntegralField()
    age = NonIntegralField()
    # age = 90
    # year = IntegralField()
    # friends = IntegralField()
    def __init__(self,age):
        self.age = 0


if __name__ == "__main__":
    stu = Student()
    print(stu.age)
    print(getattr(stu,"age"))
    stu.age = 12
    print(stu.age)
    # del stu.age
    # stu.year = 2000
    # print(stu.year)


'''
如果stu是Student类的实例，那么stu.age（以及等价的getattr(stu,'age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
stu = Student(), 那么stu.age 顺序如下：
（1）如果“age”是出现在Student或其基类的__dict__中， 且age是data descriptor， 那么调用其__get__方法, 否则
（2）如果“age”出现在stu这个对象的__dict__中， 那么直接返回 stu.__dict__[‘age’]， 否则
（3）如果“age”出现在Student或其基类的__dict__中
    （3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则
    （3.2）返回 Student.__dict__[‘age’]
（4）如果Student有__getattr__方法，调用__getattr__方法，否则
（5）抛出AttributeError
'''