import os
import multiprocessing
from multiprocessing import Process


def child():
    for x in range(5):
        print("Soy Hijo.")


if __name__ == '__main__':
    p=Process(target=child)
    p.start()
    for x in range(2):
        print("Soy Padre.")
    p.join()
    print("Mi proceso hijo termino.")
