import socket

__author__ = 'mahmood'

class SocketManager:

    def get_next_socket(self):

        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        return s