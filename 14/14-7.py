def f(x, y):
    return int('12'+ str(y) + x +'9', 21) + int('36' + str(y) + '99', 21)

for x in '0123456789ABCDEFGEIJK':
    for y in '0123456789ABCDEFGEIJK':
        if f(x, y) % 18 == 0:
            print(f(x, 5)/18)
            break
