import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",6000))

while True:
    msg = input()
    client.send(msg.encode("utf-8"))
    data = client.recv(256)
    print("服务器说：",data.decode("utf-8"))
    # client.close()
