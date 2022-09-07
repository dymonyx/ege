k = 0
for i in range(1, 100):
    b = bin(i)[2:]
    b += str(b.count('1')%2)
    b += str(b.count('1')%2)
    if 210 <= int(b,2) <= 260:
        k+=1
print(k)
