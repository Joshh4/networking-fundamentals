# Include socket library
from socket import *

server_port = 12000

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
    print("Connection from", addr)

    # Read bytes from new connection socket (conn)
    message = conn.recv(1024).decode()
    modified_message = message.upper()

    print("Received", message, "from", addr)

    # Send modified message back to client
    conn.send(modified_message.encode())

    # Close client connection (but not this server)
    conn.close()
