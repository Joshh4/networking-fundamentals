# Include socket library
from socket import *

server_port = 12000

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

    print("Received", message, "from", client_addr)

    # Send upper-case string back to this client
    sock.sendto(modified_message.encode(), client_addr)
