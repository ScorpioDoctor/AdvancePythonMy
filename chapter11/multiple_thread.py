import threading
import time


def get_url_list():
    print("get_url_list  begining")
    time.sleep(3)
    print("get_url_list  end")


def get_html_detail(url):
    print("get_html_detail  begining")
    time.sleep(6)
    print("get_html_detail  end")


class GetUrlList(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(self.name + "  begining")
        time.sleep(3)
        print(self.name + "  end")


class GetHtmlDetail(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(self.name + "  begining")
        time.sleep(6)
        print(self.name + "  end")


if __name__ == "__main__":
    # list_thread = threading.Thread(target=get_url_list)
    # detail_thread = threading.Thread(target=get_html_detail, args=("wwww.studyai.com",))
    list_thread = GetUrlList(name="url-list")
    detail_thread = GetHtmlDetail(name="html-detail")
    list_thread.setDaemon(True)
    detail_thread.setDaemon(True)
    start_time = time.time()
    list_thread.start()
    detail_thread.start()
    list_thread.join()
    detail_thread.join()
    consumed_time = time.time() - start_time
    print("time consumed: ", consumed_time)
