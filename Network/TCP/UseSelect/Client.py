# Echo client program
import socket

HOST = '192.168.1.104'    # The remote host
PORT = 11111
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))