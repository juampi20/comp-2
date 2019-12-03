import os
import sys
import time
from multiprocessing import Process, Pipe


def main():
    fifo_fd = open('Fifo', "r")
    line = fifo_fd.readline()
    lector_conn, escritor_conn = Pipe()
    p = Process(target=hijo, args=(lector_conn, ))
    p.start()
    escritor_conn.send(line)
    p.join()


def hijo(lector_conn):
    print("El mensaje recibido es: ", lector_conn.recv())


if __name__ == '__main__':
    main()
