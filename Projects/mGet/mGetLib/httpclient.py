import socket
from urllib.parse import urlparse
import sys
from mGetLib.socketmanager import SocketManager


class HttpClient:

    def __init__(self, url):

        self.url = url
        self.extract_info_from_url()

    def extract_info_from_url(self):
        parsed_url = urlparse(self.url)

        if parsed_url.port == None:
            self.port = 80
        else:
            self.port = parsed_url.port

        self.hostname=parsed_url.hostname
        self.ip =socket.gethostbyname(parsed_url.hostname)
        self.scheme = parsed_url.scheme

        if parsed_url.path.startswith("/"):
            self.path = parsed_url.path[1:]
        else:
            self.path=parsed_url.path

    def get_file_size(self):

        if self.scheme == "http":
            return self.get_file_size_http()

    def get_file_size_http(self):

        try:
            CRLF = "\r\n"
            encoding="latin-1"

            if self.path=="" :
                return None

            head_line="HEAD /{0} HTTP/1.1".format(self.path)
            host_line="Host: {0}".format(self.hostname)

            request = [
                head_line,
                host_line,
                "Connection: Close",
                "",
                "",
            ]

            socket_manager=SocketManager()
            s=socket_manager.get_next_socket()

            s.connect((self.ip, self.port))

            request_line=CRLF.join(request)

            s.send(request_line.encode(encoding))

            response = ''
            buffer = s.recv(1024)
            while buffer:
                response += bytes.decode(buffer,encoding)
                buffer = s.recv(1024)

            s.close()

            header_data, _, body = response.partition(CRLF + CRLF)

            headers=header_data.split(CRLF)

            for header in headers:
                if header.startswith("Content-Length"):
                    h=header.split(":")

                    length= h[1].strip()
                    return length

            # if header doesn't exist return None
            return None

        except:

            # if error occurred return None
            return None

