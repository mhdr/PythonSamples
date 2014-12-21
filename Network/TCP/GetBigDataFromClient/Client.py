__author__ = 'Mahmood'

import socket
import struct

host = "127.0.0.1"
port = 9001

msg = ""
for i in range(0, 10000):
    msg += "Mahmood\n"

msgB=str.encode(msg)

length=len(msgB)
lengthPacked=struct.pack("i",length)
data=lengthPacked+msgB

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(data)
s.close()

