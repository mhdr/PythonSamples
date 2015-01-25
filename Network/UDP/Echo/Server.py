import socket

host=""
port=9001

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

while True:
    dataB,address=s.recvfrom(1024)
    print(address)

    s.sendto(dataB,address)
    data=bytes.decode(dataB)
    print(data)