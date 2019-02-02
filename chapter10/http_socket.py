# requests --> urllib  --->  socket
import socket
from urllib.parse import urlparse


def get_url(url):
    # 解析URL地址
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立 socket 连接，
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(True) #设置成非阻塞
    client.connect((host, 80))# 阻塞会导致CPU空转
    # 非阻塞会不断的询问连接是否建立好，需要while循环不停的检查状态
    # 做计算任务，不需要依赖连接的建立
    # 请求 html 页面
    client.send("GET {0} HTTP/1.1 \r\nHost:{1}\r\nConnection:close\r\n\r\n".
                format(path, host).encode("utf-8"))
    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8",'ignore')
    print(data)
    client.close()


if __name__ == "__main__":
    get_url("http://studyai.com/course/index/")
