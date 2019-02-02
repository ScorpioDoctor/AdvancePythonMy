# 列表生成式:1、简化代码；2、比简单的for循环效率高
mylist = list()
for i in range(30):
    if i % 2 == 0:
        mylist.append(i)

def operate_item(i):
    return i**3-i+i**2

mylist = [operate_item(i) for i in range(30) if i % 5 in [1, 2, 3, 4] if i % 3 != 0]
print(mylist)

#生成器表达式：返回 generator 类 ，而不是 set,tuple类
mygen = (i**2 for i in range(30) if i % 3 != 0)
print(type(mygen))
print(mygen)
# for item in mygen:
#     print(item)

# 字典推导(列表)式
mydict={"study":10,"ai":12,"antares":29,'oo':29}
print(type(mydict))
print(mydict)
mydict2={value:key for key,value in mydict.items()}
print(type(mydict2))
print(mydict2)
#集合推导式
myset = {key for key,value in mydict.items()}
print(type(myset))
print(myset)
myset2 = set(mydict2.values())
print(type(myset2))
print(myset2)