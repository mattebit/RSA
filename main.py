import primeGen

#prime = primeGen.primeGen()

#print(prime.calcPrim(400))

f= open("prova.txt", "w")
prime = primeGen.primeGen()


for i in range(1,10000000):
    if i%10000 == 0:
        print(i)

    if prime.isPrime(i):
        f.write(str(i) + " ")