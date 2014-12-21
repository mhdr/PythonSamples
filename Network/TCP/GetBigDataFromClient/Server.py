__author__ = 'Mahmood'

import socket
import struct

host = ""
port = 9001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
    newSock, address = s.accept()

    lengthPacked= newSock.recv(4)
    lengthUnpacked=struct.unpack("i",lengthPacked)
    length=lengthUnpacked[0]
    data= newSock.recv(length)


    newSock.close()

    dataStr = bytes.decode(data)
    print(dataStr)
    print("... connection closed ...")
