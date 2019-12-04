#!/usr/bin/python3
import socket
import sys
import os
import getopt
import time

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Fallo al crear el socket!')
    sys.exit()

print('Socket Creado!')

host = "127.0.0.1"
port = 1234

client.connect((host, port))

print('Socket conectado al host', host, 'en el puerto', port)

while True:

    print("""\n
    \t\t *** Menu ***
    - ABRIR
    - AGREGAR
    - LEER
    - CERRAR
    """)

    option = input('Opcion: ')

    client.sendto(option.encode(), (host, port))

    if (option == 'ABRIR'):
        print(client.recv(1024).decode())
        msg = input()
        client.sendto(msg.encode(), (host, port))

    elif (option == 'AGREGAR'):
        empty = ''
        print(client.recv(1024).decode())
        while True:
            msg = input()
            client.sendto(msg.encode(), (host, port))
            if msg == empty:
                break
        input('\nToque Enter para continuar...')

    elif (option == 'LEER'):
        while True:
            data = client.recv(1024)
            if data:
                print(data.decode())
            else:
                break

        input('\nToque Enter para continuar...')

    elif (option == 'CERRAR'):
        client.close()

    else:
        print('Opcion incorrecta!')

client.close()
