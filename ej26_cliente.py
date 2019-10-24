#!/usr/bin/python3
import socket, sys, os, time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket!'
    sys.exit()

print 'Socket Created!'

host = int(sys.argv[1])
port = int(sys.argv[2])

s.connect((host, port))

print 'Socket Connected to ' + host + 'in port' + port

while True:
    msg = input('Ingrese msg: ').encode()
    if msg == 'exit':
        sys.exit()
    else:
        try :
        	#Set the whole string
        	s.sendto(msg,(host, port))
        except socket.error:
        	#Send failed
        	print 'Send failed'
        	sys.exit()
        print 'Message send successfully'
        sys.exit()

s.close()
