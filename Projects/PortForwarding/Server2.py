__author__ = 'Mahmood'

import socket

host=""
port=9002

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)

while True :
    newSock, address=s.accept()
    data= newSock.recv(1024)

    if data :
        dataStr=bytes.decode(data)
        print("Client sent : {0}".format(dataStr))

        msg="Hello {0}".format(dataStr)
        msgB=str.encode(msg)
        newSock.sendall(msgB)

    newSock.close()
