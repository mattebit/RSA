import random
from math import sqrt; from itertools import count, islice

class primeGen:
    def calcPrim(self, cifre):
        num = "1"
        for i in range(1, cifre):
            num += "0"

        num = int(num)
        
##        for f in range(num, int(str("9" + num.split("1")[1]))):
##            if isprime(f):
##                self.

        cond = True

        MAX = ""

        for i in str(num):
            MAX += "9"

        MAX = int(MAX)

        print(MAX)

        cont = 0
        while cond:
            cc = random.randint(num, MAX)
            cont += 1
            if cont%100 == 0:
                print (cont)

            if self.isPrime(cc):
                print(cc)
                return cc

    def isPrime(self, a):
        return all(a % i for i in range(2, a))
    
a = primeGen()

print(a.calcPrim(30))

