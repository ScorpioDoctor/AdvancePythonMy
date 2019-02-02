import threading
import time
from random import randint

url_list = []


def get_url_list():
    global url_list
    print("get_url_list  begining")
    while True:
        time.sleep(2)
        for i in range(10):
            url_list.append("www.studyai.com/" + str(randint(1,100000)) + "/")
        print("get_url_list:  10 urls generated")
        print("get_url_list:  url count: "+str(len(url_list)))


def get_html_detail(id):
    global url_list
    time.sleep(3)
    # for url in url_list:
    #     print("get_detail: " + url + " begining")
    #     time.sleep(1)
    #     print("get_detail  end")
    while True:
        if len(url_list)>0:
            url = url_list.pop()
            print("#"+str(id)+"->get_detail: " + url + " begining")
            time.sleep(1)
        else:
            print("#"+str(id)+"->get_detail  end")
            break

if __name__ == "__main__":
    list_thread = threading.Thread(target=get_url_list)
    detail_thread = threading.Thread(target=get_html_detail,args=(0,))
    detail_thread1 = threading.Thread(target=get_html_detail,args=(1,))
    # list_thread.setDaemon(True)
    # detail_thread.setDaemon(True)
    start_time = time.time()
    list_thread.start()
    detail_thread.start()
    detail_thread1.start()
    list_thread.join()
    detail_thread.join()
    detail_thread1.join()
    consumed_time = time.time() - start_time
    print("time consumed: ", consumed_time)
