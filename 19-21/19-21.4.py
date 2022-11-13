#нельзя повтороять свой пред ход
def f(s, p1, p2, c, m):
    if s >=21: return c%2 == m%2
    if c == m: return 0
    h = []
    if p1 != '+1': h+=[f(s+1, p2, '+1', c+1, m)]
    if p1 != '+2': h+=[f(s+2, p2, '+2', c+1, m)]
    if p1 != '*2': h+=[f(s*2, p2, '*2', c+1, m)]
    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1, 21):
    for m in range(1, 10):
        if f(s, "", "", 0, m) == 1:
            print(s, m)
            break
