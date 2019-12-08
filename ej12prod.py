import getopt
import sys
import os

(opt, arg) = getopt.getopt(sys.argv[1:], 'a:')

arg = ""

for (op, ar) in opt:
    if(op == '-a'):
        arg = str(ar)

fd = open("/tmp/fifo", "w")

fd.write(arg)

fd.close()
