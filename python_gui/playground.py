import random

def add(*args):
    toplam = 0
    for n in args:
        toplam += n
    print(toplam)

def calculate(**kwargs):
    print(type(kwargs))


calculate(add=3, multiply=5)