#python中的变量和java中的变量是不一样的：
# python的变量实质上是指针，这个指针在内存中占用的存储字节数是固定的
# 指针像便利贴，它可以被贴到任意对象上。而这个对象本身所占有的内存区域是不固定。
# 指针可以指向 int,str,float，list,dict,自定义类的对象
# a = 1
# a = "studyai.com"
a = 'acdaaaaqqqqqqsddxxx'
# 变量 a 指向了 对象
# Python解释器先产生对象，然后再产生变量a,最后再把a指向产生的对象
#任何一个对象既有所属类型又有取值
# b = a
# b.append("xxx")
# print(a)
# print(b)
# print(a is b)
# print(id(a), id(b))

b = 'acdaaaaqqqqqqsddxxx'
print(a is b)
print(id(a)== id(b))
print(a==b)

class MyObject:
    def __del__(self):
        pass

obj = MyObject()
# isinstance(obj,MyObject)
# if type(obj) is MyObject:
#     print("休息休息")

#python中的垃圾回收采用 引用计数
obj2 = obj
print(obj)
print(obj2)
del obj2
print(obj)
print(obj2)