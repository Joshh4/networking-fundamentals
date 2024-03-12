# Lab Tasks

## T1

1. If you run TCPClient before TCPServer, a TimeoutError occurs.
   
2. Running UDPClient before UDPServer allows the client to send,
   but the program will hang forever.

3. If you use different port numbers, the client cannot find the
   server so the same issue(s) happen as above.

4. (optional)

## T2

If we change client to use sock.bind(("", 5432)), we must also
change UDPServer.py, switching the port number to 5432, otherwise
the client cannot recv any data because the server originally runs
on port 12000.

## T3

See ./T3 for appropriate edits to code.

## T4

See ./T4 for appropriate edits to code.