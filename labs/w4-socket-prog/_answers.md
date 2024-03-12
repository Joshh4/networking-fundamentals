# Lab Tasks


## T1

1. Suppose you run TCPClient before TCPServer. What happens? Why?

   If you run TCPClient before TCPServer, a TimeoutError occurs. See the error below.

   ```
   Traceback (most recent call last):
      File "c:\Users\chall\OneDrive\Documents\Programming\Projects\networking-fundamentals\labs\w4-socket-prog\T4\tcp_client.py", line 19, in <module>
      sock.connect((server_ip, server_port))
      TimeoutError: timed out
   ```

   The reason this happens is because there is no server for the client to connect to.
   

2. Suppose you run UDPClient before you run UDPServer. What happens? Why?

   Running UDPClient before UDPServer allows the client to send,
   but the program will hang forever.


3. What happens if you use different port numbers for the client and server sides?

   If you use different port numbers, the client cannot find the
   server so the same issue(s) happen as above. The TCP system will run into a TimeoutError,
   and the UDP system will hang.


4. (Q was optional)


## T2

If we add the line sock.bind(("", 5432)) to the client, we find
that the address the server receives from has the provided port
that the client binded to. If we omit the bind line, the client
will have whatever port the server decides to assign.

This can be tested by adding the line `print(client_addr)` to
the server right after the message and addr is received.


## T3

See ./T3 for appropriate edits to code.


## T4

See ./T4 for appropriate edits to code.