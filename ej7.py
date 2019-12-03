import os
import time
import signal

# Hijo.


def child():
    print('Hijo:', 'Iniciando...')
    while True:
        print(, 'Hijo:', 'Señal recibida!')
        signal.pause()

# Manejo de señales.


def handler(signum, frame):
    print('Padre:', 'Mandando señal...')
    return


# Registro de señales.
signal.signal(signal.SIGUSR1, handler)

# Creando fork.
pid = os.fork()

if pid == 0:
    child()
# Padre.
else:
    print('Padre:', 'Iniciando...')
    while True:
        os.kill(pid, signal.SIGUSR1)
        time.sleep(5)
