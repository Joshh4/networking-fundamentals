import socket

def construct_resp(status:str) -> str:
    ...

class WebServer():
    def __init__(self, port:int):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", self.port))
        self.sock.listen(1)
    
    def run(self):
        """This function runs a loop answering and handling
        client requests, and triggering appropriate response functions
        as required.
        """

        while True:
            conn, addr = self.sock.accept()
            
            try:
                message = conn.recv(1024)
                if len(message) == 0:
                    continue # Client closed tab
            
            except IOError:
                print(f"IOError, assuming 404")

if __name__ == "__main__":
    print("WebServer main is running")

    ws = WebServer(19225)
    ws.run()