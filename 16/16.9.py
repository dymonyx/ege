def f(n):
    if n<= 5: return n
    if n>= 5 and n%4 == 0: return n + f(n/2 -1)
    return n + f(n+2)


for n in range(1,1000):
    try:
        print(n, f(n))
    except:
        pass
