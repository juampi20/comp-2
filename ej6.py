import signal
import os
import time


def handler(s,f):
    print('\nEsta vez me saldré, inténtalo nuevamente')
    signal.signal(signal.SIGINT, signal.SIG_DFL)


#Registro de señales
signal.signal(signal.SIGINT, handler)


#Tiempo para apretar 'Ctrl + C'
time.sleep(100)
