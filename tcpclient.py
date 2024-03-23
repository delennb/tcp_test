import socket
import sys
import codecs

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12600)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    # print >>sys.stderr, 'sending "%s"' % message
    print('sending "%s"' % message, file=sys.stderr)
    sock.sendall(bytes(message, 'utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        print('test')
        data = sock.recv(16)
        amount_received += len(data)
        # print >>sys.stderr, 'received "%s"' % data
        print( 'received "%s"' % data, file=sys.stderr)
        # print(data.decode(encoding='utf-8', errors='strict'))
        # print(codecs.decode(data, "hex_codec"))

finally:
    # print >>sys.stderr, 'closing socket'
    print('closing socket', file=sys.stderr)
    sock.close()