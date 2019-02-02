# 什么是迭代协议？
# 迭代器是什么？他是访问容器(列表，集合，字典)内元素的一种方式，用处就是遍历数据
# 下标访问：也是一种获取，遍历数据的另外一种方式,允许随机访问
# 区别是：迭代器是不能返回的
# 迭代器提供了一种对容器数据的惰性访问方式：不会把整个容器的数据全部搬进来，而是需要的时候才获取
# 可迭代类型：实现了迭代协议的类型：list,set,tuple,array:共同点是实现了 魔法函数 __iter__()
# 迭代器与可迭代类型有什么分别？迭代器协议是要求必须实现魔法函数：__next__()
from collections import Iterable,Iterator
a = list([1,2,3,4,5])
a[0],a[2],a[1],a[0]
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
print(type(Iterator))
print(isinstance(iter(a) ,Iterator))
