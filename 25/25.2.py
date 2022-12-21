def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for j in range(81234, 134689+1):
    if len(div(j)) == 3:
        print(j, div(j)[0], div(j)[-1])
