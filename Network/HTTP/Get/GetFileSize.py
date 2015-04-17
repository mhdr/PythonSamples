import socket

CRLF = "\r\n"

request = [
    "HEAD /Keygen.exe HTTP/1.1",
    "Host: 192.168.150.129",
    "Connection: Keep-Alive",
    "",
    "",
]

# Connect to the server
s = socket.socket()
s.connect(('192.168.150.129', 80))

# Send an HTTP request
s.send(CRLF.join(request))

# Get the response (in several parts, if necessary)
response = ''
buffer = s.recv(4096)
while buffer:
    response += buffer
    buffer = s.recv(4096)

#print(response)

headers= response.split(CRLF)

for h in headers :
    label,_,value=h.partition(":")
    if label.strip()=="Content-Length":
        print(value.strip())