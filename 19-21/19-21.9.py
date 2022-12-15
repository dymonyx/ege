def f(s, c, m):
    if s >= 103: return c%2 == m%2
    if c == m: return 0
    h = []
    if (s+2) % 3!= 0: h+=[f(s+2, c+1, m)]
    if (s+1) % 3!= 0: h+=[f(s+1, c+1, m)]
    if (s*2) % 3!= 0: h+=[f(s*2, c+1, m)]
    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1, 102):
    for m in range(1, 7):
        if f(s, 0, m) == 1:
            print(s, m)


#19 - 50
#20 - 25 49
#21 - 47
