import time
from concurrent import futures

future = futures.Future() # 未来对象：作为task的返回容器


# futures为我们提供了管理线程池的方法
# 为什么需要线程池？
# 可以像 Semaphore 那样控制并发线程的数量
# 在主线程中获取某个子线程的状态或者某一个任务的状态，以及返回值
# 当一个子线程完成的时候，主线程能够立即知道
# futures 可以让多线程编程和多进程编程的代码规范和接口一致


def spider(idx, times):
    time.sleep(times)
    print("#" + str(idx) + "-->当前页面成功爬取~~")
    return "#" + str(idx) + "---" + str(times)


def spider2(params):
    idx=params.get("idx")
    times=params.get("times")
    time.sleep(times)
    print("#" + str(idx) + "-->当前页面成功爬取~~")
    return "#" + str(idx) + "---" + str(times)

executor = futures.ThreadPoolExecutor(max_workers=2)

# submit() 可以把待执行的函数提交到线程池,提交完之后立即返回
# task1 = executor.submit(spider,idx=1,times=4)
# task2 = executor.submit(spider,2,2)
# task3 = executor.submit(spider,2,2)
# # time.sleep(3)
# # cancel() 把尚未运行的子线程从线程池里面取消掉
# task2.cancel()
# # done()方法是Future类提供的，用来判断任务是否完成
# print(task1.done())
# print(task2.done())
# # result 方法是Future类提供的，用来获取执行结果
# print(task1.result())
# print(task2.result())

# as_completed 获取已经执行完毕的子线程，还可以得到子线程的返回值
urls = [(1, 3), (2, 1), (3, 2)]
all_tasks = [executor.submit(spider, idx, times) for idx, times in urls]
# futures.wait(all_tasks)
# print("所有线程执行完毕了")
futures.wait(all_tasks,return_when=futures.FIRST_COMPLETED)
print("有一个线程执行完毕了")

for future in futures.as_completed(all_tasks):
    result = future.result()
    print(result)

# print("=================")
# # 通过 executor 的 map()方法获取已经完成的子线程的返回值
# urls = [{"idx":1,"times":3}, {"idx":2,"times":1}, {"idx":3,"times":2}]
# for result in executor.map(spider2,urls):
#     print(result)

