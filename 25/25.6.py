def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(250_000, 250_201):
    arr = [i for i in div(i) if i % 2 == 0]
    if len(arr) == 6:
        print(i, arr[-2], arr[-1])
