from socket import *

serverName = '127.0.0.1'  # 如果是域名，自动调用DNS
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))  # 发起连接
message = input('输入小写字符:')
clientSocket.send(message.encode())
recv_content = clientSocket.recv(2048)
print(recv_content.decode())
clientSocket.close()