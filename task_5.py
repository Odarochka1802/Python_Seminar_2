# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)
print("Первый вариант")
class LSFR_PRNG:
    def __init__(self, S=0xdeadbeef):
        self.S = S & 0xffffffff
    def next(self):
        bit = (((self.S >> 31) ^ (self.S >> 30) ^ (self.S >> 29) ^ (self.S >> 27) ^ (self.S >> 25) ^ self.S ) & 0x00000001 )
        self.S = (self.S >> 1)| (bit << 31)
        return self.S
    def randint(self, left, right=None):
        if right is None:
            left, right = 0, left
        if left > right:
            left, right = right, left
        rng = right - left
        return left + self.next()%rng

import time

prng = LSFR_PRNG(hash(time.time()))  

for i in range(5):
    print(prng.randint(1, 10000))
    print(prng.randint(-100, 100))
print("#"*20)
#С классом частично мой код, для меня это пока сложнова-то. Классы только изучаю

print("Второй вариант")
import datetime

def random_number(minimum,maximum):
    now = str(datetime.datetime.now())
    rnd = float(now[::-1][:3:])/1000
    return int(minimum + rnd*(maximum-minimum))

print(random_number(-1000, 1000))
print(random_number(-100, 100))
