import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 12600)
# print >>sys.stderr, 'starting up on %s port %s' % server_address
print('TCP Server: starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

gds_address = ('localhost', 50050)
print('To GDS: connecting to %s port %s' % gds_address, file=sys.stderr)
sock2.connect(gds_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('TCP Server: waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        print('TCP Server: connection from', client_address, file=sys.stderr)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)

            print('TCP Server: received from FSW"%s"' % data, file=sys.stderr)
            if data:
                print('TCP Client: sending data to the GDS', file=sys.stderr)
                sock2.sendall(data)

                data2 = sock2.recv(16)
                print( 'TCP Client: received from GDS "%s"' % data2, file=sys.stderr)


                print("TCP Server: hopefully sending data back to FSW")
                connection.sendall(data2)

            else:
                print('TCP Server: no more data from', client_address, file=sys.stderr)
                break
        
    finally:
        # Clean up the connection
        connection.close()
    