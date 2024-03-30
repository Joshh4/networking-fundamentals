import socket
import dataclasses
import typing
import urllib.parse

from . import html_resp_ds


class WebServer():
    def __init__(self):
        self.routes = {}
        self.port = 0
    
    def route(self, path:str):
        # TODO: Check func for request kwarg and mark it
        # so the code below only tries to parse request to
        # func if it's a proper argument.
        def __decorator(func):
            self.routes[path] = func
            return func
        return __decorator

    def receive_and_parse_request(self, conn:socket.socket) -> typing.Union[html_resp_ds.HTMLRequest, None]:
        r = conn.recv(1024)
        if len(r) == 0:
            return None
        r = r.decode()
        return html_resp_ds.HTMLRequest.from_message(r)

    def run(self, ip:str, port:int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(1)

        while True:
            conn, addr = self.sock.accept()
            request = self.receive_and_parse_request(conn)

            if request is None:
                continue
            
            print(request._r)
            print(request.type, request.path, request.args)

            sec_fetch_dest = request.header.get("Sec-Fetch-Dest")
            display_404 = False

            if sec_fetch_dest == "document":
                callback = self.routes.get(request.path)
                callback_kwargs = { "request": request }

                if callback is not None:
                    status, callback_result = callback(**callback_kwargs)

                    response = html_resp_ds.HTMLResponse.basic_text_html(
                        status_int=200,
                        status_str="OK",
                        content=callback_result.encode() 
                    )
                    conn.send(response.compile())
                
                else:
                    display_404 = True
            
            elif sec_fetch_dest == "image":
                with open(request.path[1:], "rb") as buffer:
                    content = buffer.read()

                response = html_resp_ds.HTMLResponse.image(
                    status_int=200, status_str="OK",
                    image_format="jpg", content=content
                )
                conn.send(response.compile())
            
            if display_404:
                response = html_resp_ds.HTMLResponse.basic_text_html(
                    status_int=404,
                    status_str="Not Found",
                    content=f"<html><head></head><body><h1>404 Not Found</h1><p>The requested path \"{request.path}\" was not found.</p></body></html>\r\n".encode()
                )
                conn.send(response.compile())
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