import random
from math import sqrt; from itertools import count, islice

class qEpGen:
    def __init__(self):
        self.p = 0
        self.q = 0

    def calcPrim(self, cifre):
        num = "1"
        for i in range(1, cifre):
            num += "0"

        num = int(num)
        
##        for f in range(num, int(str("9" + num.split("1")[1]))):
##            if isprime(f):
##                self.

        cond = True
        while cond:
            cc = random.randint(num, int("9" + str(num).split("1")[1]))
            if self.isPrime(cc):
                self.p = cc
                cond = False
        

    def isPrime(self, n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    
a = qEpGen()

a.calcPrim(30)

print(a.p)
