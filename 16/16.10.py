from functools import *


@lru_cache(None)
def f(n):
    if n<=1: return n
    if n%3 ==0: return n+f(n/3)
    return n+f(n+3)


for n in range(-1000, 1000):
        try:                  ##if обязательно стоит после try
            if f(n)>100:
                print(n)
        except:
            pass
