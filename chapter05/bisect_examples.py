import bisect
#用来管理已排序好的序列，让这个序列在插入操作时始终维持排序状态
#二分查找
mylist = [1,2,3,4,5,8]
bisect.insort(mylist,6)
bisect.insort(mylist,7)
bisect.insort(mylist,0)
# mylist.extend([0])
# bisect.insort_right(mylist,6.1)
# bisect.insort(mylist,4.1)
# bisect.insort_left(mylist,4.1)
index = bisect.bisect_left(mylist,3)
bisect.insort_left(mylist,3)

print(index)
print(mylist)