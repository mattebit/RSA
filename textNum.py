# Z27 (alfabeto e spazio) valore*27**posizione

# r = val + letter e r*27

# r = val mod 27 = letter
# val - r/27 =



text = "abc"


class selfNum():
    Z = ["","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "Z", " "]

    def textToNum(self, text, Z_VAL=27):
        n = 0
        for i in text:
            print(i.upper())
            n = (text.index(i)+ 1 + self.Z.index(i.upper())) * Z_VAL
            print(self.Z.index(i.upper()))

        return n

    def numToText(self, num, Z_VAL=27):
        res = ""
        while num != 0:
            res += self.Z[num%Z_VAL]
            num = (num-(num%Z_VAL))/Z_VAL
        return res


print(selfNum().textToNum(text))
