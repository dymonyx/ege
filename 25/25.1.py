def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for j in range(193136, 193224):
    if len(div(j)) == 6:
        print(div(j), j)
