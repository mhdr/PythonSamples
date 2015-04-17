import socket

CRLF = "\r\n"

request = [
    "GET /Keygen.exe HTTP/1.1",
    "Host: 192.168.150.129",
    "Connection: Keep-Alive",
    "Accept-Encoding: gzip, deflate",
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
progress=0
buffer = s.recv(4096)
while buffer:
    response += buffer
    progress +=len(buffer)
    print(progress)
    buffer = s.recv(4096)

# HTTP headers will be separated from the body by an empty line
header_data, _, body = response.partition(CRLF + CRLF)

file=open("Keygen.exe","wb")
file.write(body)
file.flush()
file.close()