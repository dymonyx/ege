a = set()
for i in range(1,5000):
    k = '5'*i
    while '555' in k or '888' in k:
        k = k.replace('555', '8', 1)
        k = k.replace('888', '55', 1)
    a.add(k)
print(len(a))
