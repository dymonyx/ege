s = open('24 (3).txt').readline()
kMin, k = len(s), 0
for i in s:
    if i == 'A':
        k += 1
    elif k != 0:
        kMin = min(kMin, k)
        k = 0
kMin = min(kMin, k)
print(kMin)
