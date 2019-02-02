# gil : global interpreter lock （全局解释器锁）（cpython）
# python 中的一个线程对应于c语言中的一个线程
# gil 使得同一时刻只有一个线程在一个CPU上面执行字节码，无法将多个线程映射到多个CPU上执行

def add2(a):
    a = a + 1
    return a

# import dis
# print(dis.dis(add2))

#全局解释器锁会在执行I/O操作或者是执行固定长度的字节码或者cpu时间片到了以后释放
total = 0
def add():
    global total
    for i in range(10000000):
        total +=1
    return total

def sub():
    global total
    for i in range(10000000):
        total -=1
    return total

if __name__=="__main__":
    # add()
    # print(total)
    # sub()
    # print(total)
    from threading import Thread
    add_thread = Thread(target=add)
    sub_thread = Thread(target=sub)
    add_thread.start()
    sub_thread.start()
    add_thread.join()
    sub_thread.join()
    print(total)