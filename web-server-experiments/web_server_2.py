import os, sys

# Import socket module
from socket import *

# Prepare a sever socket
server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.bind(("", 19225))
server_sock.listen(1)

while True:

    # Establish the connection
    print('Ready to serve...')
    conn, addr = server_sock.accept()

    try:
        message = conn.recv(1024)
        if len(message) == 0: # Client disconnected through closing tab?
            continue

        filename = message.split()[1].decode()
        with open(filename[1:], "r") as buffer:
            file_content = buffer.read()
        
        print(f"Client requested {filename[1:]}, gathered content and sending...")
        
        # Send HTTP header line(s) into socket
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        if os.path.splitext(filename)[1] == ".html":
            conn.send("Content-Type: text/html\r\n\r\n".encode())
        conn.send("\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(file_content)):
            conn.send(file_content[i].encode())
        conn.send("\r\n".encode())
        conn.close()

    except IOError:
        print(f"IOError, assuming 404")

        # Send response message for file not found
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/html\r\n\r\n".encode())
        conn.send(f"<html><head></head><body><h1>404 Not Found</h1><p>The requested file at {filename} could not be found on the server.</p></body></html>\r\n".encode())

        # Close client socket
        conn.close()