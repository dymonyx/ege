res = []
minn = 118
a = [int(c) for c in open('17_8475.txt')]
for i in range(len(a)-2):
    if (a[i]**2 > 988**2) + (a[i+1]**2 > 988**2) + (a[i+2]**2 > 988**2) == 2:
        if 99<abs(a[i])<1000 or 99<abs(a[i+1])<1000 or 99<abs(a[i+2])<1000:
            res.append(a[i]+a[i+1]+a[i+2])

print(len(res), max(res))
