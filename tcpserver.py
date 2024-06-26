import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 12600)
# print >>sys.stderr, 'starting up on %s port %s' % server_address
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    # print >>sys.stderr, 'waiting for a connection'
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        # print >>sys.stderr, 'connection from', client_address
        print('connection from', client_address, file=sys.stderr)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            # print >>sys.stderr, 'received "%s"' % data
            print('received "%s"' % data, file=sys.stderr)
            if data:
                # print >>sys.stderr, 'sending data back to the client'
                print('sending data back to the client', file=sys.stderr)
                connection.sendall(data)
            else:
                # print >>sys.stderr, 'no more data from', client_address
                print('no more data from', client_address, file=sys.stderr)
                break
        
    finally:
        # Clean up the connection
        connection.close()
    