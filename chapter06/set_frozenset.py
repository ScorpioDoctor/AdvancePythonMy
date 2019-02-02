#set 集合 frozenset 不可变集合： 无序，不重复 ：对数学里面集合概念的模拟
s1 = set("studyai.com")
# s = set([1,2,3,4])
# s = {'q':'www','w':'studyai','123':'.com'}
s = {'q','w','123','q','w'}
fs = frozenset(['2',2,'aa'])#可以把它作为dict的key
# print(type(fs))
# print(fs)
#向set里面加入元素
s.add('ai')
print(s)
#集合的并集，交集，差集
# diff_set = s.difference(set(['q','ai']))
# diff_set = s - set(['q','ai','abc'])
# union_set = s | set(['q','ai','abc'])
insect_set = s & set(['q','ai','abc'])
print(insect_set)

print(s)
print(insect_set.issubset(s))

if 'q' in insect_set:
    print("我在里面")