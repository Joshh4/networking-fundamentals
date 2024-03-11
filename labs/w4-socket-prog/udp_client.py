# Include socket library
from socket import *

# The destination
server_ip = "192.168.15.23"
server_port = 12000

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
