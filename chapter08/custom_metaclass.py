# 元类是用来创建类的类，用来控制创建类的过程
# 元类创建类对象的过程：会首先去寻找metaclass，通过metaclass来创建类对象本身；
# 如果没有自定义metaclass,最终会调用type这个元类来创建对象
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("MetaClass::__new__")
        return super().__new__(cls,*args, **kwargs)
class School(metaclass=MetaClass):
    def __init__(self,lights,sofa):
        self.lights = lights
        self.sofa = sofa
        print("__init__")

if __name__=="__main__":
    sch = School(lights="雷士灯",sofa="顾家沙发")#sch：School类的实例；把School本身叫做类对象
    print(sch.sofa)
    from collections import Sized
    class MySize(Sized):
        def __len__(self):
            pass
    mysize=MySize()