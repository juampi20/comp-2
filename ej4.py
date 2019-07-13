import multiprocessing
from multiprocessing import Process
import os


def child(num):
    print("\n#El hijo incrementa el numero en 2.")
    print("Hijo:", num + 2)  # El Hijo incrementa el numero en 2


if __name__ == "__main__":
    num = int(input("Ingrese numero: "))
    print("\n#El padre incrementa el numero en 4.")
    print("Padre:", num + 4)  # El Padre incrementa el numero en 4
    p = Process(target=child, args=(num,))
    p.start()
    p.join()
