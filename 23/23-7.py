from functools import *        #двоичные числа

@lru_cache(None)
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr*2, end) + f(curr+1, end) + f(curr*2 + 1, end)
print(f(4, 218))
