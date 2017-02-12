import random

f = open("prime.txt", "r")

fileBuff = f.read()

f = open("prime.txt","w")

f.write(fileBuff)

def isPrime(a):
    return all(a % i for i in range(2, a))



buff = 6
cont = 0
for i in range(113657, 1000000000000000000):
    cont += 1
    if cont % 500 == 0:
        print(cont)

    if len(str(i)) == len(str(buff)):
        if isPrime(i):
            f.write(str(i) + ",")
    else:
        f.write("]" + "\n" + "[")
        if isPrime(i):
            f.write(str(i) + ",")

    buff = i
