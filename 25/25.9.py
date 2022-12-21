def prime(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

def div(x):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

ans = []
for i in range(158928, 345293+1):
    d = [j for j in div(i) if prime(j)]
    if len(d) == 3 and d[0]*d[1]*d[2] == i:
        ans.append(i)
print(min(ans), len(ans))
