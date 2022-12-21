def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(135790, 163229):
    if sum(div(i)) > 460_000:
        print(len(div(i)), sum(div(i)))
