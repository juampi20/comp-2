import os, time

fifo = '/Minichat.txt'


def main():
    fd = open(fifo,os.O_RDWR)
    while True:
        linea = input('\nIngrese mensaje: ')
        linea =
        time.sleep(1)
        if x == '':
            break

if __name__ == '__main__':
    main()
