from socket import *

serverName = '127.0.0.1' # 如果是域名，自动调用DNS
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('输入小写字符:')
clientSocket.sendto(bytes(message, encoding='gbk'), (serverName, serverPort))
recv_content, addr = clientSocket.recvfrom(2048)  # 区别tcp的recv() 因为是udp 所以谁都可以向客户端发起通信，所以要得知addr
print(recv_content.decode())
clientSocket.close()
