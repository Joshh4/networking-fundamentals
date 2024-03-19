import socket
import dataclasses
import typing


@dataclasses.dataclass
class html_request:
    type: str
    path: str
    protocol: str
    header: typing.Dict[str, str]
    args: typing.Dict[str, str]
    body: str


class WebServer():
    def __init__(self):
        self.routes = {}
        self.port = 0
    
    def route(self, path:str):
        # TODO: Check func for request kwarg and mark it
        # so the code below only tries to parse request to
        # func if it's a proper argument.
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def receive_and_parse_request(self, conn:socket.socket):
        r = conn.recv(1024)
        if len(r) == 0:
            return None

        r = r.decode()
        parts = r.split("\r\n\r\n")
        header, body = parts

        header_lines = header.split("\r\n")
        body_lines = body.split("\r\n")

        type_, path, protocol = header_lines[0].split(" ", 2)

        args = {}
        for entry in path.split("&")[1:]:
            k, v = entry.split("=",1)
            # TODO: Url decode v
            args[k] = v
        
        path = path.split("&", 1)[0]

        header_dict = {}
        for line in header_lines[1:]:
            if len(line) == 0:
                continue
            k, v = line.split(": ", 1)
            header_dict[k] = v
        
        return html_request(
            type=type_,
            path=path,
            protocol=protocol,
            args=args,
            header=header_dict,
            body=body)

    def run(self, ip:str, port:int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(1)

        while True:
            conn, addr = self.sock.accept()
            request = self.receive_and_parse_request(conn)
            if request is None:
                continue

            callback = self.routes.get(request.path)
            callback_kwargs = {
                "request": request
            }

            if callback is not None:
                status, result = callback(**callback_kwargs)
                conn.send(f"HTTP/1.1 {status} OK\r\n".encode())
                conn.send(b"Content-Type: text/html\r\n\r\n")
                conn.send(result.encode())
            else:
                conn.send(b"HTTP/1.1 200 OK\r\n")
                conn.send(b"Content-Type: text/html\r\n\r\n")
                conn.send(f"<html><head></head><body><h1>404 Not Found</h1><p>The requested path \"{request.path}\" was not found.</p></body></html>\r\n".encode())
            conn.close()


if __name__ == "__main__":
    print("WebServer main is running")

    ws = WebServer()
    
    @ws.route("/")
    def root(request:html_request=None):
        return 200, "Hello, World!... "+request.args.get("q")
    
    @ws.route("/index")
    def index(request:html_request=None):
        return 200, "This is the index page"

    ws.run("", 3882)