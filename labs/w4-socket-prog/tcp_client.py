# Include socket library
from socket import *

server_ip = "192.168.15.23"
server_port = 12000

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
