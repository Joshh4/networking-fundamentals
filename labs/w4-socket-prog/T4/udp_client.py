import sys

# Include socket library
from socket import *

# The destination
server_ip = "172.19.126.234"

# Ask user for port # and exit if not within required range
server_port = int(input("Enter port # "))
if server_port < 1024 or server_port > 65535:
    print("Server port must be > 1024 and < 65536")
    sys.exit(-1)

# Create UDP socket for client
sock = socket(AF_INET, SOCK_DGRAM)

# Get user keyboard input
message = input("Input lowercase sentence: ")

# Attach server name, port to message; send into socket
sock.sendto(message.encode(), (server_ip, server_port))

# Read reply characters from socket into string
modified_message, server_addr = sock.recvfrom(2048)

# Print out received string and close socket
print(modified_message.decode())
sock.close()
