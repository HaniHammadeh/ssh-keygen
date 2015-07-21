#! /bin/python

import socket
import sys
import threading
import subprocess



#data = ''
#server_address = '0.0.0.0'
client_address = '0.0.0.0'
#connection = ''
#IP_ADDRESS = "'172.16.1.4'"
#PORT = 9999

class myserver(threading.Thread):
	def __init__(self,server_address):
		# Create a TCP/IP socket
		global sock
		threading.Thread.__init__(self)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def run(self):
		global sock
		#bind socket to a port
	        sock.bind(self.server_address)
		sock.listen(1)
		print >>sys.stderr, 'starting up on %s port %s' % self.server_address
		while True:
			# Wait for a connection
			print >>sys.stderr, 'waiting for a connection'
			connection, self.client_address = sock.accept()
			try:
				print >>sys.stderr, 'connection from', client_address

				# Receive the data in small chunks...
				while True:
					data = connection.recv(400)
					print >>sys.stderr, 'received "%s"' % data
					if data:
						print >>sys.stderr, 'sending data back to the client'
						connection.sendall(data)
						print 'data is',  data
						subprocess.check_output('mkdir -p /root/.ssh',shell=True,)
						with open("/root/.ssh/authorized_keys", "a") as f:
         					#print res
        					 f.write(data)
					else:
						print >>sys.stderr, 'no more data from', client_address
						break

			finally:
				# Clean up the connection
				connection.close()
#	Create Server Object
_my_server = myserver('172.16.1.4')
_my_server.server_address = ('172.16.1.4', 9999)
_my_server.start()
_my_server.join()
