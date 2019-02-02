#1. epoll 并不代表一定比select好
#2. 在并发高而连接活跃度不是很高的情况下，epoll 比 select 好（例如:Web页面请求）
#3. 并发低而连接活跃度很高的情况下，select比epoll好: （例如：游戏场景）

#通过非阻塞IO模拟实现HTTP请求
# requests --> urllib  --->  socket
import socket
from urllib.parse import urlparse
# import sys
# print(sys.getdefaultencoding())

def get_url(url):
    # 解析URL地址
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立 socket 连接，
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False) #设置成非阻塞
    try:
        client.connect((host, 80))# 阻塞会导致CPU空转
    except BlockingIOError as e:
        pass
    # 非阻塞会不断的询问连接是否建立好，需要while循环不停的检查状态
    # 做计算任务，不需要依赖连接的建立
    # 请求 html 页面
    while True:
        try:
            client.send("GET {0} HTTP/1.1 \r\nHost:{1}\r\nConnection:close\r\n\r\n".
                        format(path, host).encode("utf-8"))
            break
        except OSError as e:
            pass

    data = b''
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8",'ignore')
    print(data)
    client.close()


if __name__ == "__main__":
    get_url("http://studyai.com/course/index/")
