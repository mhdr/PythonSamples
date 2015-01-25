import socket

host="127.0.0.1"
port=9001
message="Hello World"
messageB=str.encode(message)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(messageB,(host,port))

dataB,address=s.recvfrom(1024)
data=bytes.decode(dataB)

print(dataB)

s.close()