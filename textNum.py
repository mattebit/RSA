# Z27 (alfabeto e spazio) valore*27**posizione

# r = val + letter e r*27

# r = val mod 27 = letter
# val - r/27 =

text = "abc"

class selfNum():
    def text2num(self, text):  # Testo a numero in Z27
        n = 0
        l = list()
        for i in text:
            l.append(ord(i))
        for i in l:
            n = n * 400 + i
        return n

    def num2text(self, num):  # Numero a testo in Z27
        l = list()
        res = num % 400
        l.append(res)
        while num != 0:
            num, res = self._calculation(num, res, 400)
            l.append(res)
        l.remove(0)
        return "".join([chr(i) for i in reversed(l)])

    def _calculation(self, t, k, m):  # Calcoli
        n = (t - k) // m
        q = n % m
        return n, q

print(selfNum().num2text(selfNum().text2num(text)))
