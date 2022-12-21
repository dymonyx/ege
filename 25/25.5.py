def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

k = 0
for j in range(850_001, 1_000_000):
    if k < 6:
        res = div(j)
        if len(res) > 0:
            if (res[-1] - res[0]) % 3 == 0:
                print(j, res[-1] - res[0])
                k+=1
    else:
        break
