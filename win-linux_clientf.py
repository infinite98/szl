# encoding: utf-8
from socket import *
HOST = "118.228.168.70"   #服务端的地址
PORT = 23333
ADDR = (HOST,PORT)
client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)
with open("gg.txt","ab") as f:   #打开准备接收数据的文件
  while True:
    data = client.recv(1024)  #接收文件
    if not data:
      break;
    f.write(data)
f.close()
print("接收完毕")
client.close()
