from multiprocessing import Process, Queue, Lock
import os
import time


def f(x, l, q):
    l.acquire()
    time.sleep(1)  # Esperar 'x' segundos
    q.put("Proceso: %d PID: %d" % (x, os.getpid()))  # Introducir msg a la cola
    l.release()

# Funcion 'Cola'


def mostrarCola(q):
    # Imprime la cola
    while True:
        print(q.get())
        # Si la cola esta vacia, sale del While
        if q.empty():
            break


if __name__ == '__main__':  # Proceso 'Padre'
    q = Queue()  # Definir la cola
    lock = Lock()  # 'Lock' para sincronizar los procesos
    for x in range(10):  # 'For' para iniciar 10 procesos
        p = Process(target=f, args=(x, lock, q))  # Definir proceso
        p.start()
        p.join()  # Esperar a que el proceso termine
    mostrarCola(q)  # Iniciar la funcion para imprimir la cola
