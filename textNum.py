# Z27 (alfabeto e spazio) valore*27**posizione

# r = val + letter e r*27

# r = val mod 27 = letter
# val - r/27 =

def textToNum(text): # Z27
    n = 0
    l = list()
    for i in text:
        l.append(ord(i))
    for i in l:
        n = n * 400 + i
    return n

def numToText(num): # Z27
    l = list()
    res = num % 400
    l.append(res)
    while num != 0:
        num, res = _calculation(num, res, 400)
        l.append(res)
    l.remove(0)
    return "".join([chr(i) for i in reversed(l)])

def _calculation(t, k, m):  
    n = (t - k) // m
    q = n % m
    return n, q


