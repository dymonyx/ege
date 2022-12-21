def prime(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

def div(x):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(650_000, 650_500):
    d = [j for j in div(i) if prime(j)]
    if sum(d) % 100 == 25:
        print(i, sum(d))
