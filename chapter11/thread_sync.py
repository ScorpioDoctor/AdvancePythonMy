import dis
from threading import Lock,RLock
# RLock:可重入锁：在同一个线程里面可以连续多次调用acquire获得锁，但是必须要连续调用相同次数的release来释放锁
global a

def add2(a):
    a += 1
    return a

def sub2(a):
    a -= 1
    return a

# if __name__=="__main__":
#     print(dis.dis(add2))
#     print("====================")
#     print(dis.dis(sub2))

total = 0
# lock = Lock()
lock = RLock()

def add():
    global total,lock
    for i in range(100000):
        lock.acquire()
        # print("第1次上锁")
        lock.acquire()
        # print("第2次上锁")
        total +=1
        mul(lock)
        lock.release()
        lock.release()
    return total

def mul(lock):
    global total
    lock.acquire()
    total *= 1
    lock.release()
    return total
def sub():
    global total
    for i in range(100000):
        lock.acquire()
        total -=1
        lock.release()
    return total

# 发生死锁的情况：
# 1、忘了释放锁
# 2、资源竞争导致死锁
# A(a,b)
#   require(a)
#   do something for a
#   require(b)
#   do something for b
#   release(b)
#   release(a)

# B(a,b)
#   require(b)
#   do something for b
#   require(a)
#   do something for a
#   release(a)
#   release(b)
# 在同一个线程内部发生函数调用，在被调用的函数内部再去申请锁

if __name__=="__main__":
    from threading import Thread
    add_thread = Thread(target=add)
    sub_thread = Thread(target=sub)
    add_thread.start()
    sub_thread.start()
    add_thread.join()
    sub_thread.join()
    print(total)

