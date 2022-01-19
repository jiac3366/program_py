from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("server is listening")
while True:
    message, client_addr = serverSocket.recvfrom(2048)
    newmes = message.decode().upper()
    serverSocket.sendto(bytes(newmes, encoding='utf-8'), client_addr)