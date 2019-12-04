#!/usr/bin/python3
import os
import socket
import sys
import threading
import time


def th_server(server):
    print("Launching thread...")
    while True:

        op = server.recv(1024)
        print("Opcion: " + op.decode())

        if (op.decode() == 'ABRIR'):
            arch = '\nNombre del archivo:'
            server.send(arch.encode())
            data = server.recv(1024)
            archivo = 'tmp/'+data.decode()+'.txt'
            fd = open(archivo, 'a+')

        elif (op.decode() == 'AGREGAR'):
            title = 'Texto:'
            server.send(title.encode())
            while True:
                message = server.recv(1024)
                if not message:                 # ERROR ACA, NO SALE DEL LOOP
                    break
                print('Recibido: '+message.decode())
                fd.write(message.decode()+'\n')
            print('Loop ended.')

        elif (op.decode() == 'LEER'):
            for lines in fd:
                server.send(lines.encode())

        elif (op.decode() == 'CERRAR'):
            fd.close()

        else:
            print('Cerrando conexion...')
            break


# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
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
print('Client disconnect...')
