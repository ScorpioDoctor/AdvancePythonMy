import threading
import time
from random import randint
from queue import Queue

def get_url_list(url_queue):
    # 爬取文章列表页的url：生产者
    print("get_url_list  begining")
    while True:
        for i in range(10):
            url_queue.put("www.studyai.com/"+str(randint(1,2000))+"/")
        time.sleep(2)
        print("生产者又生产了10个url")


def get_html_detail(id,url_queue):
    # 爬取url列表中的文章的详情页：消费者
    print("#"+str(id)+" get_html_detail  begining")
    while True:
        print("剩余url个数：", url_queue.qsize())
        if not url_queue.empty():
            # for url in url_list:
            url = url_queue.get()
            print("#"+str(id)+" 正在爬取详情页："+url)
            time.sleep(1)
        else:
            print("url 队列 为空啦~~")
            # url_queue.task_done()
            # break


if __name__ == "__main__":
    start_time = time.time()
    url_queue = Queue(maxsize=50)
    list_thread = threading.Thread(target=get_url_list,args=(url_queue,))
    list_thread.start()
    # list_thread.join()
    detail_threads=[]
    for k in range(5):
        detail_thread = threading.Thread(target=get_html_detail,args=(k,url_queue))
        detail_threads.append(detail_thread)
        detail_thread.start()
        # detail_thread.join()
    url_queue.join()
    consumed_time = time.time() - start_time
    print("time consumed: ", consumed_time)
