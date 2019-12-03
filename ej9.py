import os
import time
import signal

# Manejo de señales


def handler(s, f):
    print("Soy el proceso PID %d recibi la señal %s de mi padre %d" %
          (os.getpid(), s, os.getppid()))


# Registro de señales
signal.signal(signal.SIGUSR1, handler)


def hijo1():
    print("Soy el proceso Hijo %d " % os.getppid())


pid = os.fork()

if pid == 0:
    signal.pause()
    os._exit(0)

pid1 = os.fork()

if pid1 == 0:
    signal.pause()
    os._exit(0)

pid2 = os.fork()

if pid2 == 0:
    signal.pause()
    os._exit(0)

os.kill(pid, signal.SIGUSR1)
os.kill(pid1, signal.SIGUSR1)
os.kill(pid2, signal.SIGUSR1)
