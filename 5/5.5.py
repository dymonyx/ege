for n in range(1,256):
    b = bin(n)[2:]
    b = '0'*(8 - len(b)) + b
    b = b.replace('0', '2').replace('1', '0').replace('2', '1')
    if int(b , 2) - n == 99:
        print(n)
