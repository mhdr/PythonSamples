__author__ = 'Mahmood'

import socket
import threading


def forward(source, destination):

    string = ' '
    while string:
        string = source.recv(1024)
        if string:
            destination.sendall(string)
        else:
            source.shutdown(socket.SHUT_RD)
            destination.shutdown(socket.SHUT_WR)


host = ""
port = 9003

dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dock_socket.bind((host, port))
dock_socket.listen(1000)

while True:
    client_socket = dock_socket.accept()[0]
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(client_socket.getsockname())

    threading.Thread(target=forward, args=(client_socket, server_socket)).start()
    threading.Thread(target=forward, args=(server_socket, client_socket)).start()






