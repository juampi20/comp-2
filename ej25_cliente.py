#!/usr/bin/python3
import socket
import getopt
import time
import sys
import os

(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')

print('opciones: ', opt)

a = ""
p = ""

for (op, ar) in opt:
    if (op == '-a'):
        a = str(ar)
        print('Opcion -a exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    else:
        print('Opcion incorrecta!')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = a
port = p

s.connect((host, port))

while True:
    msg = input('Ingrese msg: ').encode('ascii')
    try:
        s.sendto(msg, (host, port))
    except socket.error:
        print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
        sys.exit()
sys.exit()
