#数组
import array
# list可以在里面放不同类型的数据
# array只能在里面存放相同类型的数据

mylist = list()
mylist.append(9)
mylist.append(10)
# print(mylist)
# print("==================")
myarray = array.array('i')
myarray.fromlist(mylist)
myarray.append(1)
myarray.append(3)
myarray.extend([1,2,-2**31,2**31-1])
print(myarray)