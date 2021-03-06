import socket

CRLF = "\r\n"

request = [
    "HEAD /proxy/OmegaRules_Auto_Switch.sorl HTTP/1.1",
    "Host: 80.84.55.200",
    "Connection: Close",
    "",
    "",
]

# Connect to the server
s = socket.socket()
s.connect(('80.84.55.200', 80))

# Send an HTTP request
s.send(CRLF.join(request))

# Get the response (in several parts, if necessary)
response = ''
buffer = s.recv(4096)
while buffer:
    response += buffer
    buffer = s.recv(4096)

print(response)
