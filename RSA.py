import re
import random
import math
import primeGen
import textNum


def generateKeys(k): # RSA
    p = primeGen.calcPrim(k)
    q = primeGen.calcPrim(k)
    n = p*q
    pn = (p-1)*(q-1)
    e = _calcE(pn, k)
    d = _calcD(e, pn)
    return n, e, d

def encrypt(num, e, n): # Cifra
    return pow(num, e, n)

def decrypt(num, d, n): # Decifra
    return pow(num, d, n)

def _calcE(pn, k): # Calcola e partendo da P(n) e langhezza minima
    while True:
        n = random.randint(pow(2, (k-1)), pn)
        if _mcd(n, pn) == 1:
            return n
        
def _calcD(pn, e):
    return _inverse(pn, e)
        
def _mcd(a, b): # Massimo comune divisore
    while b:
        a, b = b, a%b
    return a

def _inverse(a, n): # Extended Ecluidian Algorithm
    t = 0; newt = 1
    r = n; newr = a;
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1: return "Invertible Number"
    if t < 0: t = t + n
    return t
        
    
##    if __name__ == '__main__': # PROVA
##        debug = True
##        if debug:
##            n, e, d = generateKeys(1024) # Lunghezza in bit della chiave
##            tchiaro = "I am maxrode"
##            print("N: %s... \nE: %s... \nD: %s..."%(str(n)[:16], str(e)[:16], str(d)[:16]))
##            print("Testo in chiaro: %s"%(tchiaro))
##            numero = text2num(tchiaro)
##            print("Testo in numero: %s"%(numero))
##            nCriptato = encrypt(numero, e, n)
##            print("Numero criptato: %s..."%(str(nCriptato)[:16]))
##            nDecriptato = decrypt(nCriptato, d, n)
##            print("Numero decriptato: %s"%(nDecriptato))
##            print("Numero in testo: %s"%(num2text(nDecriptato)))

n, e, d = generateKeys(30)
print("n: " + str(n)[:15] + "...")
print("e: " + str(e)[:15] + "...")
print("d: " + str(d)[:15] + "...")

testoInChiaro = "Ciao come va"
print("Testo in chiaro: " + testoInChiaro[:15] + "...")

testoInNumero = textNum.textToNum(testoInChiaro)
print("Testo in numero: " + str(testoInNumero)[:15] + "...")

numeroCifrato = encrypt(testoInNumero, e, n)
print("Numero cifrato: " + str(numeroCifrato)[:15] + "...")

numeroDecifrato = decrypt(numeroCifrato, d, n)
print("Numero decifrato: " + str(numeroDecifrato)[:15] + "...")

numeroInTesto = textNum.numToText(numeroDecifrato)
print("Numero in testo: " + str(numeroInTesto)[:15] + "...")


