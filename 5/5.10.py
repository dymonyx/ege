for n in range(100,1000):
    b = bin(n)[2:]
    for _ in range(1, 4):
        if  b.count('1') > b.count('0'):
            b = b + '0'
        elif b.count('1') < b.count('0'):
            b = b + '1'
        else:
            b = b + b[-1]
    res = int(b, 2)
    if res % 4 == 0:
        print(n)
        break
