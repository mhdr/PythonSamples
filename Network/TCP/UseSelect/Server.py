import select
import socket

host=""
port=11111

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

readable_arg=[s]
writeable_arg=[]
exception_arg=[]

while True:
    readable_result,writeable_result,exception_result=select.select(readable_arg,writeable_arg,exception_arg)

    for current_socket in readable_result:
        if current_socket==s:
            newSocket,address=s.accept()
            newSocket.setblocking(True)
            readable_arg.append(newSocket)
        else:
            if isinstance(current_socket,socket.socket):
                data_recv= current_socket.recv(1024)
                print(data_recv)
                data=bytearray()

                current_socket.settimeout(1)
                while len(data_recv)>0:
                    data.extend(data_recv)
                    try:
                        data_recv= current_socket.recv(1024)
                    except socket.timeout:
                        break
                    print(data_recv)

                current_socket.sendall(b"End")
                readable_arg.remove(current_socket)
                current_socket.close()
                print(data)