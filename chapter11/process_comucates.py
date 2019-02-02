from multiprocessing import Process,Queue,Pool,Manager,Pipe
# from queue import Queue #只能用于线程通信
import time

def producer(queue):
    idx = 1
    while True:
        queue.put("面包#"+str(idx))
        print("生产了一个面包#"+str(idx))
        idx+=1
        time.sleep(2)

def consumer(queue):
    while True:
        time.sleep(1)
        data = queue.get()
        print("消费了一个: " + data)

def producer2(a):
    idx = 1
    while True:
        # queue.put("面包#"+str(idx))
        a=idx
        print("生产了一个面包#"+str(a))
        idx+=1
        time.sleep(2)

def consumer2(a):
    while True:
        time.sleep(1)
        data = str(a)
        print("消费了一个: " + data)

def producer3(pipe):
    idx = 1
    while True:
        pipe.send("面包#"+str(idx))
        print("生产了一个面包#"+str(idx))
        idx+=1
        time.sleep(1)

def consumer3(pipe):
    while True:
        data = pipe.recv()
        print("消费了一个: " + data)
        time.sleep(2)

def producer4(shared):
    idx = 1
    while True:
        shared[str(idx)]="面包#"+str(idx)
        print("生产了一个:" + shared[str(idx)])
        idx+=1
        time.sleep(2)

def consumer4(shared):
    while True:
        for key,value in shared.items():
            print("消费了一个: " + shared.pop(key))
            time.sleep(1)

if __name__=="__main__":
    # from multiprocessing import Queue
    # queue = Queue(9)
    # # a = 1
    # myproducer = Process(target=producer,args=(queue,))
    # myconsumer = Process(target=consumer,args=(queue,))
    # # myproducer = Process(target=producer2,args=(a,))
    # # myconsumer = Process(target=consumer2,args=(a,))
    # myproducer.start()
    # myconsumer.start()
    # myproducer.join()
    # myconsumer.join()
    # print("生产消费已经完毕！")

    #multiprocessing里面的Queue不能用于进程池通信
    # Manager().Queue()
    # pool = Pool(2)
    # queue = Manager().Queue(9)
    # pool.apply_async(producer,args=(queue,))
    # pool.apply_async(consumer,args=(queue,))
    # pool.close()
    # pool.join()

    # 通过 Pipe 进行进程间通信：只能用于两个进程通信，效率比较高，锁比较少
    # recv_pipe, send_pipe = Pipe()
    # myproducer = Process(target=producer3,args=(send_pipe,))
    # myconsumer = Process(target=consumer3,args=(recv_pipe,))
    # myproducer.start()
    # myconsumer.start()
    # myproducer.join()
    # myconsumer.join()
    # print("生产消费已经完毕！")

    # 进程间共享变量
    shared_dict= Manager().dict()
    myproducer = Process(target=producer4,args=(shared_dict,))
    myconsumer = Process(target=consumer4,args=(shared_dict,))
    myproducer.start()
    myconsumer.start()
    myproducer.join()
    myconsumer.join()
    print("生产消费已经完毕！")