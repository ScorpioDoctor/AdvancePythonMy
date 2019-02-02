import threading
import time
from random import randint

url_list=[]

def get_url_list():
    global url_list
    # 爬取文章列表页的url：生产者
    print("get_url_list  begining")
    while True:
        for i in range(10):
            url_list.append("www.studyai.com/"+str(randint(1,2000))+"/")
        time.sleep(2)
        print("生产者又生产了10个url")


def get_html_detail(id):
    global url_list
    # 爬取url列表中的文章的详情页：消费者
    print("get_html_detail  begining")
    while True:
        print("剩余url个数：", len(url_list))
        if len(url_list)>0:
            # for url in url_list:
            url = url_list.pop()
            print("#"+str(id)+" 正在爬取详情页："+url)
            time.sleep(1)
        else:
            print("url 列表为空啦~~")
            # break


if __name__ == "__main__":
    start_time = time.time()
    list_thread = threading.Thread(target=get_url_list)
    list_thread.start()
    # list_thread.join()
    detail_threads=[]
    for k in range(5):
        detail_thread = threading.Thread(target=get_html_detail,args=(k,))
        detail_threads.append(detail_thread)
        detail_thread.start()
        # detail_thread.join()
    consumed_time = time.time() - start_time
    print("time consumed: ", consumed_time)
