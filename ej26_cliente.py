#!/usr/bin/python3
import socket
import sys
import os
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Fallo al crear el socket!')
    sys.exit()

print('Socket Creado!')

host = str(sys.argv[1])
port = int(sys.argv[2])

s.connect((host, port))

print('Socket conectado al host', host, 'en el puerto', port)

while True:
    msg = input('Ingrese msg: ').encode()
    if msg.decode() == 'exit':
        break
    else:
        try:
            if not msg:
                break
            s.sendto(msg, (host, port))
        except socket.error:
            # Send failed
            print('Fallo al enviar el msg!')
            sys.exit()

s.close()
