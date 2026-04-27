#14-misol
class Oyin:
    def __init__(self, nomi):
        self.nomi = nomi

    def boshlash(self):
        print("O‘yin boshlandi")

class Shaxmat(Oyin):

    def boshlash(self):
        print("O‘yin boshlandi")

o1 = Oyin("vnzv;")
o2 = Shaxmat(Oyin)

o1.boshlash()
o2.boshlash()
