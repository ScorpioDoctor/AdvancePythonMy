# import os
# import time
# #fork只能用于linux/unix中，会返回两次
# print("antares")
# pid = os.fork()
# # print("antares")
# if pid == 0:
#     print('子进程id:{},父进程id:{}'.format(os.getpid(), os.getppid()))
# else:
#     print("我是父进程id:{}".format(pid))
#
# time.sleep(2)

# from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time
def spider(n):
    time.sleep(n)
    print("子进程成功执行！")
    return n

class Spider(multiprocessing.Process):
    def run(self):
        pass

if __name__=="__main__":
    # progress = multiprocessing.Process(target=spider,args=(3,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join(timeout=2)
    # print("主进程已结束！")

    # 进程池
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(spider,args=(3,))
    # # result1 = pool.apply_async(spider,args=(1,))
    # # 等待所有子进程完成
    # pool.close()
    # pool.join()
    # # print(result.get())
    # # print(result1.get())

    #imap 执行多个子进程
    # for result in pool.imap(spider,[1,4,2]):
    #     print("%s sleep ended" % (result))

    # imap_unordered
    for result in pool.imap_unordered(spider,[1,4,2]):
        print("%s sleep ended" % (result))