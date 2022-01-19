from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# TCP 全连接队列 = min(somaxconn, backlog), backlog是listen() 中指定的参数
# TCP 全连接队列溢出后，由于 tcp_abort_on_overflow 内核参数默认为 0，服务端会丢掉客户端发过来的 ack，
# 如果你把该参数设置为 1，那现象将变成，服务端会给客户端发送 RST 报文，废弃掉连接。
serverSocket.listen(1)
print("server is listening")

while True:
    connSocket, client_addr = serverSocket.accept()
    print('接受到客户端请求', client_addr)
    message = connSocket.recv(1024)
    newmes = message.decode().upper()
    print('给客户端返回: ', newmes)
    connSocket.send(newmes.encode())
    connSocket.close()
