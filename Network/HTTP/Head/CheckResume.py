import socket

CRLF = "\r\n"

request = [
    "HEAD /hello.txt HTTP/1.1",
    "Host: localhost",
    "Connection: Close",
    "Range: bytes=0-5",
    "",
    "",
]

# Connect to the server
s = socket.socket()
s.connect(('localhost', 80))

# Send an HTTP request
s.send(CRLF.join(request))

# Get the response (in several parts, if necessary)
response = ''
buffer = s.recv(4096)
while buffer:
    response += buffer
    buffer = s.recv(4096)

print(response)