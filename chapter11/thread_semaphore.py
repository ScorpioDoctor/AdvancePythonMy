import threading

import time


class SpiderConsumer(threading.Thread):
    def __init__(self,url, name,sema):
        super().__init__(name=name)
        self.url = url
        self.sema = sema

    def run(self):
        time.sleep(2)
        print("#"+self.name+"-->当前页面成功爬取~~")
        self.sema.release()


class UrlProducer(threading.Thread):
    def __init__(self,sema):
        self.sema = sema
        super().__init__(name="url 生产者")

    def run(self):
        for i in range(150):
            url = "www.studyai.com/news/detail/{0}/".format(i)
            self.sema.acquire()
            spider = SpiderConsumer(url, str(i), self.sema)
            spider.start()




if __name__=="__main__":
    # 计数信号量
    sema = threading.Semaphore(value=5)
    url_producer = UrlProducer(sema)
    url_producer.start()