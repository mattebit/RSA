# Z27 (alfabeto e spazio) valore*27**posizione

# r = val + letter e r*27

# r = val mod 27 = letter
# val - r/27 =



text = "ciao"


class selfNum():
    Z = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "Z", " "]

    def textToNum(self, text, Z_VAL=27):
        n = 0
        for i in text:
            print(i.upper())
            n = (text.index(i) + self.Z.index(i.upper())) * Z_VAL

        return n

    def numToText(self, num, Z_VAL=27):
        res = ""
        while num != 0:
            res += Z[num%Z_VAL]
            num = (num-(num%Z_VAL))/Z_VAL


print(selfNum().textToNum(text))
print(selfNum().numToText(selfNum().textToNum(text)))