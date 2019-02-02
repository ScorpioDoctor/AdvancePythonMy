import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 6000))
server.listen()
print("服务器开始监听...")

# 处理与单个客户端的会话
def handle_session(sock, remote_addr):
    while True:
        data = sock.recv(256)
        data = data.decode("utf-8")
        # print(type(data))
        print("客户端说：", data)
        server_msg = input()
        sock.send(server_msg.encode("utf-8"))


while True:
    sock, remote_addr = server.accept()
    # print(sock, remote_addr)
    session_thread = threading.Thread(target=handle_session,args=(sock,remote_addr))
    session_thread.start()
    # sock.close()
    # server.close()
