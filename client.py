#! /bin/python

import socket
import sys
import subprocess

IP_ADDRESS= "'172.16.1.4'"
PORT = 9999
print IP_ADDRESS
print PORT
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address =('172.16.1.4', 9999)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    
    subprocess.check_output('ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -N ""',shell=True,) 
    # Send data
    message = subprocess.check_output('cat /root/.ssh/id_rsa.pub',shell=True,)
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
