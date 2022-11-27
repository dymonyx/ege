from functools import * #самая короткая программа

@lru_cache(None)
def f(curr, end, step):
    if curr > end: return 100000000
    if curr == end: return step
    if curr < end: return min(f(curr + 1, end, step+1), f(curr + 5, end, step+1), f(curr * 3, end, step+1))

print(f(1, 227, 0))
