import primeGen
import time
import sys

args = sys.argv

NOME_FILE = "primes/gen1.txt"#args[1]
FROM = 100000000#int(args[2])
TO = 200000000#int(args[3])

f = open(NOME_FILE, "r")
fileBuff = f.read()
f = open(NOME_FILE, "w")
f.write(fileBuff)

t = time.time()

buff = FROM
cont = 0

for i in range(FROM, TO):
    cont += 1
    if cont % 10000 == 0:
        t = time.time() -t
        print(str(i) + " Tempo: " + str(t))
        t = time.time()

    if primeGen.isPrime(i):
        f.write(str(i) + ",")

f.close()
