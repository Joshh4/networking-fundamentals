import sys

# Include socket library
from socket import *

# Ask user for port # and exit if not within required range
server_port = int(input("Enter port # "))
if server_port < 1024 or server_port > 65535:
    print("Server port must be > 1024 and < 65536")
    sys.exit(-1)

# Create UDP socket
sock = socket(AF_INET, SOCK_DGRAM)

# Bind socket to local port number 12000
sock.bind(("", server_port))
print("The server is running and ready")

# Loop forever
while True:

    # Read from UDP socket into message, getting client's address (ip, port)
    message, client_addr = sock.recvfrom(2048)
    modified_message = message.decode().upper()

    # Send upper-case string back to this client
    sock.sendto(modified_message.encode(), client_addr)
