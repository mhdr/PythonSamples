import socket

CRLF = "\r\n"

request = [
    "GET /hello.txt HTTP/1.1",
    "Host: 192.168.150.129",
    "Connection: Close",
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

# HTTP headers will be separated from the body by an empty line
header_data, _, body = response.partition(CRLF + CRLF)

#print header_data
print(body)