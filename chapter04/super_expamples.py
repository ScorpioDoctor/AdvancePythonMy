# from threading import Thread
# class MyThread(Thread):
#     def __init__(self,name,user,group):
#         self.user = user
#         super().__init__(name=name,group=group)


class A(object):
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")
        super().__init__()
class C(A):
    def __init__(self):
        print("C")
        super().__init__()
class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()
if __name__=="__main__":
    d = D()
    print(D.__mro__)
    # my_thread = MyThread("my-thread",'mine',group="usergroup")