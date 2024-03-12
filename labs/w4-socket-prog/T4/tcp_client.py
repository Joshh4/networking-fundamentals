import sys

# Include socket library
from socket import *

server_ip = "172.19.126.234"

# Ask user for port # and exit if not within required range
server_port = int(input("Enter port # "))
if server_port < 1024 or server_port > 65535:
    print("Server port must be > 1024 and < 65536")
    sys.exit(-1)

# Create TCP server socket
sock = socket(AF_INET, SOCK_STREAM)

# Connect to remote server at port 12000
sock.connect((server_ip, server_port))
message = input("Input a lower case sentence: ")

# No need to attach server ip or port
sock.send(message.encode())

# Wait to receive from server
modified_message = sock.recv(1024).decode()

# Print out received string and close connection
print("From server:", modified_message)
sock.close()
