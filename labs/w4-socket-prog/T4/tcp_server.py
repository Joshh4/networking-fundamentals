import sys

# Include socket library
from socket import *

# Ask user for port # and exit if not within required range
server_port = int(input("Enter port # "))
if server_port < 1024 or server_port > 65535:
    print("Server port must be > 1024 and < 65536")
    sys.exit(-1)

# Create TCP welcoming socket
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", server_port))

# Server begins listening for incoming TCP requests
sock.listen(1)
print("The server is running and ready")

# Loop forever
while True:

    # Server waits on accept() for incoming requests; new socket created on return
    conn, addr = sock.accept()

    # Read bytes from new connection socket (conn)
    message = conn.recv(1024).decode()
    modified_message = message.upper()

    # Send modified message back to client
    conn.send(modified_message.encode())

    # Close client connection (but not this server)
    conn.close()
