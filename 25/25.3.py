def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for j in range(244143, 367821+1):
    if len(div(j)) == 5:
        print(div(j)[-2], div(j)[-1])
