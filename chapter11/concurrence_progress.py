#多进程编程：在操作系统中，进程的切换比线程的切换花费更多的时间
# 消耗CPU的操作比较多的时候，使用多进程编程
# 对于I/O操作比较频繁的程序，使用多线程编程
from concurrent.futures import ThreadPoolExecutor,as_completed,ProcessPoolExecutor

import time


def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)


if __name__=="__main__":
    # with ThreadPoolExecutor(3) as executor:
    with ProcessPoolExecutor(3) as executor:
        all_tasks = [executor.submit(fib, n) for n in range(28, 35)]
        start_time = time.time()
        for future in as_completed(all_tasks):
            result = future.result()
            print(result)
        print("花费时间：", time.time() - start_time)

def sleep_forwhile(n):
    time.sleep(n)
    return n

# if __name__=="__main__":
#     with ThreadPoolExecutor(3) as executor:
#     # with ProcessPoolExecutor(3) as executor:
#         all_tasks = [executor.submit(sleep_forwhile, n) for n in [2]*30]
#         start_time = time.time()
#         for future in as_completed(all_tasks):
#             result = future.result()
#             print(result)
#         print("花费时间：", time.time() - start_time)