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
    e = calcoloE(pn, k)
    d = calcoloD(e, pn)
    return n, e, d

def cifra(num, e, n): 
    return pow(num, e, n)

def decifra(num, d, n): 
    return pow(num, d, n)

def calcoloE(pn, k): # Calcola e partendo da P(n) e langhezza minima
    while True:
        n = random.randint(pow(2, (k-1)), pn)
        if MCD(n, pn) == 1:
            return n
        
def calcoloD(pn, e):
    return inverse(pn, e)
        
def MCD(a, b):
    while b:
        a, b = b, a%b
    return a

def inverse(a, n): # Extended Ecluidian Algorithm
    t = 0; newt = 1
    r = n; newr = a;
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1: return "Invertible Number"
    if t < 0: t = t + n
    return t

n, e, d = generateKeys(30)
print("n: " + str(n)[:15] + "...")
print("e: " + str(e)[:15] + "...")
print("d: " + str(d)[:15] + "...")

testoInChiaro = "Ciao come va"
print("Testo in chiaro: " + testoInChiaro[:15] + "...")

testoInNumero = textNum.textToNum(testoInChiaro)
print("Testo in numero: " + str(testoInNumero)[:15] + "...")

numeroCifrato = cifra(testoInNumero, e, n)
print("Numero cifrato: " + str(numeroCifrato)[:15] + "...")

numeroDecifrato = decifra(numeroCifrato, d, n)
print("Numero decifrato: " + str(numeroDecifrato)[:15] + "...")

numeroInTesto = textNum.numToText(numeroDecifrato)
print("Numero in testo: " + str(numeroInTesto)[:15] + "...")


