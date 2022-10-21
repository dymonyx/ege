for n in range(2,1000):
    conter_1 = 0
    conter_0 = 0
    b = bin(n)[2:]
    for i in range(1, len(b), 2):
        if b[i] == '1':
            conter_1 +=1
    for i in range(2, len(b), 2):
        if b[i] == '0':
            conter_0 +=1
    res = abs(conter_0 - conter_1)
    if res == 4:
        print(n)
