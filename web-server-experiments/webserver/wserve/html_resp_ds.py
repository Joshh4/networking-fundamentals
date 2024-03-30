# This file holds HTML response data structures

import typing
import datetime
import urllib

def get_current_gmt_time() -> str:
    gmt_offset = datetime.timezone.utc.utcoffset(None)
    gmt_time = datetime.datetime.now() - gmt_offset
    date_formatted = gmt_time.strftime("%a, %d %b %Y %H:%M:%S GMT")

class HTMLRequest(object):
    type:str
    path:str
    protocol:str
    header:typing.Dict[str,str]
    args:typing.Dict[str,str]
    body:str
    
    def __init__(self,
                 type_:str=None,
                 path:str=None,
                 protocol:str=None,
                 header:typing.Dict[str, str]=None,
                 args:typing.Dict[str, str]=None,
                 body:str=None):
        self._r = ""
        self.type = type_
        self.path = path
        self.protocol = protocol
        self.header = header
        self.args = args
        self.body = body
    
    @staticmethod
    def from_message(r:str):
        if len(r) == 0:
            return None

        parts = r.split("\r\n\r\n")
        header, body = parts

        header_lines = header.split("\r\n")
        body_lines = body.split("\r\n")

        type_, path, protocol = header_lines[0].split(" ", 2)

        args = {}
        for entry in path.split("&")[1:]:
            k, v = entry.split("=",1)
            args[k] = urllib.parse.unquote(v)
        
        path = path.split("&", 1)[0]

        header_dict = {}
        for line in header_lines[1:]:
            if len(line) == 0:
                continue
            k, v = line.split(": ", 1)
            header_dict[k] = v
        
        req = HTMLRequest(
            type_=type_,
            path=path,
            protocol=protocol,
            header=header_dict,
            args=args,
            body=body)
        req._r = r
        
        return req
    
    @staticmethod
    def from_values(*args, **kwargs):
        return HTMLRequest(*args, **kwargs)
    
    def get_accept_types(self) -> typing.List[str]:
        accept_ = self.header.get("Accept")
        if accept_ is None:
            return []
        return accept_.split(";",1)[0].split(",")

class HTMLResponse(object):
    header:typing.Dict[str, str]
    content:bytes

    def __init__(
            self,
            protocol:str,
            status_int:int,
            status_str:str,
            header:typing.Dict[str,str],
            content:bytes):
        self.protocol = protocol
        self.status_int = status_int
        self.status_str = status_str
        self.header = header
        self.content = content
    
    def compile(self) -> bytes:
        s = f"{self.protocol} {self.status_int} {self.status_str}\r\n".encode()
        for k,v in self.header.items():
            s += f"{k}: {v}\r\n".encode()
        s += b"\r\n"
        if len(self.content) > 0:
            s += self.content
            s += b"\r\n"
        return s
    
    @staticmethod
    def basic_text_html(
            status_int:int,
            status_str:str,
            content:bytes,
            content_type="text/html; charset=utf-8"):
        header = {}
        header["Connection"] = "close"
        header["Content-Type"] = content_type
        header["Date"] = get_current_gmt_time()
        if len(content) > 0:
            header["Content-Length"] = len(content)
        return HTMLResponse("HTTP/1.1", status_int, status_str, header, content)
    
    @staticmethod
    def image(
            status_int:int,
            status_str:str,
            image_format:str,
            content:bytes):
        header = {}
        header["Connection"] = "close"
        header["Content-Type"] = "image/"+image_format
        header["Date"] = get_current_gmt_time()
        header["Content-Length"] = len(content)
        return HTMLResponse("HTTP/1.1", status_int, status_str, header, content)