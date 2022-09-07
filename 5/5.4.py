for n in range(1,128):
    b = bin(n)[2:]
    b = '0'*(8 - len(b)) + b
    b = b.replace('0', '2').replace('1', '0').replace('2', '1')
    r = int(b ,2)
    if r + 1 == 153:
        print(n)
