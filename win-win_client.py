#!/usr/bin/env python
from socket import *
HOST = '127.0.0.1'      #服务器的地址
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM) 
tcpCliSock.connect(ADDR)
while True:
  data = input('>')
  if  data == 'exit':
    break
  tcpCliSock.send(data.encode())      #发送给服务器的数据
  data = tcpCliSock.recv(1024).decode()   #接收数据
  if data == 'exit':
    break
  print (data)
tcpCliSock.close()
