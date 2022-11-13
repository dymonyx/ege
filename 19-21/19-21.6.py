#чет нечет
def f(s, c, m):
    if s >=51: return c%2 == m%2
    if c == m: return 0
    h = []
    if (s+1)%2 != 0: h+=[f(s+1, c+1, m)]
    if (s+3)%2 != 0: h+=[f(s+3, c+1, m)]
    if (s*3)%2 != 0: h+=[f(s*3, c+1, m)]
    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1, 50):
    for m in range(1, 10):
        if f(s, 0, m) == 1:
            print(s, m)
            break
