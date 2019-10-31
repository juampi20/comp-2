from multiprocessing import Queue, Pool
import os, time

def f(x):
    #Esperar 'x' segundos
    time.sleep(x)
    #Introducir msg a la cola
    q.put("Proceso: %d PID: %d" % (x, os.getpid()))

#Funcion 'Cola'
def mostrarCola():
    #Imprime la cola
    while True:
        print (q.get())
        #Si la cola esta vacia, sale del While
        if q.empty():
            break

#Global Queue
q = Queue()

if __name__ == '__main__':
    p = Pool(processes=4)
#    for x in range(10):
#        p.apply(f,args=(x,))
    p.map(f,range(10))
    mostrarCola()
