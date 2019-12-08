import os
import time
from multiprocessing import Process


def childProcess(x, pid):
    print("Process -", x, ", PID Hijo:", os.getpid(), ", PID Padre:", pid)


# Padre
if __name__ == '__main__':
    pid = os.getpid()
    for x in range(1, 4):
        p = Process(target=childProcess, args=(x, pid))
        p.start()
        p.join()
