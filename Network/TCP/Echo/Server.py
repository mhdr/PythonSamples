__author__ = 'Mahmood'

import socket

host = ""
port = 9001

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)

while True:
    newSocket, address = serverSocket.accept()
    print("new connection from", address)

    data = newSocket.recv(1024)
    if data:
        print("client sent :", bytes.decode(data, "utf-8"))
        newSocket.sendall(data)

    newSocket.close()



