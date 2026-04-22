import random

def add(*args):
    toplam = 0
    for n in args:
        toplam += n
    print(toplam)

def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for (key,value) in kwargs.items():
        print(key,value)


calculate(add=3, multiply=5)