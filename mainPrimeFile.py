import primeGen
import time

prime = primeGen.primeGen()

# print(prime.calcPrim(1024))

f = open("prime.txt", "r")

fileBuff = f.read()

f = open("prime.txt", "w")

f.write(fileBuff)

t = time.time()

buff = 60000000
cont = 0

for i in range(60000000, 70000000):

    cont += 1
    if cont % 5000 == 0:
        t = time.time() -t
        print(str(i) + " Tempo: " + str(t))
        t = time.time()

    if prime.isPrime(i):
        f.write(str(i) + ",")

