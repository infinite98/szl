# _*_ coding:utf-8 _*_
from socket import *
import _thread
def tcplink(skt,addr):
  print(skt)
  print(addr,"已经连接上...")
  print('开始发送文件')
  with open(r'C:\Users\dell\Desktop\szl\win-Linux间文件/ww.txt', 'rb') as f:       #打开将要传输的文件
  for data in f:
    print(data)         #将文件的内容输出在屏幕上
    skt.send(data)      #将文件传输到客户机的相应文件夹中
  f.close()
  skt.close()
HOST = "118.228.168.70"
PORT = 23333
ADDR = (HOST,PORT)
server = socket(AF_INET,SOCK_STREAM)   #创建套接字
server.bind(ADDR)                #绑定地址到套接字
server.listen(5)          #开始进行TCP监听
while True:
  print("等待连接...")
  skt,addr = server.accept()   #被动接受TCP客户端连接,(阻塞式)等待连接的到来 
  print(skt)
  try:
    _thread.start_new_thread(tcplink,(skt,addr))  #创建一个新的线程，返回一个线程标识符
  except:
    print("线程无法启动")
server.close()
