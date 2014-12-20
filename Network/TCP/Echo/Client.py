__author__ = 'Mahmood'

import socket

host="127.0.0.1"
port=9001

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
clientSocket.connect((host,port))
clientSocket.sendall(str.encode("Hello World","utf-8"))
data=clientSocket.recv(1024)
clientSocket.close()

print("Recieved",bytes.decode(data,"utf-8"))
