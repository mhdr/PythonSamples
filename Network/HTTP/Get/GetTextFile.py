import socket

CRLF = "\r\n"

request = [
    "GET /hello.txt HTTP/1.1",
    "Host: localhost",
    "Connection: Close",
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

# HTTP headers will be separated from the body by an empty line
header_data, _, body = response.partition(CRLF + CRLF)

#print header_data
print(response)