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

        print(message)

        filename = message.split()[1].decode()

        with open(filename[1:], "r") as buffer:
            file_content = buffer.read()
        
        # Send one HTTP header line into socket

        # Fill in start
        conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(file_content)):
            conn.send(file_content[i].encode())
        conn.send("\r\n".encode())
        conn.close()

    except IOError:
        # Send response message for file not found

        # Fill in start
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        conn.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Fill in end

        # Close client socket
        conn.close()

# Close the server socket
server_sock.close()
sys.exit() # Terminate the program after sending the corresponding data