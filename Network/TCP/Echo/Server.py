__author__ = 'Mahmood'

import socket

host = ""
port = 9001

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen(1)

newSocket, address = serverSocket.accept()

print("new connection from" , address)

while True :
    data=newSocket.recv(1024)
    if data :
            print("data",bytes.decode(data,"utf-8"))
            newSocket.sendall(data)


newSocket.close()



