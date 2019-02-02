from collections import abc

# 不可修改序列
class MyInmutableSequence(abc.Sequence):
    pass

# 可修改序列
class MyMutableSequence(abc.MutableSequence):
    pass

if __name__=="__main__":
    my_seq = MyMutableSequence()
    a=[1,2,3]
    if 1 in a:
        pass
    for item in a:
        pass