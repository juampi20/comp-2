#!/usr/bin/python3
import socket
import os
import threading
import sys


def th_server(sock):
    print("Launching thread...")
    while True:
        msg = sock.recv(1024)
        print("Recibido: %s" % msg.decode('ascii'))
        if not msg:
            break
#    sock.close()


# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 1234

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    th = threading.Thread(target=th_server, args=(clientsocket,))
    th.start()
clientsocket.close()
