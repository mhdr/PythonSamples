__author__ = 'Mahmood'

import socket

host="127.0.0.1"
port=9001

name="Mahmood"
nameB=str.encode(name)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.sendall(nameB)
data= s.recv(1024)
dataStr=bytes.decode(data)

print("Server sent : {0}".format(dataStr))

s.close()

