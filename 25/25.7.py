def div(x):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for j in range(500_000, 500_021):
    d1 = [i for i in div(j) if (i!=8 and i!=j and i%10 == 8)]
    if len(d1) > 0:
        print(j, min(d1))
