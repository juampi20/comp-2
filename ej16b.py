import os, time

fifo = '/Minichat.txt'

def main():
    fd = open(fifo,os.O_RDWR)
    while True:
        x = input('2: ')
        time.sleep(1)
        if x == '':
            break

if __name__ == '__main__':
    main()
