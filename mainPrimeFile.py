import primeGen
import time
import sys

args = sys.argv

NOME_FILE = args[1]
FROM = int(args[2])
TO = int(args[3])

f = open(NOME_FILE, "r")
fileBuff = f.read()
f = open(NOME_FILE, "w")
f.write(fileBuff)

t = time.time()

buff = FROM
cont = 0

for i in range(FROM, TO):
    cont += 1
    if cont % 50000 == 0:
        t = time.time() -t
        print(str(i) + " Tempo: " + str(t))
        t = time.time()

    if primeGen.isPrime(i):
        f.write(str(i) + ",")

f.close()
