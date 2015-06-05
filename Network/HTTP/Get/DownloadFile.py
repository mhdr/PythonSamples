import socket

CRLF = "\r\n"

address="127.0.0.1"
port=80
file="Keygen.jar"

encoding="latin-1"

get_line="GET /{0} HTTP/1.1".format(file)
host_line="Host: {0}".format(address)

request = [
    get_line,
    host_line,
    "Connection: Keep-Alive",
    "",
    "",
]

# Connect to the server
s = socket.socket()
s.connect((address,port))

requestStr=CRLF.join(request)

# Send an HTTP request
s.send(requestStr.encode(encoding))

# Get the response (in several parts, if necessary)
response = ''
progress=0
buffer = s.recv(4096)
while buffer:
    response += bytes.decode(buffer,encoding)
    progress +=len(buffer)
    print(progress)
    buffer = s.recv(4096)

# HTTP headers will be separated from the body by an empty line
header_data, _, body = response.partition(CRLF + CRLF)

file=open(file,"wb")
file.write(body.encode(encoding))
file.flush()
file.close()