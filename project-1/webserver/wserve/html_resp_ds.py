# This file holds HTML response data structures

import typing
import datetime

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
            # TODO: Url decode v
            args[k] = v
        
        path = path.split("&", 1)[0]

        header_dict = {}
        for line in header_lines[1:]:
            if len(line) == 0:
                continue
            k, v = line.split(": ", 1)
            header_dict[k] = v
        
        return HTMLRequest(
            type_=type_,
            path=path,
            protocol=protocol,
            header=header_dict,
            args=args,
            body=body)
    
    @staticmethod
    def from_values(*args, **kwargs):
        return HTMLRequest(*args, **kwargs)

class HTMLResponse(object):
    def __init__(self,
                 status_int:int,
                 status_str:str,
                 date:datetime.datetime,
                 connection_type:str,
                 keep_alive:str,
                 content_encoding:str,
                 content_type:str,
                 last_modified:datetime.datetime,
                 body:str):
        self.status_int:int = status_int
        self.status_str:str = status_str
        self.date:datetime.datetime = date
        self.connection_type:str = connection_type
        self.keep_alive:str = keep_alive
        self.content_encoding:str = content_encoding
        self.content_type:str = content_type
        self.last_modified:datetime.datetime = last_modified
        self.body:str = body
    
    def compile(self) -> bytes:
        s = ""

        s += f"{self.status_int} {self.status_str}\r\n"
        s += f"Connection: {self.connection_type}\r\n"
        s += f"Content-Type: {self.content_type}\r\n"
        s += f"Content-Length: {len(self.body)}\r\n"
        s += f"Date: {...}\r\n"

        # TODO:
        # Format date


        '''
        from datetime import datetime, timezone, timedelta

        # Get the current time in local timezone
        local_time = datetime.now()

        # Convert local time to GMT (UTC)
        gmt_offset = timezone.utc.utcoffset(None)
        gmt_time = local_time - gmt_offset

        # Format the GMT time
        formatted_date = gmt_time.strftime('%a, %d %b %Y %H:%M:%S GMT')

        print(formatted_date)'''

        s += "\r\n"

        s += self.body+"\r\n"

        return s.encode()